#!/usr/bin/env python3
"""
OpenAPI to Agent-Ready Artifacts Converter

Converts OpenAPI YAML/JSON specs into three artifacts:
1. tools.json - Machine-readable tool/function specs for agents
2. docs.md - Human-readable reference for prompting/RAG
3. chunks.jsonl - Retrieval chunks for fast context injection

Based on the blueprint from new_instructions.md
"""

import json
import yaml
import sys
import re
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set
from collections import defaultdict
from copy import deepcopy


class OpenAPIToAgent:
    """Convert OpenAPI specification to agent-ready artifacts."""
    
    def __init__(self, spec_path: str, output_dir: Optional[str] = None, server_index: int = 0):
        self.spec_path = Path(spec_path)
        self.output_dir = Path(output_dir) if output_dir else self.spec_path.parent / "output"
        self.server_index = server_index
        self.spec = self._load_spec()
        self.components = self.spec.get('components', {})
        self.dereferenced_cache = {}
        self.ref_stack = []  # For cycle detection
        self.used_schemas = set()  # Track which schemas are referenced
        
    def _load_spec(self) -> Dict[str, Any]:
        """Load OpenAPI spec from YAML or JSON."""
        with open(self.spec_path, 'r', encoding='utf-8') as f:
            if self.spec_path.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            else:
                return json.load(f)
    
    def _normalize_value(self, value: Any) -> Any:
        """Normalize values to JSON-serializable types."""
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        return value
    
    def _dereference(self, ref_or_obj: Any, max_depth: int = 10) -> Any:
        """
        Dereference $ref pointers recursively with cycle detection.
        """
        if len(self.ref_stack) > max_depth:
            return {"type": "object", "description": "(circular reference)"}
        
        # Normalize datetime objects
        if isinstance(ref_or_obj, (datetime, date)):
            return ref_or_obj.isoformat()
            
        if isinstance(ref_or_obj, dict):
            if '$ref' in ref_or_obj:
                ref = ref_or_obj['$ref']
                
                # Cycle detection
                if ref in self.ref_stack:
                    return {"type": "object", "description": f"(circular: {ref})"}
                
                if ref in self.dereferenced_cache:
                    return self.dereferenced_cache[ref]
                
                # Parse reference like "#/components/schemas/User"
                parts = ref.split('/')
                obj = self.spec
                for part in parts[1:]:  # Skip the '#'
                    obj = obj.get(part, {})
                
                # Track schema usage
                if '/schemas/' in ref:
                    schema_name = ref.split('/schemas/')[-1]
                    self.used_schemas.add(schema_name)
                
                self.ref_stack.append(ref)
                dereferenced = self._dereference(deepcopy(obj), max_depth)
                self.ref_stack.pop()
                
                self.dereferenced_cache[ref] = dereferenced
                return dereferenced
            else:
                return {k: self._dereference(v, max_depth) for k, v in ref_or_obj.items()}
        elif isinstance(ref_or_obj, list):
            return [self._dereference(item, max_depth) for item in ref_or_obj]
        elif isinstance(ref_or_obj, (datetime, date)):
            return ref_or_obj.isoformat()
        else:
            return ref_or_obj
    
    def _flatten_allof(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Flatten allOf by merging all schemas."""
        if 'allOf' not in schema:
            return schema
        
        merged = {}
        for sub_schema in schema['allOf']:
            sub_schema = self._dereference(sub_schema)
            if 'properties' in sub_schema:
                if 'properties' not in merged:
                    merged['properties'] = {}
                merged['properties'].update(sub_schema['properties'])
            if 'required' in sub_schema:
                if 'required' not in merged:
                    merged['required'] = []
                merged['required'].extend(sub_schema['required'])
            # Merge other fields
            for key in sub_schema:
                if key not in ['properties', 'required', 'allOf']:
                    merged[key] = sub_schema[key]
        
        # Copy over other fields from original schema
        for key in schema:
            if key != 'allOf' and key not in merged:
                merged[key] = schema[key]
        
        return merged
    
    def _pick_servers(self) -> List[str]:
        """Extract and normalize server URLs."""
        servers = self.spec.get('servers', [])
        if not servers:
            return ["https://api.example.com"]
        
        server_urls = []
        for server in servers:
            url = server.get('url', '')
            if url:
                server_urls.append(url)
        
        return server_urls if server_urls else ["https://api.example.com"]
    
    def _extract_auth(self) -> Dict[str, Any]:
        """Extract and normalize authentication info."""
        security_schemes = self.components.get('securitySchemes', {})
        if not security_schemes:
            return {"type": "none"}
        
        # Take first security scheme as primary
        for scheme_name, scheme in security_schemes.items():
            scheme_type = scheme.get('type', '')
            
            if scheme_type == 'apiKey':
                return {
                    "type": "apiKey",
                    "in": scheme.get('in', 'header'),
                    "name": scheme.get('name', 'X-API-Key'),
                    "format": "${API_KEY}"
                }
            elif scheme_type == 'http':
                http_scheme = scheme.get('scheme', 'bearer')
                if http_scheme == 'bearer':
                    return {
                        "type": "bearer",
                        "header": "Authorization",
                        "format": "Bearer ${TOKEN}"
                    }
                elif http_scheme == 'basic':
                    return {
                        "type": "basic",
                        "header": "Authorization",
                        "format": "Basic ${CREDENTIALS}"
                    }
            elif scheme_type == 'oauth2':
                flows = scheme.get('flows', {})
                scopes = []
                for flow_type, flow in flows.items():
                    if 'scopes' in flow:
                        scopes.extend(flow['scopes'].keys())
                return {
                    "type": "oauth2",
                    "flows": list(flows.keys()),
                    "oauth2_scopes": scopes[:10]  # Limit to first 10
                }
        
        return {"type": "none"}
    
    def _make_operation_name(self, operation: Dict[str, Any], path: str, method: str) -> str:
        """Generate unique operation name."""
        # Prefer operationId
        if 'operationId' in operation:
            name = operation['operationId']
            # Sanitize: remove special chars, convert to snake_case
            name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
            name = re.sub(r'_+', '_', name).strip('_').lower()
            return name
        
        # Build from path and method
        tags = operation.get('tags', [])
        tag = tags[0] if tags else 'api'
        
        # Clean tag
        tag = re.sub(r'[^a-zA-Z0-9]', '_', tag).lower()
        
        # Clean path segments
        path_parts = [p for p in path.split('/') if p and not p.startswith('{')]
        path_str = '_'.join(path_parts[:2]) if path_parts else 'root'
        
        # Handle path params
        has_id = '{id}' in path or '{' in path.split('/')[-1]
        suffix = '_by_id' if has_id else ''
        
        name = f"{tag}_{method}_{path_str}{suffix}"
        name = re.sub(r'_+', '_', name).strip('_')
        
        return name
    
    def _merge_parameters(self, path_params: List[Dict], operation_params: List[Dict]) -> List[Dict]:
        """Merge path-level and operation-level parameters."""
        # Dereference all params
        all_params = []
        param_names = set()
        
        for param in path_params + operation_params:
            param = self._dereference(param)
            name = param.get('name', '')
            if name and name not in param_names:
                all_params.append(param)
                param_names.add(name)
        
        return all_params
    
    def _params_to_json_schema(self, parameters: List[Dict]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Convert OpenAPI parameters to JSON Schema and arg_mapping."""
        properties = {}
        required = []
        arg_mapping = {}
        
        for param in parameters:
            name = param.get('name', '')
            param_in = param.get('in', 'query')
            param_required = param.get('required', False)
            schema = param.get('schema', {'type': 'string'})
            description = param.get('description', '')
            
            # Build property
            prop = {
                "type": schema.get('type', 'string'),
                "description": description[:200] if description else f"{name} parameter"
            }
            
            # Add constraints
            for key in ['minimum', 'maximum', 'minLength', 'maxLength', 'pattern', 'enum', 'default']:
                if key in schema:
                    prop[key] = schema[key]
            
            properties[name] = prop
            
            if param_required:
                required.append(name)
            
            # Arg mapping
            arg_mapping[name] = {
                "in": param_in,
                "name": name
            }
            
            # Add style/explode if present
            if 'style' in param:
                arg_mapping[name]['style'] = param['style']
            if 'explode' in param:
                arg_mapping[name]['explode'] = param['explode']
        
        json_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": properties
        }
        
        if required:
            json_schema["required"] = required
        
        return json_schema, arg_mapping
    
    def _extract_request_body(self, operation: Dict[str, Any]) -> Tuple[Optional[Dict], Dict[str, Any], List[str]]:
        """Extract request body schema, metadata, and content types."""
        request_body = operation.get('requestBody', {})
        if not request_body:
            return None, {}, []
        
        request_body = self._dereference(request_body)
        content = request_body.get('content', {})
        
        # Prefer application/json
        content_types = ['application/json', 'multipart/form-data', 'application/x-www-form-urlencoded']
        chosen_type = None
        for ct in content_types:
            if ct in content:
                chosen_type = ct
                break
        
        if not chosen_type:
            chosen_type = list(content.keys())[0] if content else None
        
        if not chosen_type:
            return None, {}, []
        
        schema = content[chosen_type].get('schema', {})
        schema = self._dereference(schema)
        schema = self._flatten_allof(schema)
        
        metadata = {
            "content_type": chosen_type,
            "required": request_body.get('required', False),
            "schema": schema
        }
        
        return schema, metadata, list(content.keys())
    
    def _extract_success_response(self, operation: Dict[str, Any]) -> Tuple[Optional[Dict], int, str, List[str]]:
        """Extract success response schema, status code, media type, and all media types."""
        responses = operation.get('responses', {})
        
        # Try success codes in order
        for code in ['200', '201', '202', '204']:
            if code in responses:
                response = self._dereference(responses[code])
                content = response.get('content', {})
                
                if code == '204':
                    return {"type": "null"}, 204, "application/json", []
                
                # Prefer application/json
                if 'application/json' in content:
                    schema = content['application/json'].get('schema', {})
                    schema = self._dereference(schema)
                    schema = self._flatten_allof(schema)
                    return schema, int(code), "application/json", list(content.keys())
                elif content:
                    media_type = list(content.keys())[0]
                    schema = content[media_type].get('schema', {})
                    schema = self._dereference(schema)
                    schema = self._flatten_allof(schema)
                    return schema, int(code), media_type, list(content.keys())
                else:
                    return {"type": "null"}, int(code), "application/json", []
        
        return {"type": "null"}, 200, "application/json", []
    
    def _detect_pagination(self, parameters: List[Dict], response_schema: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Detect pagination pattern heuristically."""
        param_names = {p.get('name', '').lower() for p in parameters}
        
        # Check for limit/offset
        if 'limit' in param_names or 'offset' in param_names:
            return {
                "style": "limit-offset",
                "limit_param": "limit" if 'limit' in param_names else None,
                "offset_param": "offset" if 'offset' in param_names else None,
                "items_path": "$",
                "next_offset_path": "$.next_offset"
            }
        
        # Check for page/per_page
        if 'page' in param_names or 'per_page' in param_names:
            return {
                "style": "page-based",
                "page_param": "page" if 'page' in param_names else None,
                "per_page_param": "per_page" if 'per_page' in param_names else None,
                "items_path": "$",
                "next_page_path": "$.next_page"
            }
        
        # Check for cursor
        if 'cursor' in param_names or 'page_token' in param_names:
            return {
                "style": "cursor",
                "cursor_param": "cursor" if 'cursor' in param_names else "page_token",
                "items_path": "$.items",
                "next_cursor_path": "$.next_cursor"
            }
        
        # Check response schema for hints
        if response_schema and response_schema.get('type') == 'object':
            props = response_schema.get('properties', {})
            if 'next_cursor' in props or 'next' in props or 'next_page' in props:
                return {
                    "style": "cursor",
                    "cursor_param": "cursor",
                    "items_path": "$.items",
                    "next_cursor_path": "$.next_cursor" if 'next_cursor' in props else "$.next"
                }
        
        return None
    
    def _extract_errors(self, operation: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract error responses."""
        responses = operation.get('responses', {})
        errors = []
        
        for status_code, response_obj in responses.items():
            if status_code.startswith('4') or status_code.startswith('5'):
                response = self._dereference(response_obj)
                description = response.get('description', '')
                # Take first sentence
                name = description.split('.')[0] if description else f"Error {status_code}"
                errors.append({
                    "status": int(status_code),
                    "name": name[:80]
                })
        
        return errors
    
    def _is_auth_required(self, operation: Dict[str, Any]) -> bool:
        """Check if operation requires authentication."""
        op_security = operation.get('security')
        global_security = self.spec.get('security', [])
        
        # If operation explicitly sets security, use that
        if op_security is not None:
            return len(op_security) > 0
        
        # Otherwise use global
        return len(global_security) > 0
    
    def _synthesize_example_value(self, schema: Dict[str, Any], param_name: str) -> Any:
        """Synthesize example value from schema."""
        if 'example' in schema:
            return schema['example']
        if 'default' in schema:
            return schema['default']
        if 'enum' in schema:
            return schema['enum'][0]
        
        schema_type = schema.get('type', 'string')
        
        if schema_type == 'integer':
            return 1
        elif schema_type == 'number':
            return 1.0
        elif schema_type == 'boolean':
            return True
        elif schema_type == 'array':
            return []
        elif schema_type == 'object':
            return {}
        else:
            # Heuristics for common param names
            if 'id' in param_name.lower():
                return "123"
            elif 'name' in param_name.lower():
                return "example"
            elif 'email' in param_name.lower():
                return "user@example.com"
            else:
                return "value"
    
    def _generate_curl_example(self, api_info: Dict[str, Any], tool: Dict[str, Any]) -> str:
        """Generate minimal curl example."""
        base_url = api_info['servers'][0]
        method = tool['x-http']['method']
        path = tool['x-http']['path_template']
        
        # Build URL with path params
        full_url = f"{base_url}{path}"
        query_params = []
        headers = []
        
        parameters = tool['parameters']
        arg_mapping = tool['x-http']['arg_mapping']
        
        for param_name, mapping in arg_mapping.items():
            param_schema = parameters['properties'].get(param_name, {})
            example_value = self._synthesize_example_value(param_schema, param_name)
            
            if mapping['in'] == 'path':
                full_url = full_url.replace(f"{{{param_name}}}", str(example_value))
            elif mapping['in'] == 'query':
                query_params.append(f"{param_name}={example_value}")
            elif mapping['in'] == 'header':
                headers.append(f'-H "{param_name}: {example_value}"')
        
        if query_params:
            full_url += '?' + '&'.join(query_params[:2])  # Limit to 2 params
        
        # Auth header
        auth = api_info.get('auth', {})
        if tool['x-http'].get('auth_required') and auth.get('type') != 'none':
            if auth['type'] == 'bearer':
                headers.append(f'-H "{auth["header"]}: Bearer $TOKEN"')
            elif auth['type'] == 'apiKey':
                if auth['in'] == 'header':
                    headers.append(f'-H "{auth["name"]}: $API_KEY"')
        
        curl = f"curl -X {method} '{full_url}'"
        if headers:
            curl += ' \\\n  ' + ' \\\n  '.join(headers[:3])
        
        return curl
    
    def _generate_tools_json(self) -> Dict[str, Any]:
        """Generate the main tools.json artifact."""
        info = self.spec.get('info', {})
        
        api = {
            "api_name": info.get('title', 'API'),
            "version": info.get('version', '1.0.0'),
            "servers": self._pick_servers(),
            "auth": self._extract_auth(),
            "common_headers": [],
            "rate_limits": {"headers": ["X-RateLimit-Remaining", "Retry-After"]},
            "tools": [],
            "components": {"schemas": {}}
        }
        
        paths = self.spec.get('paths', {})
        operation_names = set()
        
        for path, path_item in sorted(paths.items()):
            # Get path-level parameters
            path_params = path_item.get('parameters', [])
            
            for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                if method not in path_item:
                    continue
                
                operation = path_item[method]
                
                # Build tool
                tool = {}
                
                # Name
                name = self._make_operation_name(operation, path, method)
                # Ensure uniqueness
                original_name = name
                counter = 2
                while name in operation_names:
                    name = f"{original_name}_{counter}"
                    counter += 1
                operation_names.add(name)
                tool['name'] = name
                
                # Description
                summary = operation.get('summary', '')
                description = operation.get('description', '')
                desc_text = summary or description.split('.')[0] if description else f"{method.upper()} {path}"
                tool['description'] = desc_text[:160]
                
                # Parameters
                op_params = operation.get('parameters', [])
                merged_params = self._merge_parameters(path_params, op_params)
                parameters_schema, arg_mapping = self._params_to_json_schema(merged_params)
                
                # Request body
                body_schema, body_meta, request_content_types = self._extract_request_body(operation)
                if body_schema:
                    # Add body to arg_mapping
                    if body_schema.get('type') == 'object' and 'properties' in body_schema:
                        for prop_name in body_schema['properties']:
                            arg_mapping[prop_name] = {"in": "body", "name": prop_name}
                
                tool['parameters'] = parameters_schema
                
                # Returns
                returns_schema, success_code, response_media_type, response_content_types = self._extract_success_response(operation)
                tool['returns'] = returns_schema
                
                # x-http
                tool['x-http'] = {
                    "method": method.upper(),
                    "path_template": path,
                    "arg_mapping": arg_mapping,
                    "request_body": body_meta if body_schema else None,
                    "success_code": success_code,
                    "response_pointer": response_media_type,
                    "auth_required": self._is_auth_required(operation),
                    "content_types": {
                        "request": request_content_types,
                        "response": response_content_types
                    }
                }
                
                # Pagination
                pagination = self._detect_pagination(merged_params, returns_schema)
                if pagination:
                    tool['x-http']['pagination'] = pagination
                
                # Errors
                tool['errors'] = self._extract_errors(operation)
                
                # Examples (generate after tool is complete)
                curl_example = self._generate_curl_example(api, tool)
                tool['examples'] = {
                    "curl": curl_example,
                    "response_excerpt": '{"example": "response"}'
                }
                
                api['tools'].append(tool)
        
        # Add used schemas to components
        schemas = self.components.get('schemas', {})
        for schema_name in self.used_schemas:
            if schema_name in schemas:
                api['components']['schemas'][schema_name] = self._dereference(schemas[schema_name])
        
        return api
    
    def _generate_docs_md(self, api: Dict[str, Any]) -> str:
        """Generate human-readable docs.md."""
        lines = [
            f"# {api['api_name']}",
            f"**Version:** {api['version']}",
            "",
            "## Base URLs",
        ]
        
        for url in api['servers']:
            lines.append(f"- {url}")
        
        lines.append("")
        lines.append("## Authentication")
        auth = api['auth']
        if auth['type'] == 'bearer':
            lines.append(f"- Type: Bearer token")
            lines.append(f"- Header: `{auth['header']}: {auth['format']}`")
        elif auth['type'] == 'apiKey':
            lines.append(f"- Type: API Key")
            lines.append(f"- Location: {auth['in']}")
            lines.append(f"- Parameter: `{auth['name']}`")
        elif auth['type'] == 'oauth2':
            lines.append(f"- Type: OAuth2")
            lines.append(f"- Flows: {', '.join(auth['flows'])}")
        else:
            lines.append("- None required")
        
        lines.append("")
        lines.append("## Rate Limits")
        lines.append(f"- Headers: {', '.join(api['rate_limits']['headers'])}")
        lines.append("")
        
        # Group by tag
        tools_by_tag = defaultdict(list)
        for tool in api['tools']:
            # Infer tag from name
            tag = tool['name'].split('_')[0].title()
            tools_by_tag[tag].append(tool)
        
        lines.append("## Endpoints")
        lines.append("")
        
        for tag in sorted(tools_by_tag.keys()):
            lines.append(f"### {tag}")
            lines.append("")
            
            for tool in tools_by_tag[tag]:
                method = tool['x-http']['method']
                path = tool['x-http']['path_template']
                desc = tool['description']
                
                lines.append(f"#### `{tool['name']}`")
                lines.append(f"**{method}** `{path}`")
                lines.append("")
                lines.append(f"*{desc}*")
                lines.append("")
                
                # Required params
                required = tool['parameters'].get('required', [])
                if required:
                    lines.append("**Required parameters:**")
                    for param in required:
                        prop = tool['parameters']['properties'].get(param, {})
                        param_type = prop.get('type', 'string')
                        param_desc = prop.get('description', '')
                        lines.append(f"- `{param}` ({param_type}): {param_desc}")
                    lines.append("")
                
                # Auth
                if tool['x-http']['auth_required']:
                    lines.append(f"**Auth:** Required ({auth['type']})")
                    lines.append("")
                
                # Pagination
                if 'pagination' in tool['x-http']:
                    pag = tool['x-http']['pagination']
                    lines.append(f"**Pagination:** {pag['style']}")
                    lines.append("")
                
                # Example
                lines.append("**Example:**")
                lines.append("```bash")
                lines.append(tool['examples']['curl'])
                lines.append("```")
                lines.append("")
                
                # Errors
                if tool['errors']:
                    lines.append("**Common errors:**")
                    for error in tool['errors'][:3]:
                        lines.append(f"- {error['status']}: {error['name']}")
                    lines.append("")
                
                lines.append("---")
                lines.append("")
        
        return '\n'.join(lines)
    
    def _generate_chunks_jsonl(self, api: Dict[str, Any]) -> str:
        """Generate chunks.jsonl for RAG."""
        chunks = []
        
        for tool in api['tools']:
            # Infer tag
            tag = tool['name'].split('_')[0]
            method = tool['x-http']['method']
            path = tool['x-http']['path_template']
            
            # Build text
            text_parts = [tool['description']]
            
            # Params
            required = tool['parameters'].get('required', [])
            if required:
                param_strs = []
                for param in required[:5]:  # Limit to 5
                    prop = tool['parameters']['properties'].get(param, {})
                    param_type = prop.get('type', 'string')
                    param_strs.append(f"{param} ({param_type})")
                text_parts.append(f"Required params: {', '.join(param_strs)}.")
            
            # Returns
            returns = tool.get('returns', {})
            ret_type = returns.get('type', 'object')
            text_parts.append(f"Returns {ret_type}.")
            
            # Pagination
            if 'pagination' in tool['x-http']:
                pag_style = tool['x-http']['pagination']['style']
                text_parts.append(f"Pagination: {pag_style}.")
            
            text = ' '.join(text_parts)
            
            # Limit to 800 chars
            if len(text) > 800:
                text = text[:797] + "..."
            
            chunk = {
                "id": tool['name'],
                "tag": tag,
                "method": method,
                "path": path,
                "text": text,
                "meta": {
                    "required": required,
                    "auth": tool['x-http']['auth_required']
                }
            }
            
            chunks.append(json.dumps(chunk, separators=(',', ':')))
        
        return '\n'.join(chunks)
    
    def convert(self):
        """Main conversion - generates all three artifacts."""
        print(f"📖 Loading OpenAPI spec: {self.spec_path}")
        
        # Generate tools.json
        print("🔧 Generating tools.json...")
        api = self._generate_tools_json()
        
        # Generate docs.md
        print("📝 Generating docs.md...")
        docs = self._generate_docs_md(api)
        
        # Generate chunks.jsonl
        print("📦 Generating chunks.jsonl...")
        chunks = self._generate_chunks_jsonl(api)
        
        # Save all
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        tools_path = self.output_dir / "tools.json"
        with open(tools_path, 'w', encoding='utf-8') as f:
            json.dump(api, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved: {tools_path} ({len(api['tools'])} tools)")
        
        docs_path = self.output_dir / "docs.md"
        with open(docs_path, 'w', encoding='utf-8') as f:
            f.write(docs)
        print(f"✅ Saved: {docs_path} ({len(docs):,} chars)")
        
        chunks_path = self.output_dir / "chunks.jsonl"
        with open(chunks_path, 'w', encoding='utf-8') as f:
            f.write(chunks)
        print(f"✅ Saved: {chunks_path} ({len(chunks.splitlines())} chunks)")
        
        print(f"\n🎉 Done! Output directory: {self.output_dir}")


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python new_main.py <openapi-file.yaml|json> [--out <output-dir>] [--server-index <N>]")
        print("\nExample:")
        print("  python new_main.py ../APIs.guru-swagger.json")
        print("  python new_main.py api-spec.yaml --out ./my-output")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = None
    server_index = 0
    
    # Simple arg parsing
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--out' and i + 1 < len(sys.argv):
            output_dir = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--server-index' and i + 1 < len(sys.argv):
            server_index = int(sys.argv[i + 1])
            i += 2
        else:
            i += 1
    
    try:
        converter = OpenAPIToAgent(input_file, output_dir, server_index)
        converter.convert()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

