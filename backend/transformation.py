#!/usr/bin/env python3
"""
OpenAPI to LLM-Ready Markdown Converter

Converts API specifications (OpenAPI YAML/JSON, RAML, WSDL, GraphQL, API Blueprint) into structured, LLM-friendly markdown format.
Features:
- Dereferences $ref schemas
- Surfaces authentication and base URLs
- Generates runnable curl examples
- Uses strict Gitingest-style separators
- Groups by tag, alphabetically ordered
- Keeps chunks under 2-4k tokens per endpoint
"""

import json
import yaml
import sys
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict
from copy import deepcopy


_RAML_TYPE_MAP = {
    "string": "string", "number": "number", "integer": "integer",
    "boolean": "boolean", "date-only": "string", "time-only": "string",
    "datetime-only": "string", "datetime": "string", "file": "string",
    "nil": "string", "any": "string", "object": "object", "array": "array",
}


def _raml_type_to_schema(raml_type: Any) -> Dict[str, Any]:
    """Best-effort conversion of a RAML type definition to an OpenAPI schema."""
    if isinstance(raml_type, str):
        base = raml_type.rstrip("[]")
        is_array = raml_type.endswith("[]")
        mapped = _RAML_TYPE_MAP.get(base, "string")
        if is_array:
            return {"type": "array", "items": {"type": mapped}}
        if base in _RAML_TYPE_MAP:
            schema: Dict[str, Any] = {"type": mapped}
            if base == "date-only":
                schema["format"] = "date"
            return schema
        return {"type": "string", "description": f"(RAML type: {raml_type})"}

    if isinstance(raml_type, dict):
        schema = {}
        t = raml_type.get("type", "object")
        if isinstance(t, str) and t.endswith("[]"):
            schema["type"] = "array"
            schema["items"] = _raml_type_to_schema(t.rstrip("[]"))
        else:
            schema["type"] = _RAML_TYPE_MAP.get(t, "string") if isinstance(t, str) else "string"
        if "description" in raml_type:
            schema["description"] = raml_type["description"]
        if "enum" in raml_type:
            schema["enum"] = raml_type["enum"]
        if "properties" in raml_type and isinstance(raml_type["properties"], dict):
            schema["type"] = "object"
            props = {}
            for pname, pdef in raml_type["properties"].items():
                clean = pname.rstrip("?")
                props[clean] = _raml_type_to_schema(pdef) if isinstance(pdef, dict) else _raml_type_to_schema(pdef)
            schema["properties"] = props
        return schema

    return {"type": "string"}


def _raml_resource_to_paths(key: str, resource: dict, default_media: str) -> Dict[str, Dict]:
    """Flatten a RAML resource (possibly with nested sub-resources) into OpenAPI paths."""
    paths: Dict[str, Dict] = {}
    methods = ("get", "post", "put", "patch", "delete", "head", "options")
    path_item: Dict[str, Any] = {}

    display_name = resource.get("displayName", "")
    resource_desc = resource.get("description", "")

    for method in methods:
        if method not in resource:
            continue
        method_def = resource[method] if isinstance(resource[method], dict) else {}
        operation: Dict[str, Any] = {}

        if display_name:
            operation["summary"] = display_name
        if resource_desc:
            operation["description"] = resource_desc
        elif method_def.get("description"):
            operation["description"] = method_def["description"]

        operation["operationId"] = f"{method}_{key.replace('/', '_').strip('_')}"
        operation["tags"] = [display_name] if display_name else ["Default"]

        params = []
        for pname, pdef in (method_def.get("queryParameters") or {}).items():
            clean_name = pname.rstrip("?")
            required = not pname.endswith("?")
            param: Dict[str, Any] = {"name": clean_name, "in": "query", "required": required}
            if isinstance(pdef, dict):
                if "description" in pdef:
                    param["description"] = str(pdef["description"]).strip()
                param["schema"] = _raml_type_to_schema(pdef)
            else:
                param["schema"] = {"type": "string"}
            params.append(param)
        if params:
            operation["parameters"] = params

        raw_responses = method_def.get("responses", {})
        if raw_responses and isinstance(raw_responses, dict):
            oapi_responses: Dict[str, Any] = {}
            for status, resp_def in raw_responses.items():
                resp: Dict[str, Any] = {"description": ""}
                if isinstance(resp_def, dict):
                    body = resp_def.get("body", {})
                    if body and isinstance(body, dict):
                        content = {}
                        for media, media_def in body.items():
                            content[media] = {"schema": _raml_type_to_schema(media_def) if isinstance(media_def, dict) else {"type": "string"}}
                        resp["content"] = content
                oapi_responses[str(status)] = resp
            operation["responses"] = oapi_responses
        else:
            operation["responses"] = {"200": {"description": "OK"}}

        path_item[method] = operation

    if path_item:
        paths[key] = path_item

    for sub_key, sub_val in resource.items():
        if sub_key.startswith("/") and isinstance(sub_val, dict):
            sub_paths = _raml_resource_to_paths(key + sub_key, sub_val, default_media)
            paths.update(sub_paths)

    return paths


def _safe_load_raml(content: str) -> Dict[str, Any]:
    """YAML-load RAML content, tolerating !include and other custom tags."""
    class _RAMLLoader(yaml.SafeLoader):
        pass
    _RAMLLoader.add_multi_constructor("!", lambda loader, suffix, node: None)
    try:
        return yaml.load(content, Loader=_RAMLLoader) or {}
    except yaml.YAMLError:
        return {}


def normalize_raml(raml: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a RAML-parsed dict into an OpenAPI-like structure."""
    spec: Dict[str, Any] = {"openapi": "3.0.0"}

    info: Dict[str, Any] = {
        "title": raml.get("title", "API"),
        "version": str(raml.get("version", "1.0.0")),
    }
    if "description" in raml:
        info["description"] = raml["description"]

    docs = raml.get("documentation")
    if isinstance(docs, list):
        parts = []
        for doc in docs:
            if isinstance(doc, dict):
                parts.append(f"## {doc.get('title', '')}\n{doc.get('content', '')}")
        if parts:
            extra = "\n\n".join(parts)
            info["description"] = f"{info.get('description', '')}\n\n{extra}".strip()

    spec["info"] = info

    base_uri = raml.get("baseUri")
    if base_uri:
        url = base_uri["value"] if isinstance(base_uri, dict) and "value" in base_uri else str(base_uri)
        spec["servers"] = [{"url": url}]

    default_media = raml.get("mediaType", "application/json")
    paths: Dict[str, Dict] = {}
    for key, val in raml.items():
        if key.startswith("/") and isinstance(val, dict):
            paths.update(_raml_resource_to_paths(key, val, default_media))
    spec["paths"] = paths

    raml_types = raml.get("types", {})
    if isinstance(raml_types, dict) and raml_types:
        schemas = {}
        for tname, tdef in raml_types.items():
            schemas[tname] = _raml_type_to_schema(tdef)
        spec["components"] = {"schemas": schemas}

    return spec


# ── API Blueprint normalizer ─────────────────────────────────────────

_APIB_RESOURCE_RE = re.compile(r"^##\s+(.+?)\s*\[(/[^\]]*)\]\s*$")
_APIB_ACTION_RE = re.compile(r"^###\s+(.+?)\s*\[(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\]\s*$")
_APIB_RESPONSE_RE = re.compile(r"^\+\s+Response\s+(\d{3})\s*(?:\(([^)]*)\))?\s*$")
_APIB_GROUP_RE = re.compile(r"^#\s+Group\s+(.+)$")
_APIB_TITLE_RE = re.compile(r"^#\s+(?!Group\s)(.+)$")


def normalize_apib(content: str) -> Dict[str, Any]:
    """Convert API Blueprint text into an OpenAPI-like structure."""
    spec: Dict[str, Any] = {"openapi": "3.0.0"}
    info: Dict[str, Any] = {"title": "API", "version": "1.0.0"}
    paths: Dict[str, Dict] = {}

    current_tag = "Default"
    current_path: Optional[str] = None
    current_resource_name = ""
    current_method: Optional[str] = None
    current_action_name = ""
    current_responses: Dict[str, Any] = {}

    def _flush_action():
        nonlocal current_method, current_responses
        if current_path and current_method:
            path_item = paths.setdefault(current_path, {})
            op_id = f"{current_method.lower()}_{current_path.replace('/', '_').strip('_')}"
            operation: Dict[str, Any] = {
                "operationId": op_id,
                "tags": [current_tag],
                "responses": current_responses or {"200": {"description": "OK"}},
            }
            if current_action_name:
                operation["summary"] = current_action_name
            if current_resource_name:
                operation["description"] = current_resource_name
            path_item[current_method.lower()] = operation
        current_method = None
        current_responses = {}

    for line in content.splitlines():
        stripped = line.strip()

        title_m = _APIB_TITLE_RE.match(stripped)
        if title_m and info["title"] == "API":
            info["title"] = title_m.group(1).strip()
            continue

        group_m = _APIB_GROUP_RE.match(stripped)
        if group_m:
            _flush_action()
            current_tag = group_m.group(1).strip()
            continue

        resource_m = _APIB_RESOURCE_RE.match(stripped)
        if resource_m:
            _flush_action()
            current_resource_name = resource_m.group(1).strip()
            current_path = resource_m.group(2).strip()
            continue

        action_m = _APIB_ACTION_RE.match(stripped)
        if action_m:
            _flush_action()
            current_action_name = action_m.group(1).strip()
            current_method = action_m.group(2).strip()
            continue

        resp_m = _APIB_RESPONSE_RE.match(stripped)
        if resp_m:
            status = resp_m.group(1)
            ct = resp_m.group(2) or "application/json"
            current_responses[status] = {
                "description": "",
                "content": {ct: {"schema": {"type": "object"}}},
            }
            continue

        # Standalone method line: `# GET /path` (simplest APIB form)
        standalone = re.match(r"^#\s+(GET|POST|PUT|PATCH|DELETE)\s+(/\S+)\s*$", stripped)
        if standalone:
            _flush_action()
            current_method = standalone.group(1)
            current_path = standalone.group(2)
            current_action_name = f"{current_method} {current_path}"
            continue

    _flush_action()

    spec["info"] = info
    spec["paths"] = paths
    return spec


# ── WSDL normalizer ──────────────────────────────────────────────────

def normalize_wsdl(content: str) -> Dict[str, Any]:
    """Convert WSDL XML into an OpenAPI-like structure."""
    spec: Dict[str, Any] = {"openapi": "3.0.0"}
    info: Dict[str, Any] = {"version": "1.0.0"}
    paths: Dict[str, Dict] = {}
    schemas: Dict[str, Any] = {}
    servers: List[Dict[str, str]] = []

    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return {
            "openapi": "3.0.0",
            "info": {"title": "WSDL Service", "version": "1.0.0"},
            "paths": {},
            "_raw_content": content,
        }

    # Strip namespace prefixes for easier traversal
    ns_map: Dict[str, str] = {}
    for elem in root.iter():
        tag = elem.tag
        if tag.startswith("{"):
            ns_uri = tag[1:tag.index("}")]
            local = tag[tag.index("}") + 1:]
            if "xmlsoap.org/wsdl" in ns_uri and "wsdl" not in ns_map:
                ns_map["wsdl"] = ns_uri
            if "xmlsoap.org/wsdl/soap" in ns_uri and "soap" not in ns_map:
                ns_map["soap"] = ns_uri

    wsdl_ns = ns_map.get("wsdl", "http://schemas.xmlsoap.org/wsdl/")
    soap_ns = ns_map.get("soap", "http://schemas.xmlsoap.org/wsdl/soap/")

    info["title"] = root.attrib.get("name", "WSDL Service")

    # Extract service endpoint URL
    for service in root.iter(f"{{{wsdl_ns}}}service"):
        for port in service.iter(f"{{{wsdl_ns}}}port"):
            for addr in port:
                loc = addr.attrib.get("location")
                if loc:
                    servers.append({"url": loc})

    # Extract messages -> schemas
    messages: Dict[str, List[Dict[str, str]]] = {}
    for msg in root.iter(f"{{{wsdl_ns}}}message"):
        msg_name = msg.attrib.get("name", "")
        parts = []
        for part in msg.iter(f"{{{wsdl_ns}}}part"):
            pname = part.attrib.get("name", "")
            ptype = part.attrib.get("type", "string")
            if ":" in ptype:
                ptype = ptype.split(":", 1)[1]
            parts.append({"name": pname, "type": ptype})
        messages[msg_name] = parts
        if parts:
            props = {}
            for p in parts:
                props[p["name"]] = {"type": _wsdl_type_map(p["type"])}
            schemas[msg_name] = {"type": "object", "properties": props}

    # Extract portType operations -> paths
    for port_type in root.iter(f"{{{wsdl_ns}}}portType"):
        for operation in port_type.iter(f"{{{wsdl_ns}}}operation"):
            op_name = operation.attrib.get("name", "")
            if not op_name:
                continue
            path = f"/{op_name}"
            op: Dict[str, Any] = {
                "operationId": op_name,
                "summary": op_name,
                "tags": [info["title"]],
                "responses": {"200": {"description": "OK"}},
            }

            # Input message -> parameters
            input_el = operation.find(f"{{{wsdl_ns}}}input")
            if input_el is not None:
                msg_ref = input_el.attrib.get("message", "")
                if ":" in msg_ref:
                    msg_ref = msg_ref.split(":", 1)[1]
                parts = messages.get(msg_ref, [])
                if parts:
                    params = []
                    for p in parts:
                        params.append({
                            "name": p["name"],
                            "in": "query",
                            "required": True,
                            "schema": {"type": _wsdl_type_map(p["type"])},
                        })
                    op["parameters"] = params

            # Output message -> response schema
            output_el = operation.find(f"{{{wsdl_ns}}}output")
            if output_el is not None:
                msg_ref = output_el.attrib.get("message", "")
                if ":" in msg_ref:
                    msg_ref = msg_ref.split(":", 1)[1]
                if msg_ref in schemas:
                    op["responses"]["200"] = {
                        "description": "OK",
                        "content": {"application/xml": {"schema": {"$ref": f"#/components/schemas/{msg_ref}"}}},
                    }

            paths[path] = {"post": op}

    spec["info"] = info
    spec["paths"] = paths
    if servers:
        spec["servers"] = servers
    if schemas:
        spec["components"] = {"schemas": schemas}
    return spec


def _wsdl_type_map(xsd_type: str) -> str:
    """Map XSD type names to OpenAPI types."""
    mapping = {
        "string": "string", "int": "integer", "integer": "integer",
        "long": "integer", "short": "integer", "byte": "integer",
        "float": "number", "double": "number", "decimal": "number",
        "boolean": "boolean", "date": "string", "dateTime": "string",
        "time": "string", "base64Binary": "string", "anyURI": "string",
    }
    return mapping.get(xsd_type, "string")


# ── GraphQL normalizer ────────────────────────────────────────────────

_GQL_TYPE_BLOCK_RE = re.compile(
    r"^(?:type|input)\s+(\w+)(?:\s+implements\s+\w+)?\s*\{([^}]*)\}",
    re.DOTALL | re.MULTILINE,
)
_GQL_ENUM_BLOCK_RE = re.compile(
    r"^enum\s+(\w+)\s*\{([^}]*)\}",
    re.DOTALL | re.MULTILINE,
)
_GQL_FIELD_RE = re.compile(
    r"(\w+)\s*(?:\(([^)]*)\))?\s*:\s*(.+)"
)
_GQL_ARG_RE = re.compile(
    r"(\w+)\s*:\s*([^,\)]+)"
)


_GQL_SCHEMA_RE = re.compile(
    r"schema\s*\{([^}]*)\}", re.DOTALL
)
_GQL_ROOT_FIELD_RE = re.compile(
    r"(query|mutation)\s*:\s*(\w+)"
)
_GQL_DOC_STRING_RE = re.compile(r'"""[\s\S]*?"""')


def normalize_graphql(content: str) -> Dict[str, Any]:
    """Convert GraphQL SDL into an OpenAPI-like structure."""
    spec: Dict[str, Any] = {"openapi": "3.0.0"}
    info: Dict[str, Any] = {"title": "GraphQL API", "version": "1.0.0"}
    paths: Dict[str, Dict] = {}
    schemas: Dict[str, Any] = {}

    cleaned = _GQL_DOC_STRING_RE.sub("", content)

    query_type_name = "Query"
    mutation_type_name = "Mutation"
    schema_match = _GQL_SCHEMA_RE.search(cleaned)
    if schema_match:
        for root_field in _GQL_ROOT_FIELD_RE.finditer(schema_match.group(1)):
            if root_field.group(1) == "query":
                query_type_name = root_field.group(2)
            elif root_field.group(1) == "mutation":
                mutation_type_name = root_field.group(2)

    root_types = {query_type_name: ("get", "Queries"), mutation_type_name: ("post", "Mutations")}

    for type_match in _GQL_TYPE_BLOCK_RE.finditer(cleaned):
        type_name = type_match.group(1)
        body = type_match.group(2)

        if type_name in root_types:
            http_method, tag = root_types[type_name]

            for field_match in _GQL_FIELD_RE.finditer(body):
                field_name = field_match.group(1)
                args_str = field_match.group(2)
                return_type = field_match.group(3).strip()

                path = f"/{field_name}"
                op: Dict[str, Any] = {
                    "operationId": field_name,
                    "summary": f"{type_name}.{field_name}",
                    "tags": [tag],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {"application/json": {"schema": _gql_type_to_schema(return_type)}},
                        }
                    },
                }

                if args_str:
                    params = []
                    for arg_match in _GQL_ARG_RE.finditer(args_str):
                        arg_name = arg_match.group(1)
                        arg_type = arg_match.group(2).strip()
                        required = arg_type.endswith("!")
                        params.append({
                            "name": arg_name,
                            "in": "query",
                            "required": required,
                            "schema": _gql_type_to_schema(arg_type),
                        })
                    if params:
                        op["parameters"] = params

                paths[path] = {http_method: op}
        else:
            # Regular type -> schema
            props: Dict[str, Any] = {}
            required_fields: List[str] = []
            for field_match in _GQL_FIELD_RE.finditer(body):
                fname = field_match.group(1)
                ftype = field_match.group(3).strip()
                if ftype.endswith("!"):
                    required_fields.append(fname)
                props[fname] = _gql_type_to_schema(ftype)
            schema: Dict[str, Any] = {"type": "object", "properties": props}
            if required_fields:
                schema["required"] = required_fields
            schemas[type_name] = schema

    for enum_match in _GQL_ENUM_BLOCK_RE.finditer(cleaned):
        enum_name = enum_match.group(1)
        values = [v.strip() for v in enum_match.group(2).split("\n") if v.strip()]
        if values:
            schemas[enum_name] = {"type": "string", "enum": values}

    spec["info"] = info
    spec["paths"] = paths
    if schemas:
        spec["components"] = {"schemas": schemas}
    return spec


def _gql_type_to_schema(gql_type: str) -> Dict[str, Any]:
    """Map a GraphQL type annotation to an OpenAPI schema."""
    t = gql_type.strip().rstrip("!")
    scalar_map = {
        "String": "string", "Int": "integer", "Float": "number",
        "Boolean": "boolean", "ID": "string",
    }
    # List type [Foo!] or [Foo]
    list_m = re.match(r"^\[(.+)\]$", t)
    if list_m:
        inner = list_m.group(1).strip().rstrip("!")
        return {"type": "array", "items": _gql_type_to_schema(inner)}
    if t in scalar_map:
        return {"type": scalar_map[t]}
    return {"type": "string", "description": f"(GraphQL type: {t})"}


class OpenAPIToMarkdown:
    """Convert OpenAPI specification to LLM-ready markdown format."""
    
    def __init__(self, spec_path: str, output_path: Optional[str] = None):
        self.spec_path = Path(spec_path)
        self.spec = self._load_spec()
        self.components = self.spec.get('components', {})
        self.dereferenced_cache = {}
        
        # Generate output path based on API name and version
        if output_path:
            self.output_path = Path(output_path)
        else:
            self.output_path = self._generate_output_filename()
        
    def _load_spec(self) -> Dict[str, Any]:
        """Load API spec from YAML, JSON, or other formats (best-effort)."""
        with open(self.spec_path, 'r', encoding='utf-8') as f:
            content = f.read()

        suffix = self.spec_path.suffix.lower()

        if suffix == '.raml':
            raw = _safe_load_raml(content)
            return normalize_raml(raw)

        if suffix == '.apib':
            return normalize_apib(content)

        if suffix == '.wsdl':
            return normalize_wsdl(content)

        if suffix in ('.graphql', '.gql'):
            return normalize_graphql(content)

        if suffix in ('.yaml', '.yml'):
            return yaml.safe_load(content) or {}

        if suffix == '.json':
            return json.loads(content)

        try:
            result = yaml.safe_load(content)
            if isinstance(result, dict):
                return result
        except Exception:
            pass
        try:
            result = json.loads(content)
            if isinstance(result, dict):
                return result
        except Exception:
            pass

        return {
            "info": {"title": self.spec_path.stem, "version": "1.0.0"},
            "_raw_content": content,
        }
    
    def _generate_output_filename(self) -> Path:
        """Generate output filename based on API name and version."""
        info = self.spec.get('info', {})
        api_name = info.get('title', 'api')
        api_version = info.get('version', '1.0.0')
        
        # Sanitize the API name for use in filename
        # Remove/replace special characters, convert to lowercase, replace spaces with hyphens
        sanitized_name = re.sub(r'[^\w\s-]', '', api_name.lower())
        sanitized_name = re.sub(r'[-\s]+', '-', sanitized_name).strip('-')
        
        # Sanitize version (remove any non-alphanumeric except dots and hyphens)
        sanitized_version = re.sub(r'[^\w.-]', '', api_version)
        
        # Construct filename: api-name-v1.0.0.md
        filename = f"{sanitized_name}-v{sanitized_version}.md"
        
        # Place in same directory as input file
        return self.spec_path.parent / filename
    
    def _dereference(self, ref_or_obj: Any, depth: int = 0, max_depth: int = 3) -> Any:
        """
        Dereference $ref pointers (shallow inline for readability).
        Limits depth to avoid excessive expansion.
        """
        if depth > max_depth:
            return ref_or_obj
            
        if isinstance(ref_or_obj, dict):
            if '$ref' in ref_or_obj:
                ref = ref_or_obj['$ref']
                if ref in self.dereferenced_cache:
                    return self.dereferenced_cache[ref]
                
                # Parse reference like "#/components/schemas/User"
                parts = ref.split('/')
                obj = self.spec
                for part in parts[1:]:  # Skip the '#'
                    obj = obj.get(part, {})
                
                self.dereferenced_cache[ref] = obj
                return self._dereference(obj, depth + 1, max_depth)
            else:
                return {k: self._dereference(v, depth, max_depth) for k, v in ref_or_obj.items()}
        elif isinstance(ref_or_obj, list):
            return [self._dereference(item, depth, max_depth) for item in ref_or_obj]
        else:
            return ref_or_obj
    
    def _normalize_type(self, schema: Dict[str, Any]) -> str:
        """Normalize schema type to readable format."""
        if not schema:
            return "any"
        
        type_str = schema.get('type', 'object')
        fmt = schema.get('format', '')
        enum = schema.get('enum', [])
        
        if enum:
            return f"{type_str} (enum: {', '.join(map(str, enum[:5]))}{'...' if len(enum) > 5 else ''})"
        elif fmt:
            return f"{type_str} ({fmt})"
        elif type_str == 'array':
            items = schema.get('items', {})
            item_type = self._normalize_type(items) if items else 'any'
            return f"array<{item_type}>"
        elif type_str == 'object':
            props = schema.get('properties', {})
            if props:
                return f"object ({len(props)} fields)"
            return "object"
        else:
            return type_str
    
    def _format_schema_inline(self, schema: Dict[str, Any], indent: int = 0) -> str:
        """Format schema inline with key fields, types, and constraints."""
        if not schema:
            return "  " * indent + "none"
        
        lines = []
        prefix = "  " * indent
        
        schema_type = schema.get('type', 'object')
        required_fields = set(schema.get('required', []))
        
        if schema_type == 'object':
            properties = schema.get('properties', {})
            for prop_name, prop_schema in properties.items():
                is_required = prop_name in required_fields
                prop_type = self._normalize_type(prop_schema)
                description = prop_schema.get('description', '')
                
                req_marker = "required" if is_required else "optional"
                desc_str = f" — {description[:60]}..." if len(description) > 60 else f" — {description}" if description else ""
                
                lines.append(f"{prefix}- {prop_name}: {prop_type} ({req_marker}){desc_str}")
        elif schema_type == 'array':
            items = schema.get('items', {})
            item_type = self._normalize_type(items)
            lines.append(f"{prefix}array<{item_type}>")
        else:
            lines.append(f"{prefix}{self._normalize_type(schema)}")
        
        return '\n'.join(lines) if lines else f"{prefix}(empty)"
    
    def _extract_security_info(self, security: List[Dict], operation_security: Optional[List[Dict]] = None) -> str:
        """Extract and format authentication information."""
        auth_info = []
        
        # Use operation-level security if available, otherwise global
        sec_requirements = operation_security if operation_security is not None else security
        
        if not sec_requirements:
            return "None"
        
        security_schemes = self.components.get('securitySchemes', {})
        
        for req in sec_requirements:
            for scheme_name, scopes in req.items():
                scheme = security_schemes.get(scheme_name, {})
                scheme_type = scheme.get('type', 'unknown')
                
                if scheme_type == 'apiKey':
                    location = scheme.get('in', 'header')
                    name = scheme.get('name', 'X-API-Key')
                    auth_info.append(f"apiKey ({location}: {name})")
                elif scheme_type == 'http':
                    http_scheme = scheme.get('scheme', 'bearer')
                    auth_info.append(f"{http_scheme.upper()} token")
                elif scheme_type == 'oauth2':
                    scope_str = f" (scopes: {', '.join(scopes[:3])})" if scopes else ""
                    auth_info.append(f"OAuth2{scope_str}")
                elif scheme_type == 'openIdConnect':
                    auth_info.append("OpenID Connect")
                else:
                    auth_info.append(scheme_name)
        
        return ", ".join(auth_info) if auth_info else "None"
    
    def _generate_curl_example(self, method: str, path: str, operation: Dict[str, Any], base_url: str) -> str:
        """Generate a runnable curl example."""
        # Use example values from spec or create placeholders
        method_upper = method.upper()
        full_url = f"{base_url}{path}"
        
        # Replace path parameters with example values
        parameters = operation.get('parameters', [])
        path_params = {}
        query_params = []
        headers = []
        
        for param in parameters:
            param_dereferenced = self._dereference(param)
            param_name = param_dereferenced.get('name', '')
            param_in = param_dereferenced.get('in', '')
            example = param_dereferenced.get('example', param_dereferenced.get('schema', {}).get('example', 'value'))
            
            if param_in == 'path':
                path_params[param_name] = example if example != 'value' else '123'
            elif param_in == 'query':
                query_params.append(f"{param_name}={example if example != 'value' else 'example'}")
            elif param_in == 'header':
                headers.append(f'-H "{param_name}: {example if example != "value" else "value"}"')
        
        # Apply path parameters
        for param_name, param_value in path_params.items():
            full_url = full_url.replace(f'{{{param_name}}}', str(param_value))
        
        # Add query parameters
        if query_params:
            full_url += '?' + '&'.join(query_params)
        
        # Build curl command
        curl_parts = [f'curl -X {method_upper}']
        curl_parts.append(f'"{full_url}"')
        
        # Add auth header placeholder
        security = operation.get('security', self.spec.get('security', []))
        if security:
            security_schemes = self.components.get('securitySchemes', {})
            for req in security:
                for scheme_name in req.keys():
                    scheme = security_schemes.get(scheme_name, {})
                    if scheme.get('type') == 'apiKey':
                        header_name = scheme.get('name', 'X-API-Key')
                        headers.append(f'-H "{header_name}: $API_KEY"')
                    elif scheme.get('type') == 'http' and scheme.get('scheme') == 'bearer':
                        headers.append('-H "Authorization: Bearer $TOKEN"')
        
        # Add content-type for request body
        request_body = operation.get('requestBody', {})
        if request_body:
            content = request_body.get('content', {})
            if 'application/json' in content:
                headers.append('-H "Content-Type: application/json"')
                # Add simple body example
                body_schema = content['application/json'].get('schema', {})
                body_example = content['application/json'].get('example', '{"key": "value"}')
                if not isinstance(body_example, str):
                    body_example = json.dumps(body_example, separators=(',', ':'))
                curl_parts.append(f"-d '{body_example}'")
        
        # Add headers
        curl_parts.extend(headers)
        
        return ' \\\n  '.join(curl_parts)
    
    def _format_endpoint(self, path: str, method: str, operation: Dict[str, Any], tags: List[str], base_url: str) -> str:
        """Format a single endpoint block."""
        method_upper = method.upper()
        summary = operation.get('summary', operation.get('description', 'No description')[:80])
        description = operation.get('description', '')
        
        # Truncate long descriptions
        if len(description) > 200:
            description = description[:200] + "... (see full docs)"
        
        # Extract parameters
        parameters = operation.get('parameters', [])
        path_params = []
        query_params = []
        header_params = []
        
        for param in parameters:
            param = self._dereference(param)
            param_name = param.get('name', '')
            param_in = param.get('in', '')
            param_required = param.get('required', False)
            param_schema = param.get('schema', {})
            param_type = self._normalize_type(param_schema)
            req_str = "required" if param_required else "optional"
            
            param_line = f"  - {param_name} ({param_type}, {req_str})"
            
            if param_in == 'path':
                path_params.append(param_line)
            elif param_in == 'query':
                query_params.append(param_line)
            elif param_in == 'header':
                header_params.append(param_line)
        
        # Request body
        request_body = operation.get('requestBody', {})
        request_body_lines = []
        if request_body:
            content = self._dereference(request_body.get('content', {}))
            for content_type, content_schema_obj in content.items():
                schema = self._dereference(content_schema_obj.get('schema', {}))
                request_body_lines.append(f"  Content-Type: {content_type}")
                request_body_lines.append(self._format_schema_inline(schema, indent=2))
        
        # Responses
        responses = operation.get('responses', {})
        response_lines = []
        for status_code, response_obj in responses.items():
            response = self._dereference(response_obj)
            response_desc = response.get('description', '')
            content = response.get('content', {})
            
            if content:
                for content_type, content_schema_obj in content.items():
                    schema = self._dereference(content_schema_obj.get('schema', {}))
                    response_lines.append(f"  - {status_code} ({content_type}): {response_desc}")
                    response_lines.append(self._format_schema_inline(schema, indent=4))
            else:
                response_lines.append(f"  - {status_code}: {response_desc}")
        
        # Auth info
        auth_info = self._extract_security_info(
            self.spec.get('security', []),
            operation.get('security')
        )
        
        # Generate curl example
        curl_example = self._generate_curl_example(method, path, operation, base_url)
        
        # Build the block
        operation_id = operation.get('operationId', '')
        lines = [
            "=" * 80,
            f"ENDPOINT: [{method_upper}] {path}",
        ]
        if operation_id:
            lines.append(f"OPERATION_ID: {operation_id}")
        lines.extend([
            f"BASE_URL: {base_url}",
            f"TAGS: {', '.join(tags) if tags else 'none'}",
            f"SUMMARY: {summary}",
        ])
        
        if description and description != summary:
            lines.append(f"DESCRIPTION: {description}")
        
        lines.append(f"AUTH: {auth_info}")
        lines.append("")
        lines.append("REQUEST")
        
        if path_params:
            lines.append("  Path params:")
            lines.extend(path_params)
        if query_params:
            lines.append("  Query params:")
            lines.extend(query_params)
        if header_params:
            lines.append("  Header params:")
            lines.extend(header_params)
        if request_body_lines:
            lines.append("  Body:")
            lines.extend(request_body_lines)
        if not (path_params or query_params or header_params or request_body_lines):
            lines.append("  none")
        
        lines.append("")
        lines.append("RESPONSES")
        lines.extend(response_lines if response_lines else ["  none"])
        
        lines.append("")
        lines.append("EXAMPLE (curl)")
        lines.append(curl_example)
        lines.append("=" * 80)
        lines.append("")
        
        return '\n'.join(lines)
    
    def _generate_header(self) -> str:
        """Generate the markdown header section."""
        info = self.spec.get('info', {})
        title = info.get('title', 'API Documentation')
        version = info.get('version', '1.0.0')
        description = info.get('description', '')
        
        # Truncate description
        if len(description) > 500:
            description = description[:500] + "..."
        
        # Servers
        servers = self.spec.get('servers', [])
        server_lines = []
        for server in servers:
            url = server.get('url', '')
            desc = server.get('description', '')
            server_lines.append(f"  - {url}" + (f" — {desc}" if desc else ""))
        
        # Security schemes
        security_schemes = self.components.get('securitySchemes', {})
        auth_lines = []
        for scheme_name, scheme in security_schemes.items():
            scheme_type = scheme.get('type', 'unknown')
            if scheme_type == 'apiKey':
                location = scheme.get('in', 'header')
                name = scheme.get('name', '')
                auth_lines.append(f"  - {scheme_name}: API Key ({location}: {name})")
            elif scheme_type == 'http':
                http_scheme = scheme.get('scheme', 'bearer')
                auth_lines.append(f"  - {scheme_name}: HTTP {http_scheme.upper()}")
            elif scheme_type == 'oauth2':
                flows = scheme.get('flows', {})
                flow_types = ', '.join(flows.keys())
                auth_lines.append(f"  - {scheme_name}: OAuth2 ({flow_types})")
            else:
                auth_lines.append(f"  - {scheme_name}: {scheme_type}")
        
        header = [
            f"# {title}",
            f"**Version:** {version}",
            "",
        ]
        
        if description:
            header.extend([description, ""])
        
        header.append("## Base URLs")
        header.extend(server_lines if server_lines else ["  - (not specified)"])
        header.append("")
        
        if auth_lines:
            header.append("## Authentication")
            header.extend(auth_lines)
            header.append("")
        
        return '\n'.join(header)
    
    def _generate_toc(self, endpoints_by_tag: Dict[str, List[Tuple[str, str, Dict]]]) -> str:
        """Generate table of contents grouped by tag."""
        lines = ["## Endpoints by Tag", ""]
        
        for tag in sorted(endpoints_by_tag.keys()):
            lines.append(f"### {tag}")
            endpoints = endpoints_by_tag[tag]
            
            # Sort endpoints alphabetically by method then path
            sorted_endpoints = sorted(endpoints, key=lambda x: (x[1], x[0]))
            
            for path, method, operation in sorted_endpoints:
                summary = operation.get('summary', operation.get('description', ''))
                if len(summary) > 60:
                    summary = summary[:60] + "..."
                lines.append(f"- **{method.upper()}** `{path}` — {summary}")
            
            lines.append("")
        
        return '\n'.join(lines)
    
    def _group_endpoints_by_tag(self) -> Dict[str, List[Tuple[str, str, Dict]]]:
        """Group all endpoints by their tags."""
        endpoints_by_tag = defaultdict(list)
        paths = self.spec.get('paths', {})
        
        for path, path_item in paths.items():
            for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                if method in path_item:
                    operation = path_item[method]
                    tags = operation.get('tags', ['Untagged'])
                    
                    for tag in tags:
                        endpoints_by_tag[tag].append((path, method, operation))
        
        return dict(endpoints_by_tag)
    
    def _generate_components_appendix(self) -> str:
        """Generate appendix with shared components/schemas."""
        schemas = self.components.get('schemas', {})
        if not schemas:
            return ""
        
        lines = [
            "",
            "=" * 80,
            "## COMPONENTS APPENDIX",
            "=" * 80,
            "",
            "Shared schemas referenced throughout the API:",
            ""
        ]
        
        for schema_name in sorted(schemas.keys()):
            schema = self._dereference(schemas[schema_name])
            schema_type = schema.get('type', 'object')
            description = schema.get('description', '')
            
            lines.append(f"### {schema_name}")
            lines.append(f"Type: {schema_type}")
            if description:
                lines.append(f"Description: {description[:200]}{'...' if len(description) > 200 else ''}")
            lines.append("")
            lines.append(self._format_schema_inline(schema, indent=0))
            lines.append("")
        
        return '\n'.join(lines)
    
    def _get_base_url(self) -> str:
        servers = self.spec.get('servers', [])
        return servers[0].get('url', 'https://api.example.com') if servers else 'https://api.example.com'

    def convert(self) -> str:
        """Main conversion method. Returns a single monolithic markdown string."""
        base_url = self._get_base_url()
        header = self._generate_header()
        endpoints_by_tag = self._group_endpoints_by_tag()
        toc = self._generate_toc(endpoints_by_tag)

        endpoint_blocks = ["\n## Endpoint Details\n"]
        for tag in sorted(endpoints_by_tag.keys()):
            endpoint_blocks.append(f"\n### Tag: {tag}\n")
            endpoints = endpoints_by_tag[tag]
            sorted_endpoints = sorted(endpoints, key=lambda x: (x[1], x[0]))
            for path, method, operation in sorted_endpoints:
                tags = operation.get('tags', [tag])
                block = self._format_endpoint(path, method, operation, tags, base_url)
                endpoint_blocks.append(block)

        appendix = self._generate_components_appendix()
        markdown = header + "\n" + toc + "\n" + ''.join(endpoint_blocks)
        if appendix:
            markdown += "\n" + appendix
        return markdown

    def convert_chunked(self) -> Dict[str, Any]:
        """
        Progressive-disclosure output: returns a dict with separately
        addressable manifest, per-tag summaries, per-endpoint blocks,
        and per-schema definitions.

        Keys:
          manifest  - str: title, version, base URLs, auth, tag→endpoint index
          tags      - dict[str, str]: per-tag summary markdown
          endpoints - dict[str, str]: keyed by operationId (or METHOD_path fallback)
          schemas   - dict[str, str]: per-component schema markdown
        """
        base_url = self._get_base_url()
        endpoints_by_tag = self._group_endpoints_by_tag()

        manifest = self._generate_header() + "\n" + self._generate_toc(endpoints_by_tag)

        tags_dict: Dict[str, str] = {}
        endpoints_dict: Dict[str, str] = {}

        for tag in sorted(endpoints_by_tag.keys()):
            tag_lines = [f"## {tag}", ""]
            endpoints = endpoints_by_tag[tag]
            sorted_endpoints = sorted(endpoints, key=lambda x: (x[1], x[0]))

            for path, method, operation in sorted_endpoints:
                op_tags = operation.get('tags', [tag])
                block = self._format_endpoint(path, method, operation, op_tags, base_url)

                op_id = operation.get('operationId') or f"{method.upper()}_{path.replace('/', '_').strip('_')}"
                endpoints_dict[op_id] = block

                summary = operation.get('summary', operation.get('description', ''))
                if len(summary) > 60:
                    summary = summary[:60] + "..."
                tag_lines.append(f"- **{method.upper()}** `{path}` ({op_id}) — {summary}")

            tag_lines.append("")
            tags_dict[tag] = "\n".join(tag_lines)

        schemas_dict: Dict[str, str] = {}
        for schema_name in sorted(self.components.get('schemas', {}).keys()):
            schema = self._dereference(self.components['schemas'][schema_name])
            schema_type = schema.get('type', 'object')
            description = schema.get('description', '')
            lines = [f"### {schema_name}", f"Type: {schema_type}"]
            if description:
                lines.append(f"Description: {description[:200]}{'...' if len(description) > 200 else ''}")
            lines.append("")
            lines.append(self._format_schema_inline(schema, indent=0))
            lines.append("")
            schemas_dict[schema_name] = "\n".join(lines)

        return {
            "manifest": manifest,
            "tags": tags_dict,
            "endpoints": endpoints_dict,
            "schemas": schemas_dict,
        }

    def generate_tool_schemas(self) -> List[Dict[str, Any]]:
        """
        Emit an array of JSON-Schema tool definitions (one per endpoint),
        compatible with OpenAI / Anthropic function-calling format.

        Each tool has: name (operationId), description (summary),
        and parameters (merged path + query params and request body).
        """
        tools: List[Dict[str, Any]] = []
        paths = self.spec.get('paths', {})

        for path, path_item in paths.items():
            for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                if method not in path_item:
                    continue
                operation = path_item[method]
                op_id = operation.get('operationId') or f"{method.upper()}_{path.replace('/', '_').strip('_')}"
                summary = operation.get('summary', operation.get('description', ''))

                properties: Dict[str, Any] = {}
                required: List[str] = []

                for raw_param in operation.get('parameters', []):
                    deref_param = self._dereference(raw_param)
                    p_name = deref_param.get('name', '')
                    p_schema = self._dereference(deref_param.get('schema', {}))
                    p_in = deref_param.get('in', '')
                    p_required = deref_param.get('required', p_in == 'path')
                    desc = deref_param.get('description', '')

                    param_prop: Dict[str, Any] = {}
                    if p_schema.get('type'):
                        param_prop['type'] = p_schema['type']
                    if p_schema.get('enum'):
                        param_prop['enum'] = p_schema['enum']
                    if desc:
                        param_prop['description'] = desc
                    if p_schema.get('format'):
                        param_prop['format'] = p_schema['format']
                    if not param_prop.get('type'):
                        param_prop['type'] = 'string'
                    properties[p_name] = param_prop
                    if p_required:
                        required.append(p_name)

                request_body = operation.get('requestBody', {})
                if request_body:
                    content = self._dereference(request_body.get('content', {}))
                    json_content = content.get('application/json', {})
                    body_schema = self._dereference(json_content.get('schema', {}))
                    if body_schema.get('properties'):
                        body_required = set(body_schema.get('required', []))
                        for bp_name, bp_raw_schema in body_schema['properties'].items():
                            bp_schema = self._dereference(bp_raw_schema)
                            body_prop: Dict[str, Any] = {}
                            if bp_schema.get('type'):
                                body_prop['type'] = bp_schema['type']
                            if bp_schema.get('enum'):
                                body_prop['enum'] = bp_schema['enum']
                            if bp_schema.get('description'):
                                body_prop['description'] = bp_schema['description']
                            if bp_schema.get('format'):
                                body_prop['format'] = bp_schema['format']
                            if not body_prop.get('type'):
                                body_prop['type'] = 'string'
                            if bp_name not in properties:
                                properties[bp_name] = body_prop
                            if bp_name in body_required and bp_name not in required:
                                required.append(bp_name)

                tool: Dict[str, Any] = {
                    "name": op_id,
                    "description": summary[:200] if summary else f"{method.upper()} {path}",
                    "parameters": {
                        "type": "object",
                        "properties": properties,
                    },
                }
                if required:
                    tool["parameters"]["required"] = required
                tools.append(tool)

        return tools
    
    def save(self, content: str):
        """Save markdown to file."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Generated LLM-ready markdown: {self.output_path}")
        print(f"📊 File size: {len(content):,} characters")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert API specs to LLM-ready markdown, chunked JSON, or tool schemas."
    )
    parser.add_argument("input", help="Path to API spec file (YAML, JSON, RAML, WSDL, GraphQL, API Blueprint)")
    parser.add_argument("output", nargs="?", default=None, help="Output file path (default: auto-generated)")
    parser.add_argument("--chunked", action="store_true", help="Output progressive-disclosure chunks as JSON")
    parser.add_argument("--tools", action="store_true", help="Output JSON Schema tool definitions for function-calling")

    args = parser.parse_args()

    try:
        converter = OpenAPIToMarkdown(args.input, args.output)

        if args.chunked:
            result = converter.convert_chunked()
            out_path = args.output or converter.output_path.with_suffix(".chunks.json")
            Path(out_path).write_text(json.dumps(result, indent=2), encoding="utf-8")
            print(f"Chunked output written to {out_path}")
        elif args.tools:
            result = converter.generate_tool_schemas()
            out_path = args.output or converter.output_path.with_suffix(".tools.json")
            Path(out_path).write_text(json.dumps(result, indent=2), encoding="utf-8")
            print(f"Tool schemas written to {out_path}")
        else:
            markdown = converter.convert()
            converter.save(markdown)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

