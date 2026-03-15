#!/usr/bin/env python3
"""
MCP Server for APIIngest.

Exposes stored API specs as discoverable MCP resources and tools,
implementing the progressive-disclosure pattern:
  docs://specs              — list all stored specs
  docs://specs/{id}/manifest — manifest (title, version, auth, endpoint index)
  docs://specs/{id}/tags/{tag} — per-tag summary
  docs://specs/{id}/endpoints/{operationId} — single endpoint block
  docs://specs/{id}/schemas/{name} — single component schema
  docs://specs/{id}/tools    — JSON tool definitions for all endpoints

Tools:
  convert_spec — convert raw OpenAPI YAML/JSON to chunked markdown on the fly

Env vars (HTTP transport):
  MCP_TRANSPORT   — "streamable-http" (default) or "stdio"
  MCP_HOST        — bind address (default "0.0.0.0")
  MCP_PORT        — listen port  (default 8080)
  MCP_API_TOKEN   — optional admin fallback token (user tokens validated via DB)
"""

import hashlib
import json
import os
import tempfile
import time
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from models.database import SessionLocal
from models.api_spec import ApiSpec
from models.user import ApiToken
from transformation import OpenAPIToMarkdown

_CONVERSION_CACHE: dict[tuple[int, str], tuple[dict, OpenAPIToMarkdown]] = {}
_MAX_CACHE_SIZE = 32

mcp = FastMCP(
    "APIIngest",
    stateless_http=True,
    json_response=True,
    streamable_http_path="/",
    instructions=(
        "This server exposes LLM-ready API documentation. "
        "Start with docs://specs to list available APIs, then drill into "
        "manifest, tags, endpoints, or schemas for the one you need."
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
) -> tuple[dict, OpenAPIToMarkdown]:
    """Convert spec content to chunked dict + converter, cached by (spec_id, content_hash)."""
    content_hash = hashlib.md5(content.encode()).hexdigest()
    key = (spec_id, content_hash)
    if key in _CONVERSION_CACHE:
        return _CONVERSION_CACHE[key]

    for k in list(_CONVERSION_CACHE.keys()):
        if k[0] == spec_id:
            del _CONVERSION_CACHE[k]
    while len(_CONVERSION_CACHE) >= _MAX_CACHE_SIZE:
        del _CONVERSION_CACHE[next(iter(_CONVERSION_CACHE))]

    ext = _FORMAT_TO_EXT.get(fmt, ".yaml")
    with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(content)
        tmp = f.name
    try:
        converter = OpenAPIToMarkdown(tmp)
        chunked = converter.convert_chunked()
        result = (chunked, converter)
        _CONVERSION_CACHE[key] = result
        return result
    finally:
        Path(tmp).unlink(missing_ok=True)


def _get_chunked_and_converter(spec_id: int) -> tuple[dict, OpenAPIToMarkdown]:
    """Fetch spec from DB and return cached (chunked_dict, converter)."""
    spec = _get_spec_row(spec_id)
    return _get_cached_conversion(spec_id, spec.original_content, spec.original_format)


# ── Resources ──────────────────────────────────────────────────────────


@mcp.resource("docs://specs")
def list_specs() -> str:
    """List all stored API specs (id, name, version, token_count)."""
    db = SessionLocal()
    try:
        specs = db.query(ApiSpec).order_by(ApiSpec.uploaded_at.desc()).all()
        rows = []
        for s in specs:
            rows.append({
                "id": s.id,
                "name": s.name,
                "version": s.version,
                "token_count": s.token_count,
                "tags": [t.name for t in s.tags] if s.tags else [],
            })
        return json.dumps(rows, indent=2)
    finally:
        db.close()


@mcp.resource("docs://specs/{spec_id}/manifest")
def get_manifest(spec_id: int) -> str:
    """
    Manifest for a spec: title, version, base URLs, auth, and
    a tag-grouped endpoint index. Small enough to fit in any context window.
    """
    chunked, _ = _get_chunked_and_converter(spec_id)
    return chunked["manifest"]


@mcp.resource("docs://specs/{spec_id}/tags/{tag_name}")
def get_tag_summary(spec_id: int, tag_name: str) -> str:
    """Per-tag endpoint listing with operationIds and summaries."""
    chunked, _ = _get_chunked_and_converter(spec_id)
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
    chunked, _ = _get_chunked_and_converter(spec_id)
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
    chunked, _ = _get_chunked_and_converter(spec_id)
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
    _, converter = _get_chunked_and_converter(spec_id)
    tools = converter.generate_tool_schemas()
    return json.dumps(tools, indent=2)


# ── Tools ──────────────────────────────────────────────────────────────


_FORMAT_TO_EXT = {
    "yaml": ".yaml", "yml": ".yaml", "json": ".json",
    "raml": ".raml", "apib": ".apib", "wsdl": ".wsdl",
    "graphql": ".graphql", "gql": ".graphql",
}


@mcp.tool()
def convert_spec(content: str, format: str = "yaml") -> str:
    """
    Convert raw API spec content to chunked LLM-ready markdown.

    Args:
        content: The API spec as a string (YAML, JSON, RAML, API Blueprint, WSDL, or GraphQL).
        format: One of yaml, json, raml, apib, wsdl, graphql (default "yaml").

    Returns:
        JSON with keys: manifest, tags, endpoints, schemas.
    """
    ext = _FORMAT_TO_EXT.get(format, ".yaml")
    with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(content)
        tmp = f.name
    try:
        converter = OpenAPIToMarkdown(tmp)
        chunked = converter.convert_chunked()
        return json.dumps(chunked, indent=2)
    finally:
        Path(tmp).unlink(missing_ok=True)


@mcp.tool()
def convert_spec_to_tools(content: str, format: str = "yaml") -> str:
    """
    Convert raw API spec to JSON tool schemas for function-calling.

    Args:
        content: The API spec as a string (YAML, JSON, RAML, API Blueprint, WSDL, or GraphQL).
        format: One of yaml, json, raml, apib, wsdl, graphql (default "yaml").

    Returns:
        JSON array of tool definitions.
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
