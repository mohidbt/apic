"""
P1 tests for multi-format API spec support.

Validates that RAML, API Blueprint, WSDL, and GraphQL files are accepted
and parsed (best-effort) by both the transformation layer and main.py helpers.
"""

import re
import tempfile
from pathlib import Path
import pytest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from transformation import OpenAPIToMarkdown
from main import load_openapi_spec, ALLOWED_EXTENSIONS, FORMAT_MAP

# ── Inline fixtures ───────────────────────────────────────────────────

RAML_CONTENT = """\
#%RAML 1.0
title: Hello API
/hello:
  get:
    responses:
      200:
        body:
          application/json:
            example: |
              {"message": "hello"}
"""

APIB_CONTENT = """\
FORMAT: 1A

# Simple API

# GET /message

+ Response 200 (text/plain)

    Hello World!
"""

WSDL_CONTENT = """\
<?xml version="1.0" encoding="UTF-8"?>
<definitions name="HelloService"
  targetNamespace="http://example.com/hello"
  xmlns="http://schemas.xmlsoap.org/wsdl/">
  <service name="HelloService"/>
</definitions>
"""

GRAPHQL_CONTENT = """\
type Query {
  hello: String
}

type Book {
  title: String!
  author: String
}
"""


def _write_temp(content: str, suffix: str) -> str:
    """Write content to a temp file with the given suffix; return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=suffix, delete=False, encoding="utf-8"
    ) as f:
        f.write(content)
        return f.name


# ── Group 1: Transformation layer ────────────────────────────────────


class TestTransformationMultiFormat:
    def test_raml_parsed_as_yaml(self):
        """RAML is valid YAML — title key should be present in parsed spec."""
        tmp = _write_temp(RAML_CONTENT, ".raml")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert "title" in converter.spec
            assert converter.spec["title"] == "Hello API"
            md = converter.convert()
            assert isinstance(md, str) and len(md) > 0
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_apib_falls_back_to_raw(self):
        """API Blueprint is not YAML/JSON — falls back to _raw_content wrapper."""
        tmp = _write_temp(APIB_CONTENT, ".apib")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert "_raw_content" in converter.spec
            assert "FORMAT: 1A" in converter.spec["_raw_content"]
            assert converter.spec.get("info", {}).get("title") == Path(tmp).stem
            md = converter.convert()
            assert isinstance(md, str) and len(md) > 0
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_wsdl_falls_back_to_raw(self):
        """WSDL XML is not YAML/JSON — falls back to _raw_content wrapper."""
        tmp = _write_temp(WSDL_CONTENT, ".wsdl")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert "_raw_content" in converter.spec
            assert "<definitions" in converter.spec["_raw_content"]
            md = converter.convert()
            assert isinstance(md, str) and len(md) > 0
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_graphql_falls_back_to_raw(self):
        """GraphQL SDL is not YAML/JSON — falls back to _raw_content wrapper."""
        tmp = _write_temp(GRAPHQL_CONTENT, ".graphql")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert "_raw_content" in converter.spec
            assert "type Query" in converter.spec["_raw_content"]
            md = converter.convert()
            assert isinstance(md, str) and len(md) > 0
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_gql_alias_same_as_graphql(self):
        """.gql is treated identically to .graphql."""
        tmp = _write_temp(GRAPHQL_CONTENT, ".gql")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert "_raw_content" in converter.spec
        finally:
            Path(tmp).unlink(missing_ok=True)


# ── Group 2: load_openapi_spec() in main.py ──────────────────────────


class TestLoadOpenAPISpec:
    def test_raml_returns_yaml_dict(self):
        tmp = _write_temp(RAML_CONTENT, ".raml")
        try:
            result = load_openapi_spec(tmp, ".raml")
            assert isinstance(result, dict)
            assert result["title"] == "Hello API"
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_apib_returns_raw_fallback(self):
        tmp = _write_temp(APIB_CONTENT, ".apib")
        try:
            result = load_openapi_spec(tmp, ".apib")
            assert isinstance(result, dict)
            assert "_raw_content" in result
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_wsdl_returns_raw_fallback(self):
        tmp = _write_temp(WSDL_CONTENT, ".wsdl")
        try:
            result = load_openapi_spec(tmp, ".wsdl")
            assert isinstance(result, dict)
            assert "_raw_content" in result
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_graphql_returns_raw_fallback(self):
        tmp = _write_temp(GRAPHQL_CONTENT, ".graphql")
        try:
            result = load_openapi_spec(tmp, ".graphql")
            assert isinstance(result, dict)
            assert "_raw_content" in result
        finally:
            Path(tmp).unlink(missing_ok=True)


# ── Group 3: Constants validation ────────────────────────────────────

SCHEMA_PATTERN = re.compile(r"^(yaml|json|raml|apib|wsdl|graphql)$")


class TestConstants:
    def test_every_extension_has_format_mapping(self):
        """Every entry in ALLOWED_EXTENSIONS must have a FORMAT_MAP entry."""
        for ext in ALLOWED_EXTENSIONS:
            assert ext in FORMAT_MAP, f"{ext} missing from FORMAT_MAP"

    def test_format_map_values_match_schema_regex(self):
        """All FORMAT_MAP values must pass the original_format schema regex."""
        for ext, fmt in FORMAT_MAP.items():
            assert SCHEMA_PATTERN.match(fmt), (
                f"FORMAT_MAP['{ext}'] = '{fmt}' does not match schema pattern"
            )


# ── Group 4: Negative case ───────────────────────────────────────────


class TestNegative:
    def test_exe_not_allowed(self):
        assert ".exe" not in ALLOWED_EXTENSIONS

    def test_unknown_extension_not_in_format_map(self):
        assert ".exe" not in FORMAT_MAP
