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
"""

import hashlib
import json
import tempfile
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from models.database import SessionLocal
from models.api_spec import ApiSpec
from transformation import OpenAPIToMarkdown

_CONVERSION_CACHE: dict[tuple[int, str], tuple[dict, OpenAPIToMarkdown]] = {}
_MAX_CACHE_SIZE = 32

mcp = FastMCP(
    "APIIngest",
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

    ext = ".yaml" if fmt in ("yaml", "yml") else ".json"
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


@mcp.tool()
def convert_spec(content: str, format: str = "yaml") -> str:
    """
    Convert raw OpenAPI spec content to chunked LLM-ready markdown.

    Args:
        content: The OpenAPI spec as a string (YAML or JSON).
        format: "yaml" or "json" (default "yaml").

    Returns:
        JSON with keys: manifest, tags, endpoints, schemas.
    """
    ext = ".yaml" if format in ("yaml", "yml") else ".json"
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
    Convert raw OpenAPI spec to JSON tool schemas for function-calling.

    Args:
        content: The OpenAPI spec as a string (YAML or JSON).
        format: "yaml" or "json" (default "yaml").

    Returns:
        JSON array of tool definitions.
    """
    ext = ".yaml" if format in ("yaml", "yml") else ".json"
    with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(content)
        tmp = f.name
    try:
        converter = OpenAPIToMarkdown(tmp)
        tools = converter.generate_tool_schemas()
        return json.dumps(tools, indent=2)
    finally:
        Path(tmp).unlink(missing_ok=True)


if __name__ == "__main__":
    mcp.run()
