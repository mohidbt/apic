"""
P2 (medium importance) robustness tests for the OpenAPI-to-Markdown converter.
"""

import json
import yaml
import tempfile
import time
from pathlib import Path
import pytest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from transformation import OpenAPIToMarkdown


def _make_converter(spec: dict, suffix: str = ".json"):
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=suffix, delete=False, encoding="utf-8"
    ) as f:
        if suffix in (".yaml", ".yml"):
            yaml.dump(spec, f)
        else:
            json.dump(spec, f)
        tmp = f.name
    converter = OpenAPIToMarkdown(tmp)
    Path(tmp).unlink(missing_ok=True)
    return converter


class TestP2Robustness:
    def test_spec_with_zero_paths(self):
        """Spec with empty paths returns valid output and empty endpoints/tools."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Empty API", "version": "1.0.0"},
            "paths": {},
        }
        converter = _make_converter(spec)
        out = converter.convert()
        assert isinstance(out, str)
        assert len(out) > 0
        assert "# Empty API" in out or "Empty API" in out

        chunked = converter.convert_chunked()
        assert chunked["endpoints"] == {}

        tools = converter.generate_tool_schemas()
        assert tools == []

    def test_yaml_json_equivalence(self):
        """Same minimal spec as JSON vs YAML produces identical monolithic output."""
        minimal_spec = {
            "openapi": "3.0.0",
            "info": {"title": "Minimal API", "version": "1.0.0"},
            "paths": {
                "/users": {
                    "get": {
                        "operationId": "listUsers",
                        "summary": "List users",
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
            "components": {
                "schemas": {
                    "User": {
                        "type": "object",
                        "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
                    }
                }
            },
        }
        conv_json = _make_converter(minimal_spec, ".json")
        conv_yaml = _make_converter(minimal_spec, ".yaml")
        out_json = conv_json.convert()
        out_yaml = conv_yaml.convert()
        assert out_json == out_yaml

    def test_array_request_body_in_tool_schema(self):
        """POST with array request body schema produces valid tool without crashing."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Array API", "version": "1.0.0"},
            "paths": {
                "/items": {
                    "post": {
                        "operationId": "createItems",
                        "summary": "Create items",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                    }
                                }
                            }
                        },
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        converter = _make_converter(spec)
        tools = converter.generate_tool_schemas()
        assert len(tools) == 1
        tool = tools[0]
        assert tool["name"] == "createItems"
        assert "parameters" in tool
        assert "properties" in tool["parameters"]
        assert tool["parameters"]["properties"] == {} or isinstance(
            tool["parameters"]["properties"], dict
        )

    def test_tags_with_special_characters(self):
        """Tags with spaces and slashes are preserved in chunked output."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Tagged API", "version": "1.0.0"},
            "paths": {
                "/users": {
                    "get": {
                        "operationId": "listUsers",
                        "tags": ["User Management"],
                        "summary": "List users",
                        "responses": {"200": {"description": "OK"}},
                    }
                },
                "/beta/items": {
                    "get": {
                        "operationId": "listBetaItems",
                        "tags": ["v2/beta"],
                        "summary": "List beta items",
                        "responses": {"200": {"description": "OK"}},
                    }
                },
            },
        }
        converter = _make_converter(spec)
        chunked = converter.convert_chunked()
        tags = chunked["tags"]
        assert "User Management" in tags
        assert "v2/beta" in tags
        for tag_key, tag_content in tags.items():
            assert isinstance(tag_content, str)
            assert len(tag_content) > 0
            assert "##" in tag_content or "-" in tag_content

    @pytest.mark.slow
    def test_large_spec_performance(self):
        """Large spec (61K-line OpenAI) converts in under 30 seconds."""
        spec_path = (
            Path(__file__).resolve().parent.parent.parent
            / "examples"
            / "openapi.documented.yml"
        )
        assert spec_path.exists(), f"Large spec not found: {spec_path}"
        converter = OpenAPIToMarkdown(str(spec_path))
        start = time.perf_counter()
        converter.convert()
        elapsed = time.perf_counter() - start
        assert elapsed < 30.0, f"Conversion took {elapsed:.1f}s, expected < 30s"

    def test_description_at_truncation_boundary(self):
        """Exactly 200 chars: no truncation. 201 chars: truncation marker present."""
        base_spec = {
            "openapi": "3.0.0",
            "info": {"title": "Trunc API", "version": "1.0.0"},
            "paths": {
                "/test": {
                    "get": {
                        "operationId": "getTest",
                        "summary": "Get test",
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        desc_200 = "x" * 200
        spec_200 = {
            **base_spec,
            "paths": {
                "/test": {
                    "get": {
                        **base_spec["paths"]["/test"]["get"],
                        "description": desc_200,
                    }
                }
            },
        }
        converter_200 = _make_converter(spec_200)
        out_200 = converter_200.convert()
        assert "... (see full docs)" not in out_200
        assert desc_200 in out_200

        desc_201 = "x" * 201
        spec_201 = {
            **base_spec,
            "paths": {
                "/test": {
                    "get": {
                        **base_spec["paths"]["/test"]["get"],
                        "description": desc_201,
                    }
                }
            },
        }
        converter_201 = _make_converter(spec_201)
        out_201 = converter_201.convert()
        assert "... (see full docs)" in out_201

    def test_idempotent_conversion(self):
        """Calling convert() twice yields identical output."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Idempotent API", "version": "1.0.0"},
            "paths": {
                "/foo": {
                    "get": {
                        "operationId": "getFoo",
                        "summary": "Get foo",
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        converter = _make_converter(spec)
        out1 = converter.convert()
        out2 = converter.convert()
        assert out1 == out2
        assert out1.encode("utf-8") == out2.encode("utf-8")

    def test_unicode_in_descriptions(self):
        """Unicode in descriptions is preserved and does not crash."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Unicode API", "version": "1.0.0"},
            "paths": {
                "/users": {
                    "post": {
                        "operationId": "createUser",
                        "summary": "Create user",
                        "description": "Erstelle einen neuen Benutzer — 用户",
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        converter = _make_converter(spec)
        out = converter.convert()
        assert "Erstelle einen neuen Benutzer — 用户" in out

        chunked = converter.convert_chunked()
        endpoints = chunked["endpoints"]
        assert "createUser" in endpoints
        assert "Erstelle einen neuen Benutzer — 用户" in endpoints["createUser"]
