"""
P1 tests for multi-format API spec support.

Validates that RAML, API Blueprint, WSDL, and GraphQL files are
normalized into OpenAPI-like structure and produce real markdown output.
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
baseUri: /api/v1
/hello:
  displayName: Greeting
  get:
    queryParameters:
      name:
        type: string
        description: Name to greet
    responses:
      200:
        body:
          application/json:
            example: |
              {"message": "hello"}
/goodbye:
  get:
    responses:
      200:
        body:
          application/json:
            type: string
types:
  Greeting:
    type: object
    properties:
      message:
        type: string
"""

APIB_CONTENT = """\
FORMAT: 1A

# Bookstore API

# Group Books

## Books Collection [/books]

### List All Books [GET]

+ Response 200 (application/json)

        [{"id": 1, "title": "Dune"}]

### Create a Book [POST]

+ Response 201 (application/json)

        {"id": 2, "title": "New Book"}

## Single Book [/books/{id}]

### Get Book [GET]

+ Response 200 (application/json)

        {"id": 1, "title": "Dune"}

# Group Authors

## Authors Collection [/authors]

### List Authors [GET]

+ Response 200 (application/json)

        [{"id": 1, "name": "Frank Herbert"}]
"""

WSDL_CONTENT = """\
<?xml version="1.0" encoding="UTF-8"?>
<definitions name="CalculatorService"
  targetNamespace="http://example.com/calc"
  xmlns="http://schemas.xmlsoap.org/wsdl/"
  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
  xmlns:tns="http://example.com/calc"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <message name="AddRequest">
    <part name="a" type="xsd:int"/>
    <part name="b" type="xsd:int"/>
  </message>
  <message name="AddResponse">
    <part name="result" type="xsd:int"/>
  </message>
  <message name="MultiplyRequest">
    <part name="x" type="xsd:float"/>
    <part name="y" type="xsd:float"/>
  </message>
  <message name="MultiplyResponse">
    <part name="product" type="xsd:float"/>
  </message>

  <portType name="Calculator_PortType">
    <operation name="add">
      <input message="tns:AddRequest"/>
      <output message="tns:AddResponse"/>
    </operation>
    <operation name="multiply">
      <input message="tns:MultiplyRequest"/>
      <output message="tns:MultiplyResponse"/>
    </operation>
  </portType>

  <service name="CalculatorService">
    <port name="CalculatorPort" binding="tns:Calculator_Binding">
      <soap:address location="http://example.com/calculator"/>
    </port>
  </service>
</definitions>
"""

GRAPHQL_CONTENT = """\
type Query {
  hello: String
  users: [User!]!
  user(id: ID!): User
}

type Mutation {
  createUser(name: String!, email: String!): User!
  deleteUser(id: ID!): Boolean
}

type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  body: String
  author: User!
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
    def test_raml_normalized_to_openapi(self):
        """RAML is normalized into OpenAPI structure with info, paths, schemas."""
        tmp = _write_temp(RAML_CONTENT, ".raml")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert converter.spec.get("info", {}).get("title") == "Hello API"
            paths = converter.spec.get("paths", {})
            assert "/hello" in paths
            assert "/goodbye" in paths
            assert "Greeting" in converter.spec.get("components", {}).get("schemas", {})
            md = converter.convert()
            assert len(md) > 200
            assert "Hello API" in md
            assert "ENDPOINT:" in md
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_apib_normalized_to_openapi(self):
        """API Blueprint is parsed into OpenAPI structure with paths and tags."""
        tmp = _write_temp(APIB_CONTENT, ".apib")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert converter.spec.get("info", {}).get("title") == "Bookstore API"
            paths = converter.spec.get("paths", {})
            assert "/books" in paths
            assert "/authors" in paths
            md = converter.convert()
            assert len(md) > 200
            assert "ENDPOINT:" in md
            assert "Bookstore API" in md
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_wsdl_normalized_to_openapi(self):
        """WSDL XML is parsed into OpenAPI structure with operations as paths."""
        tmp = _write_temp(WSDL_CONTENT, ".wsdl")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert converter.spec.get("info", {}).get("title") == "CalculatorService"
            paths = converter.spec.get("paths", {})
            assert "/add" in paths
            assert "/multiply" in paths
            schemas = converter.spec.get("components", {}).get("schemas", {})
            assert "AddRequest" in schemas
            assert "MultiplyResponse" in schemas
            servers = converter.spec.get("servers", [])
            assert any("example.com/calculator" in s.get("url", "") for s in servers)
            md = converter.convert()
            assert len(md) > 200
            assert "ENDPOINT:" in md
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_graphql_normalized_to_openapi(self):
        """GraphQL SDL is parsed into OpenAPI with queries as GET, mutations as POST, types as schemas."""
        tmp = _write_temp(GRAPHQL_CONTENT, ".graphql")
        try:
            converter = OpenAPIToMarkdown(tmp)
            paths = converter.spec.get("paths", {})
            assert "/hello" in paths
            assert "/users" in paths
            assert "/user" in paths
            assert "get" in paths["/hello"]
            assert "/createUser" in paths
            assert "post" in paths["/createUser"]
            schemas = converter.spec.get("components", {}).get("schemas", {})
            assert "User" in schemas
            assert "Post" in schemas
            assert "id" in schemas["User"]["properties"]
            assert "name" in schemas["User"].get("required", [])
            md = converter.convert()
            assert len(md) > 200
            assert "ENDPOINT:" in md
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_gql_alias_same_as_graphql(self):
        """.gql produces the same normalized structure as .graphql."""
        tmp = _write_temp(GRAPHQL_CONTENT, ".gql")
        try:
            converter = OpenAPIToMarkdown(tmp)
            paths = converter.spec.get("paths", {})
            assert "/hello" in paths
            assert "User" in converter.spec.get("components", {}).get("schemas", {})
        finally:
            Path(tmp).unlink(missing_ok=True)


# ── Group 2: load_openapi_spec() in main.py ──────────────────────────


class TestLoadOpenAPISpec:
    def test_raml_returns_normalized_openapi(self):
        tmp = _write_temp(RAML_CONTENT, ".raml")
        try:
            result = load_openapi_spec(tmp, ".raml")
            assert isinstance(result, dict)
            assert result.get("info", {}).get("title") == "Hello API"
            assert "/hello" in result.get("paths", {})
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_apib_returns_normalized_openapi(self):
        tmp = _write_temp(APIB_CONTENT, ".apib")
        try:
            result = load_openapi_spec(tmp, ".apib")
            assert isinstance(result, dict)
            assert result.get("info", {}).get("title") == "Bookstore API"
            assert "/books" in result.get("paths", {})
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_wsdl_returns_normalized_openapi(self):
        tmp = _write_temp(WSDL_CONTENT, ".wsdl")
        try:
            result = load_openapi_spec(tmp, ".wsdl")
            assert isinstance(result, dict)
            assert result.get("info", {}).get("title") == "CalculatorService"
            assert "/add" in result.get("paths", {})
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_graphql_returns_normalized_openapi(self):
        tmp = _write_temp(GRAPHQL_CONTENT, ".graphql")
        try:
            result = load_openapi_spec(tmp, ".graphql")
            assert isinstance(result, dict)
            assert "/hello" in result.get("paths", {})
            assert "User" in result.get("components", {}).get("schemas", {})
        finally:
            Path(tmp).unlink(missing_ok=True)


# ── Group 2b: Real RAML example file ─────────────────────────────────


class TestRealRAML:
    RAML_PATH = Path(__file__).resolve().parent.parent.parent / "examples" / "hapi_affiliate (1).raml"

    @pytest.mark.skipif(
        not (Path(__file__).resolve().parent.parent.parent / "examples" / "hapi_affiliate (1).raml").exists(),
        reason="Example RAML file not present",
    )
    def test_real_raml_produces_endpoints(self):
        """The real Hotels Search RAML file should produce paths, schemas, and substantial markdown."""
        converter = OpenAPIToMarkdown(str(self.RAML_PATH))
        assert converter.spec["info"]["title"] == "Hotels Search API"
        assert converter.spec["info"]["version"] == "v3"
        assert len(converter.spec.get("paths", {})) >= 3
        assert len(converter.spec.get("components", {}).get("schemas", {})) > 10

        md = converter.convert()
        assert len(md) > 5000
        assert "Hotels Search API" in md
        assert "ENDPOINT:" in md


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


# ── Group 4: Negative cases ──────────────────────────────────────────


class TestNegative:
    def test_exe_not_allowed(self):
        assert ".exe" not in ALLOWED_EXTENSIONS

    def test_unknown_extension_not_in_format_map(self):
        assert ".exe" not in FORMAT_MAP

    def test_malformed_wsdl_does_not_crash(self):
        """Invalid XML should not crash, should return fallback with _raw_content."""
        tmp = _write_temp("this is not xml at all", ".wsdl")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert "_raw_content" in converter.spec
            md = converter.convert()
            assert isinstance(md, str) and len(md) > 0
        finally:
            Path(tmp).unlink(missing_ok=True)

    def test_empty_graphql_produces_no_paths(self):
        """Empty .graphql file produces valid spec with no paths."""
        tmp = _write_temp("", ".graphql")
        try:
            converter = OpenAPIToMarkdown(tmp)
            assert converter.spec.get("paths", {}) == {}
            md = converter.convert()
            assert isinstance(md, str)
        finally:
            Path(tmp).unlink(missing_ok=True)
