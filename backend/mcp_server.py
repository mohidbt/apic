#!/usr/bin/env python3
"""
MCP Server for APIIngest.

Exposes stored API specs as discoverable MCP resources and tools,
implementing the progressive-disclosure pattern:
  docs://specs                — list all stored specs
  docs://specs/{id}/manifest  — manifest (title, version, auth, endpoint index)
  docs://specs/{id}/tags/{tag} — per-tag summary
  docs://specs/{id}/endpoints/{operationId} — single endpoint block
  docs://specs/{id}/schemas/{name} — single component schema
  docs://specs/{id}/tools     — JSON tool definitions for all endpoints

Tools:
  convert_spec        — convert local raw spec to context-loading payload
  search_specs        — search marketplace specs
  load_spec           — load marketplace spec to context-loading payload
  get_chunk           — fetch one chunk (with manifest) for local or marketplace source
  convert_spec_to_tools — convert raw spec to function-calling tool schemas

Env vars (HTTP transport):
  MCP_TRANSPORT       — "streamable-http" (default) or "stdio"
  MCP_HOST            — bind address (default "0.0.0.0")
  MCP_PORT            — listen port (default 8080)
  MCP_API_TOKEN       — optional admin fallback token (user tokens validated via DB)
  MCP_TOKEN_THRESHOLD — recommended token threshold (default 4000)
"""

import hashlib
import json
import os
import re
import tempfile
import time
from pathlib import Path
from typing import Any
from uuid import uuid4

from mcp.server.fastmcp import FastMCP

import crud.specs as crud
from models.api_spec import ApiSpec
from models.database import SessionLocal
from models.user import ApiToken
from transformation import OpenAPIToMarkdown
from utils import estimate_token_count

_CONVERSION_CACHE: dict[tuple[str, str, str], tuple[dict[str, Any], OpenAPIToMarkdown, str]] = {}
_MAX_CACHE_SIZE = 32
MCP_TOKEN_THRESHOLD = int(os.getenv("MCP_TOKEN_THRESHOLD", "4000"))

mcp = FastMCP(
    "APIIngest",
    stateless_http=True,
    json_response=True,
    streamable_http_path="/",
    instructions=(
        "This server supports two workflows for API docs: "
        "(1) convert local specs with convert_spec; "
        "(2) search marketplace specs with search_specs then load_spec. "
        "Always check token_count: if small, load full_markdown; "
        "if large, start with manifest + chunks_available and fetch specific chunks with get_chunk."
    ),
)


def _get_spec_row(spec_id: int) -> ApiSpec:
    db = SessionLocal()
    try:
        spec = db.query(ApiSpec).filter(ApiSpec.id == spec_id).first()
        if not spec:
            raise ValueError(f"Spec {spec_id} not found")
        db.expunge(spec)
        return spec
    finally:
        db.close()


def _get_cached_conversion(
    spec_id: int, content: str, fmt: str
) -> tuple[dict[str, Any], OpenAPIToMarkdown, str]:
    """Convert DB spec content and cache by (db, spec_id, content_hash)."""
    content_hash = hashlib.md5(content.encode()).hexdigest()
    key = ("db", str(spec_id), content_hash)
    if key in _CONVERSION_CACHE:
        return _CONVERSION_CACHE[key]

    for cache_key in list(_CONVERSION_CACHE.keys()):
        if cache_key[0] == "db" and cache_key[1] == str(spec_id):
            del _CONVERSION_CACHE[cache_key]

    while len(_CONVERSION_CACHE) >= _MAX_CACHE_SIZE:
        del _CONVERSION_CACHE[next(iter(_CONVERSION_CACHE))]

    ext = _FORMAT_TO_EXT.get(fmt, ".yaml")
    with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(content)
        tmp = f.name
    try:
        converter = OpenAPIToMarkdown(tmp)
        chunked = converter.convert_chunked()
        full_markdown = converter.convert()
        result = (chunked, converter, full_markdown)
        _CONVERSION_CACHE[key] = result
        return result
    finally:
        Path(tmp).unlink(missing_ok=True)


def _cache_local_conversion(
    conversion_id: str,
    content: str,
    fmt: str,
) -> tuple[dict[str, Any], OpenAPIToMarkdown, str]:
    """Convert local content and cache by (local, conversion_id)."""
    key = ("local", conversion_id, "")
    if key in _CONVERSION_CACHE:
        return _CONVERSION_CACHE[key]

    while len(_CONVERSION_CACHE) >= _MAX_CACHE_SIZE:
        del _CONVERSION_CACHE[next(iter(_CONVERSION_CACHE))]

    ext = _FORMAT_TO_EXT.get(fmt, ".yaml")
    with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(content)
        tmp = f.name
    try:
        converter = OpenAPIToMarkdown(tmp)
        chunked = converter.convert_chunked()
        full_markdown = converter.convert()
        result = (chunked, converter, full_markdown)
        _CONVERSION_CACHE[key] = result
        return result
    finally:
        Path(tmp).unlink(missing_ok=True)


def _get_local_conversion(conversion_id: str) -> tuple[dict[str, Any], OpenAPIToMarkdown, str]:
    key = ("local", conversion_id, "")
    result = _CONVERSION_CACHE.get(key)
    if not result:
        raise ValueError(f"Local conversion '{conversion_id}' not found")
    return result


def _get_chunked_and_converter(spec_id: int) -> tuple[dict[str, Any], OpenAPIToMarkdown, str]:
    """Fetch spec from DB and return cached (chunked_dict, converter, full_markdown)."""
    spec = _get_spec_row(spec_id)
    return _get_cached_conversion(spec_id, spec.original_content, spec.original_format)


def _extract_endpoint_summary(endpoint_block: str) -> str:
    match = re.search(r"ENDPOINT:\s+\[(\w+)\]\s+(.+)", endpoint_block)
    if match:
        return f"{match.group(1)} {match.group(2)}"
    return "endpoint"


def _extract_schema_summary(schema_block: str) -> str:
    schema_type = "schema"
    match = re.search(r"\*\*Type:\*\*\s+([^\n]+)", schema_block)
    if match:
        schema_type = match.group(1).strip()
    field_count = schema_block.count("\n  - **")
    if field_count > 0:
        return f"{schema_type} ({field_count} fields)"
    return schema_type


def _build_chunks_index(chunked: dict[str, Any]) -> list[dict[str, str]]:
    chunks: list[dict[str, str]] = []

    for tag_name, tag_markdown in sorted(chunked.get("tags", {}).items()):
        endpoint_count = sum(
            1 for line in tag_markdown.splitlines() if line.strip().startswith("- **")
        )
        chunks.append(
            {
                "type": "tag",
                "chunk_type": "tag",
                "key": tag_name,
                "chunk_key": tag_name,
                "summary": f"{endpoint_count} endpoints",
            }
        )

    for op_id, endpoint_block in sorted(chunked.get("endpoints", {}).items()):
        chunks.append(
            {
                "type": "endpoint",
                "chunk_type": "endpoint",
                "key": op_id,
                "chunk_key": op_id,
                "summary": _extract_endpoint_summary(endpoint_block),
            }
        )

    for schema_name, schema_block in sorted(chunked.get("schemas", {}).items()):
        chunks.append(
            {
                "type": "schema",
                "chunk_type": "schema",
                "key": schema_name,
                "chunk_key": schema_name,
                "summary": _extract_schema_summary(schema_block),
            }
        )

    return chunks


def _build_context_payload(
    *,
    source_id: str,
    id_field: str,
    source_type: str,
    chunked: dict[str, Any],
    full_markdown: str,
    token_count: int,
) -> str:
    payload: dict[str, Any] = {
        id_field: source_id,
        "source_type": source_type,
        "token_count": token_count,
        "token_threshold": MCP_TOKEN_THRESHOLD,
        "full_markdown": full_markdown,
        "manifest": chunked["manifest"],
        "chunks_available": _build_chunks_index(chunked),
    }
    if id_field != "source_id":
        payload["source_id"] = source_id
    return json.dumps(payload, indent=2)


def _get_chunk_content(chunked: dict[str, Any], chunk_type: str, chunk_key: str) -> str:
    if chunk_type == "tag":
        value = chunked.get("tags", {}).get(chunk_key)
    elif chunk_type == "endpoint":
        value = chunked.get("endpoints", {}).get(chunk_key)
    elif chunk_type == "schema":
        value = chunked.get("schemas", {}).get(chunk_key)
    else:
        raise ValueError("chunk_type must be one of: tag, endpoint, schema")

    if value is None:
        raise ValueError(f"{chunk_type} chunk '{chunk_key}' not found")
    return value


def _marketplace_row_to_summary(spec: ApiSpec) -> dict[str, Any]:
    return {
        "id": spec.id,
        "spec_id": spec.id,
        "name": spec.name,
        "version": spec.version,
        "provider": spec.provider,
        "token_count": spec.token_count,
        "tags": [t.name for t in spec.tags] if spec.tags else [],
    }


# ── Resources ──────────────────────────────────────────────────────────


@mcp.resource("docs://specs")
def list_specs() -> str:
    """List all stored API specs (id, name, version, token_count)."""
    db = SessionLocal()
    try:
        specs = db.query(ApiSpec).order_by(ApiSpec.uploaded_at.desc()).all()
        rows = []
        for s in specs:
            rows.append(
                {
                    "id": s.id,
                    "spec_id": s.id,
                    "name": s.name,
                    "version": s.version,
                    "token_count": s.token_count,
                    "tags": [t.name for t in s.tags] if s.tags else [],
                }
            )
        return json.dumps(rows, indent=2)
    finally:
        db.close()


@mcp.resource("docs://specs/{spec_id}/manifest")
def get_manifest(spec_id: int) -> str:
    """
    Manifest for a spec: title, version, base URLs, auth, and
    a tag-grouped endpoint index. Small enough to fit in any context window.
    """
    chunked, _, _ = _get_chunked_and_converter(spec_id)
    return chunked["manifest"]


@mcp.resource("docs://specs/{spec_id}/tags/{tag_name}")
def get_tag_summary(spec_id: int, tag_name: str) -> str:
    """Per-tag endpoint listing with operationIds and summaries."""
    chunked, _, _ = _get_chunked_and_converter(spec_id)
    tag = chunked["tags"].get(tag_name)
    if tag is None:
        available = ", ".join(sorted(chunked["tags"].keys()))
        raise ValueError(f"Tag '{tag_name}' not found. Available: {available}")
    return tag


@mcp.resource("docs://specs/{spec_id}/endpoints/{operation_id}")
def get_endpoint(spec_id: int, operation_id: str) -> str:
    """
    Full endpoint block for a single operationId — includes method, path,
    base URL, params, request/response schemas, auth, and curl example.
    """
    chunked, _, _ = _get_chunked_and_converter(spec_id)
    ep = chunked["endpoints"].get(operation_id)
    if ep is None:
        available = ", ".join(sorted(chunked["endpoints"].keys())[:20])
        raise ValueError(
            f"Endpoint '{operation_id}' not found. "
            f"Sample available: {available}..."
        )
    return ep


@mcp.resource("docs://specs/{spec_id}/schemas/{schema_name}")
def get_schema(spec_id: int, schema_name: str) -> str:
    """Single component schema definition."""
    chunked, _, _ = _get_chunked_and_converter(spec_id)
    schema = chunked["schemas"].get(schema_name)
    if schema is None:
        available = ", ".join(sorted(chunked["schemas"].keys())[:20])
        raise ValueError(
            f"Schema '{schema_name}' not found. "
            f"Sample available: {available}..."
        )
    return schema


@mcp.resource("docs://specs/{spec_id}/tools")
def get_tool_schemas(spec_id: int) -> str:
    """JSON tool definitions for all endpoints — ready for function-calling."""
    _, converter, _ = _get_chunked_and_converter(spec_id)
    tools = converter.generate_tool_schemas()
    return json.dumps(tools, indent=2)


# ── Tools ──────────────────────────────────────────────────────────────


_FORMAT_TO_EXT = {
    "yaml": ".yaml",
    "yml": ".yaml",
    "json": ".json",
    "raml": ".raml",
    "apib": ".apib",
    "wsdl": ".wsdl",
    "graphql": ".graphql",
    "gql": ".graphql",
}


@mcp.tool()
def convert_spec(content: str, format: str = "yaml") -> str:
    """
    Convert a local API spec into smart-loading artifacts.

    Recommended flow:
    1) Check token_count against token_threshold (default 4000).
    2) If small, use full_markdown directly.
    3) If large, use manifest + chunks_available and fetch specific chunks via get_chunk.
    """
    conversion_id = str(uuid4())
    chunked, _, full_markdown = _cache_local_conversion(conversion_id, content, format)
    token_count = estimate_token_count(full_markdown)
    return _build_context_payload(
        source_id=conversion_id,
        id_field="conversion_id",
        source_type="local",
        chunked=chunked,
        full_markdown=full_markdown,
        token_count=token_count,
    )


@mcp.tool()
def search_specs(query: str = "", tag: str = "") -> str:
    """
    Search marketplace specs by query and/or tag.

    - If tag is provided, filter by tag.
    - If query is provided, search name/provider/markdown.
    - If neither is provided, list latest specs.
    """
    db = SessionLocal()
    try:
        if tag:
            specs, _ = crud.filter_by_tag(db, tag, 0, 50)
        elif query:
            specs, _ = crud.search_specs(db, query, 0, 50)
        else:
            specs, _ = crud.list_specs(db, 0, 50, None)
        return json.dumps([_marketplace_row_to_summary(spec) for spec in specs], indent=2)
    finally:
        db.close()


@mcp.tool()
def load_spec(spec_id: int) -> str:
    """
    Load a marketplace spec into smart-loading artifacts.

    Recommended flow:
    1) Check token_count against token_threshold (default 4000).
    2) If small, use full_markdown directly.
    3) If large, use manifest + chunks_available and fetch specific chunks via get_chunk.
    """
    spec = _get_spec_row(spec_id)
    chunked, _, full_markdown = _get_chunked_and_converter(spec_id)
    token_count = (
        spec.token_count if spec.token_count is not None else estimate_token_count(full_markdown)
    )
    return _build_context_payload(
        source_id=str(spec_id),
        id_field="spec_id",
        source_type="marketplace",
        chunked=chunked,
        full_markdown=full_markdown,
        token_count=token_count,
    )


@mcp.tool()
def get_chunk(source_id: str, source_type: str, chunk_type: str, chunk_key: str) -> str:
    """
    Fetch one chunk plus the manifest for context packing.

    source_type:
      - local: source_id is conversion_id returned by convert_spec
      - marketplace: source_id is spec_id returned by search_specs/load_spec
    """
    if source_type == "local":
        chunked, _, _ = _get_local_conversion(source_id)
    elif source_type == "marketplace":
        try:
            spec_id = int(source_id)
        except ValueError as exc:
            raise ValueError(
                "For marketplace source_type, source_id must be an integer string"
            ) from exc
        chunked, _, _ = _get_chunked_and_converter(spec_id)
    else:
        raise ValueError("source_type must be one of: local, marketplace")

    chunk_content = _get_chunk_content(chunked, chunk_type, chunk_key)
    return json.dumps(
        {
            "source_id": source_id,
            "source_type": source_type,
            "chunk_type": chunk_type,
            "chunk_key": chunk_key,
            "manifest": chunked["manifest"],
            "chunk_content": chunk_content,
        },
        indent=2,
    )


@mcp.tool()
def convert_spec_to_tools(content: str, format: str = "yaml") -> str:
    """
    Convert raw API spec to JSON tool schemas for function-calling.

    This tool is independent from smart context loading and returns only callable
    tool definitions.
    """
    ext = _FORMAT_TO_EXT.get(format, ".yaml")
    with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(content)
        tmp = f.name
    try:
        converter = OpenAPIToMarkdown(tmp)
        tools = converter.generate_tool_schemas()
        return json.dumps(tools, indent=2)
    finally:
        Path(tmp).unlink(missing_ok=True)


def _validate_bearer_token(raw_token: str, admin_token: str | None) -> bool:
    """Check bearer token against the admin fallback and the api_tokens table."""
    if admin_token and raw_token == admin_token:
        return True
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    db = SessionLocal()
    try:
        row = (
            db.query(ApiToken)
            .filter(ApiToken.token_hash == token_hash, ApiToken.revoked_at.is_(None))
            .first()
        )
        if not row:
            return False
        # Debounced last_used_at update (skip if < 60s ago)
        now_ts = time.time()
        if row.last_used_at is None or (now_ts - row.last_used_at.timestamp()) > 60:
            from datetime import datetime, timezone

            row.last_used_at = datetime.now(timezone.utc)
            db.commit()
        return True
    finally:
        db.close()


if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "streamable-http")

    if transport == "stdio":
        mcp.run(transport="stdio")
    else:
        import contextlib

        import uvicorn
        from starlette.applications import Starlette
        from starlette.responses import JSONResponse
        from starlette.routing import Mount
        from starlette.types import ASGIApp, Receive, Scope, Send

        host = os.getenv("MCP_HOST", "0.0.0.0")
        port = int(os.getenv("MCP_PORT", "8080"))
        admin_token = os.getenv("MCP_API_TOKEN") or None

        class _BearerTokenMiddleware:
            """Validate bearer tokens against the DB (and optional admin fallback)."""

            def __init__(self, app: ASGIApp, admin_token: str | None):
                self.app = app
                self.admin_token = admin_token

            async def __call__(self, scope: Scope, receive: Receive, send: Send):
                if scope["type"] == "http":
                    headers = dict(scope.get("headers", []))
                    auth_value = headers.get(b"authorization", b"").decode()
                    if not auth_value.startswith("Bearer "):
                        resp = JSONResponse({"error": "unauthorized"}, status_code=401)
                        await resp(scope, receive, send)
                        return
                    raw = auth_value[7:]
                    if not _validate_bearer_token(raw, self.admin_token):
                        resp = JSONResponse({"error": "unauthorized"}, status_code=401)
                        await resp(scope, receive, send)
                        return
                await self.app(scope, receive, send)

        @contextlib.asynccontextmanager
        async def lifespan(app):
            async with mcp.session_manager.run():
                yield

        starlette_app = Starlette(
            routes=[Mount("/", app=mcp.streamable_http_app())],
            lifespan=lifespan,
        )
        authed_app = _BearerTokenMiddleware(starlette_app, admin_token)

        uvicorn.run(authed_app, host=host, port=port)
