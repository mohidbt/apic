"""
P1 (high importance) behavioral tests for OpenAPIToMarkdown.

Tests edge cases: allOf, $ref in parameters, empty endpoints,
security overrides, multiple servers, required ref parameters.
"""

import json
import tempfile
from pathlib import Path
import pytest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from transformation import OpenAPIToMarkdown


class TestP1Behavioral:
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

    def test_allof_in_request_body_tool_schema(self):
        """allOf in requestBody without top-level properties produces tool with path/query only."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/items": {
                    "post": {
                        "operationId": "createItem",
                        "summary": "Create item",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "allOf": [
                                            {"$ref": "#/components/schemas/Base"},
                                            {
                                                "type": "object",
                                                "properties": {"extra": {"type": "string"}},
                                            },
                                        ]
                                    }
                                }
                            }
                        },
                        "responses": {"201": {"description": "Created"}},
                    }
                }
            },
            "components": {
                "schemas": {
                    "Base": {
                        "type": "object",
                        "properties": {"id": {"type": "string"}},
                    }
                }
            },
        }
        converter = self._make_converter(spec)
        tools = converter.generate_tool_schemas()
        assert len(tools) == 1
        tool = tools[0]
        assert tool["name"] == "createItem"
        assert "parameters" in tool
        assert "properties" in tool["parameters"]
        # allOf without top-level properties: body_schema.get('properties') is None
        # so tool has path/query params only (none here) -> empty properties
        assert tool["parameters"]["properties"] == {}

    def test_ref_in_parameters_array(self):
        """$ref in parameters array is resolved correctly."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/items": {
                    "get": {
                        "operationId": "listItems",
                        "summary": "List items",
                        "parameters": [{"$ref": "#/components/parameters/LimitParam"}],
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
            "components": {
                "parameters": {
                    "LimitParam": {
                        "name": "limit",
                        "in": "query",
                        "schema": {"type": "integer"},
                        "description": "Max items",
                    }
                }
            },
        }
        converter = self._make_converter(spec)
        tools = converter.generate_tool_schemas()
        assert len(tools) == 1
        tool = tools[0]
        assert "limit" in tool["parameters"]["properties"]
        assert tool["parameters"]["properties"]["limit"]["type"] == "integer"
        assert tool["parameters"]["properties"]["limit"]["description"] == "Max items"

    def test_empty_get_endpoint_tool_schema(self):
        """GET /health with no params/body produces valid tool with empty properties."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/health": {
                    "get": {
                        "operationId": "healthCheck",
                        "summary": "Health check",
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        converter = self._make_converter(spec)
        tools = converter.generate_tool_schemas()
        assert len(tools) == 1
        tool = tools[0]
        assert tool["name"] == "healthCheck"
        assert tool["parameters"]["properties"] == {}
        assert "required" not in tool["parameters"]

    def test_operation_security_override_none(self):
        """Endpoint with security: [] shows AUTH: None; others show BEARER."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0"},
            "components": {
                "securitySchemes": {
                    "bearerAuth": {"type": "http", "scheme": "bearer"},
                }
            },
            "security": [{"bearerAuth": []}],
            "paths": {
                "/public": {
                    "get": {
                        "operationId": "publicEndpoint",
                        "summary": "Public",
                        "security": [],
                        "responses": {"200": {"description": "OK"}},
                    }
                },
                "/private": {
                    "get": {
                        "operationId": "privateEndpoint",
                        "summary": "Private",
                        "responses": {"200": {"description": "OK"}},
                    }
                },
            },
        }
        converter = self._make_converter(spec)
        md = converter.convert()
        blocks = md.split("=" * 80)
        public_block = [b for b in blocks if "publicEndpoint" in b][0]
        private_block = [b for b in blocks if "privateEndpoint" in b][0]
        assert "AUTH: None" in public_block
        assert "BEARER" in private_block.upper()

    def test_multiple_servers_uses_first(self):
        """First server URL used in endpoint blocks; backup only in header."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0"},
            "servers": [
                {"url": "https://primary.api.com"},
                {"url": "https://backup.api.com"},
            ],
            "paths": {
                "/items": {
                    "get": {
                        "operationId": "listItems",
                        "summary": "List",
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        converter = self._make_converter(spec)
        md = converter.convert()
        blocks = md.split("=" * 80)
        endpoint_blocks = [b for b in blocks if "ENDPOINT:" in b]
        assert len(endpoint_blocks) >= 1
        for block in endpoint_blocks:
            assert "BASE_URL: https://primary.api.com" in block
            assert "https://primary.api.com" in block
            assert "https://backup.api.com" not in block
        assert "https://backup.api.com" in md  # in header listing

    def test_ref_parameter_in_tool_schema_required(self):
        """Shared parameter with required: true appears in tool's required list."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/items": {
                    "get": {
                        "operationId": "listItems",
                        "summary": "List",
                        "parameters": [{"$ref": "#/components/parameters/RequiredId"}],
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
            "components": {
                "parameters": {
                    "RequiredId": {
                        "name": "id",
                        "in": "query",
                        "required": True,
                        "schema": {"type": "string"},
                    }
                }
            },
        }
        converter = self._make_converter(spec)
        tools = converter.generate_tool_schemas()
        assert len(tools) == 1
        tool = tools[0]
        assert "id" in tool["parameters"]["properties"]
        assert "required" in tool["parameters"]
        assert "id" in tool["parameters"]["required"]
