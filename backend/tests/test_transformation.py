"""
Evaluation harness for the OpenAPI-to-Markdown transformation pipeline.

Validates that the generated output enables correct API call construction by
checking structural correctness, schema validity, and completeness — without
requiring an LLM in the loop (deterministic, CI-friendly).

Run:  pytest backend/tests/test_eval_harness.py -v
"""

import json
import re
import tempfile
from pathlib import Path

import pytest

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from transformation import OpenAPIToMarkdown

# ── Fixtures ──────────────────────────────────────────────────────────

MINIMAL_SPEC = {
    "openapi": "3.0.0",
    "info": {"title": "Pet Store", "version": "1.2.0"},
    "servers": [{"url": "https://api.petstore.io/v1"}],
    "components": {
        "securitySchemes": {
            "bearerAuth": {"type": "http", "scheme": "bearer"},
        },
        "schemas": {
            "Pet": {
                "type": "object",
                "required": ["name"],
                "properties": {
                    "id": {"type": "integer", "format": "int64"},
                    "name": {"type": "string"},
                    "tag": {"type": "string"},
                },
            },
            "Error": {
                "type": "object",
                "properties": {
                    "code": {"type": "integer"},
                    "message": {"type": "string"},
                },
            },
        },
    },
    "security": [{"bearerAuth": []}],
    "paths": {
        "/pets": {
            "get": {
                "operationId": "listPets",
                "summary": "List all pets",
                "tags": ["pets"],
                "parameters": [
                    {
                        "name": "limit",
                        "in": "query",
                        "required": False,
                        "schema": {"type": "integer", "format": "int32"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "A list of pets",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/Pet"},
                                }
                            }
                        },
                    },
                },
            },
            "post": {
                "operationId": "createPet",
                "summary": "Create a pet",
                "tags": ["pets"],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Pet"},
                        }
                    },
                },
                "responses": {
                    "201": {"description": "Pet created"},
                    "400": {
                        "description": "Bad request",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"},
                            }
                        },
                    },
                },
            },
        },
        "/pets/{petId}": {
            "get": {
                "operationId": "showPetById",
                "summary": "Info for a specific pet",
                "tags": ["pets"],
                "parameters": [
                    {
                        "name": "petId",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "string"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Expected response to a valid request",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Pet"},
                            }
                        },
                    },
                },
            },
        },
    },
}


@pytest.fixture
def converter():
    """Create a converter from the minimal spec."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as f:
        json.dump(MINIMAL_SPEC, f)
        tmp = f.name
    try:
        yield OpenAPIToMarkdown(tmp)
    finally:
        Path(tmp).unlink(missing_ok=True)


# ── 1. Monolithic output structural tests ─────────────────────────────


class TestMonolithicOutput:
    def test_header_contains_title_and_version(self, converter):
        md = converter.convert()
        assert "# Pet Store" in md
        assert "1.2.0" in md

    def test_base_url_in_header(self, converter):
        md = converter.convert()
        assert "https://api.petstore.io/v1" in md

    def test_auth_in_header(self, converter):
        md = converter.convert()
        assert "BEARER" in md.upper()

    def test_every_endpoint_has_separator(self, converter):
        md = converter.convert()
        blocks = md.split("=" * 80)
        endpoint_blocks = [
            b for b in blocks if "ENDPOINT:" in b
        ]
        assert len(endpoint_blocks) == 3  # listPets, createPet, showPetById

    def test_operation_id_in_blocks(self, converter):
        md = converter.convert()
        assert "OPERATION_ID: listPets" in md
        assert "OPERATION_ID: createPet" in md
        assert "OPERATION_ID: showPetById" in md

    def test_base_url_in_every_block(self, converter):
        md = converter.convert()
        blocks = md.split("=" * 80)
        endpoint_blocks = [b for b in blocks if "ENDPOINT:" in b]
        for block in endpoint_blocks:
            assert "BASE_URL: https://api.petstore.io/v1" in block

    def test_curl_examples_present(self, converter):
        md = converter.convert()
        assert md.count("curl -X") >= 3

    def test_curl_uses_correct_base_url(self, converter):
        md = converter.convert()
        blocks = md.split("=" * 80)
        endpoint_blocks = [b for b in blocks if "EXAMPLE (curl)" in b]
        for block in endpoint_blocks:
            curl_section = block.split("EXAMPLE (curl)")[1]
            assert "api.petstore.io" in curl_section

    def test_path_param_in_curl(self, converter):
        md = converter.convert()
        blocks = md.split("=" * 80)
        show_pet_block = [b for b in blocks if "showPetById" in b]
        assert len(show_pet_block) == 1
        curl_section = show_pet_block[0].split("EXAMPLE (curl)")[1]
        assert "{petId}" not in curl_section, \
            "Path param should be replaced with example value in curl"

    def test_request_body_schema_surfaced(self, converter):
        md = converter.convert()
        blocks = md.split("=" * 80)
        create_block = [b for b in blocks if "createPet" in b]
        assert len(create_block) == 1
        assert "name" in create_block[0]
        assert "required" in create_block[0].lower()

    def test_toc_lists_all_endpoints(self, converter):
        md = converter.convert()
        assert "`/pets`" in md
        assert "`/pets/{petId}`" in md

    def test_components_appendix(self, converter):
        md = converter.convert()
        assert "COMPONENTS APPENDIX" in md
        assert "### Pet" in md
        assert "### Error" in md


# ── 2. Chunked output tests ──────────────────────────────────────────


class TestChunkedOutput:
    def test_keys(self, converter):
        chunked = converter.convert_chunked()
        assert set(chunked.keys()) == {"manifest", "tags", "endpoints", "schemas"}

    def test_manifest_is_small(self, converter):
        chunked = converter.convert_chunked()
        assert len(chunked["manifest"]) < 2000

    def test_manifest_contains_base_url(self, converter):
        chunked = converter.convert_chunked()
        assert "https://api.petstore.io/v1" in chunked["manifest"]

    def test_tags_match_spec(self, converter):
        chunked = converter.convert_chunked()
        assert "pets" in chunked["tags"]

    def test_endpoints_keyed_by_operation_id(self, converter):
        chunked = converter.convert_chunked()
        assert "listPets" in chunked["endpoints"]
        assert "createPet" in chunked["endpoints"]
        assert "showPetById" in chunked["endpoints"]

    def test_each_endpoint_self_contained(self, converter):
        chunked = converter.convert_chunked()
        for op_id, block in chunked["endpoints"].items():
            assert "ENDPOINT:" in block, f"{op_id} missing ENDPOINT header"
            assert "BASE_URL:" in block, f"{op_id} missing BASE_URL"
            assert "AUTH:" in block, f"{op_id} missing AUTH"
            assert "curl" in block.lower(), f"{op_id} missing curl example"

    def test_schemas_present(self, converter):
        chunked = converter.convert_chunked()
        assert "Pet" in chunked["schemas"]
        assert "Error" in chunked["schemas"]

    def test_schema_content(self, converter):
        chunked = converter.convert_chunked()
        pet_schema = chunked["schemas"]["Pet"]
        assert "name" in pet_schema
        assert "required" in pet_schema.lower()


# ── 3. Tool schema tests ─────────────────────────────────────────────


class TestToolSchemas:
    def test_tool_count(self, converter):
        tools = converter.generate_tool_schemas()
        assert len(tools) == 3

    def test_tool_names_are_operation_ids(self, converter):
        tools = converter.generate_tool_schemas()
        names = {t["name"] for t in tools}
        assert names == {"listPets", "createPet", "showPetById"}

    def test_tool_has_required_fields(self, converter):
        tools = converter.generate_tool_schemas()
        for tool in tools:
            assert "name" in tool
            assert "description" in tool
            assert "parameters" in tool
            assert tool["parameters"]["type"] == "object"
            assert "properties" in tool["parameters"]

    def test_path_param_required(self, converter):
        tools = converter.generate_tool_schemas()
        show_pet = next(t for t in tools if t["name"] == "showPetById")
        assert "petId" in show_pet["parameters"]["properties"]
        assert "petId" in show_pet["parameters"].get("required", [])

    def test_query_param_optional(self, converter):
        tools = converter.generate_tool_schemas()
        list_pets = next(t for t in tools if t["name"] == "listPets")
        assert "limit" in list_pets["parameters"]["properties"]
        assert "limit" not in list_pets["parameters"].get("required", [])

    def test_request_body_fields_in_tool(self, converter):
        tools = converter.generate_tool_schemas()
        create_pet = next(t for t in tools if t["name"] == "createPet")
        props = create_pet["parameters"]["properties"]
        assert "name" in props
        assert props["name"]["type"] == "string"
        assert "name" in create_pet["parameters"].get("required", [])

    def test_tool_schemas_valid_json_schema(self, converter):
        """Each tool's parameters block must be a valid JSON Schema object."""
        tools = converter.generate_tool_schemas()
        for tool in tools:
            params = tool["parameters"]
            assert params["type"] == "object"
            for prop_name, prop_def in params["properties"].items():
                assert "type" in prop_def, \
                    f"Property {prop_name} in {tool['name']} missing 'type'"


# ── 4. Cross-format consistency tests ─────────────────────────────────


class TestCrossFormatConsistency:
    """Ensure monolithic, chunked, and tool outputs agree with each other."""

    def test_endpoint_count_matches(self, converter):
        md = converter.convert()
        chunked = converter.convert_chunked()
        tools = converter.generate_tool_schemas()

        md_count = md.count("ENDPOINT: [")
        assert md_count == len(chunked["endpoints"])
        assert md_count == len(tools)

    def test_operation_ids_consistent(self, converter):
        chunked = converter.convert_chunked()
        tools = converter.generate_tool_schemas()
        chunked_ids = set(chunked["endpoints"].keys())
        tool_ids = {t["name"] for t in tools}
        assert chunked_ids == tool_ids

    def test_schema_names_consistent(self, converter):
        chunked = converter.convert_chunked()
        md = converter.convert()
        for schema_name in chunked["schemas"]:
            assert schema_name in md, \
                f"Schema '{schema_name}' in chunked output but not in monolithic"


# ── 5. P0 Edge case tests ─────────────────────────────────────────────


class TestP0EdgeCases:
    """Critical edge cases: no operationId, circular refs, deep refs, schema deref, param collision."""

    @staticmethod
    def _make_converter(spec: dict):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(spec, f)
            tmp = f.name
        converter = OpenAPIToMarkdown(tmp)
        Path(tmp).unlink(missing_ok=True)
        return converter

    def test_no_operation_id_fallback_chunked(self):
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0"},
            "paths": {
                "/pets": {
                    "get": {"summary": "List pets", "responses": {"200": {"description": "OK"}}},
                },
            },
        }
        conv = self._make_converter(spec)
        chunked = conv.convert_chunked()
        assert "GET_pets" in chunked["endpoints"]
        md = conv.convert()
        assert "OPERATION_ID:" not in md

    def test_no_operation_id_fallback_consistent(self):
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0"},
            "paths": {
                "/pets": {
                    "get": {"summary": "List pets", "responses": {"200": {"description": "OK"}}},
                },
            },
        }
        conv = self._make_converter(spec)
        chunked = conv.convert_chunked()
        tools = conv.generate_tool_schemas()
        chunked_keys = set(chunked["endpoints"].keys())
        tool_names = {t["name"] for t in tools}
        assert chunked_keys == tool_names

    def test_circular_ref_terminates(self):
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0"},
            "paths": {"/": {"get": {"responses": {"200": {"description": "OK"}}}}},
            "components": {
                "schemas": {
                    "A": {"type": "object", "properties": {"b": {"$ref": "#/components/schemas/B"}}},
                    "B": {"type": "object", "properties": {"a": {"$ref": "#/components/schemas/A"}}},
                }
            },
        }
        conv = self._make_converter(spec)
        md = conv.convert()
        assert len(md) > 0
        chunked = conv.convert_chunked()
        assert "manifest" in chunked
        assert "schemas" in chunked

    def test_deep_ref_chain(self):
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0"},
            "paths": {"/": {"get": {"responses": {"200": {"description": "OK"}}}}},
            "components": {
                "schemas": {
                    "A": {"type": "object", "properties": {"x": {"$ref": "#/components/schemas/B"}}},
                    "B": {"type": "object", "properties": {"x": {"$ref": "#/components/schemas/C"}}},
                    "C": {"type": "object", "properties": {"x": {"$ref": "#/components/schemas/D"}}},
                    "D": {"type": "object", "properties": {"name": {"type": "string"}}},
                }
            },
        }
        conv = self._make_converter(spec)
        md = conv.convert()
        assert len(md) > 0
        assert "A" in md or "B" in md or "C" in md

    def test_schema_deref_in_chunked_output(self):
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0"},
            "paths": {"/": {"get": {"responses": {"200": {"description": "OK"}}}}},
            "components": {
                "schemas": {
                    "Order": {
                        "type": "object",
                        "properties": {"customer": {"$ref": "#/components/schemas/Customer"}},
                    },
                    "Customer": {
                        "type": "object",
                        "properties": {"name": {"type": "string"}, "email": {"type": "string"}},
                    },
                }
            },
        }
        conv = self._make_converter(spec)
        chunked = conv.convert_chunked()
        order_schema = chunked["schemas"]["Order"]
        assert "$ref" not in order_schema, "Order schema must not contain raw $ref"
        customer_schema = chunked["schemas"]["Customer"]
        assert "name" in customer_schema and "email" in customer_schema, (
            "Referenced Customer schema must have resolved field names"
        )

    def test_param_name_collision_path_wins(self):
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0"},
            "paths": {
                "/items/{id}": {
                    "post": {
                        "parameters": [
                            {
                                "name": "id",
                                "in": "path",
                                "required": True,
                                "schema": {"type": "string"},
                            }
                        ],
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {"id": {"type": "integer"}},
                                        "required": ["id"],
                                    }
                                }
                            }
                        },
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        conv = self._make_converter(spec)
        tools = conv.generate_tool_schemas()
        assert len(tools) == 1
        post_tool = tools[0]
        props = post_tool["parameters"]["properties"]
        required = post_tool["parameters"].get("required", [])
        assert "id" in props
        assert "id" in required
        assert props["id"].get("type") == "string"


# ── 6. Real spec smoke tests ─────────────────────────────────────────


EXAMPLE_SPECS = list(Path(__file__).resolve().parent.parent.parent.glob("examples/*.json")) + \
                list(Path(__file__).resolve().parent.parent.parent.glob("examples/*.yaml")) + \
                list(Path(__file__).resolve().parent.parent.parent.glob("examples/*.yml"))


@pytest.mark.parametrize("spec_path", EXAMPLE_SPECS, ids=lambda p: p.name)
class TestRealSpecs:
    """Run basic sanity checks against every example spec in the repo."""

    def test_convert_succeeds(self, spec_path):
        converter = OpenAPIToMarkdown(str(spec_path))
        md = converter.convert()
        assert len(md) > 100

    def test_chunked_succeeds(self, spec_path):
        converter = OpenAPIToMarkdown(str(spec_path))
        chunked = converter.convert_chunked()
        assert len(chunked["endpoints"]) > 0

    def test_tool_schemas_succeed(self, spec_path):
        converter = OpenAPIToMarkdown(str(spec_path))
        tools = converter.generate_tool_schemas()
        assert len(tools) > 0
        for tool in tools:
            assert "name" in tool
            assert "parameters" in tool

    def test_no_unresolved_refs_in_output(self, spec_path):
        converter = OpenAPIToMarkdown(str(spec_path))
        md = converter.convert()
        assert "$ref" not in md, "Unresolved $ref found in markdown output"
