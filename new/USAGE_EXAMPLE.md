# Usage Example

## Quick Start

```bash
# Run the converter on the APIs.guru spec
cd /Users/m0/Documents/Building/bigberlinhack/new
python3 new_main.py ../APIs.guru-swagger.json --out ./output
```

## Expected Output

```
📖 Loading OpenAPI spec: ../APIs.guru-swagger.json
🔧 Generating tools.json...
📝 Generating docs.md...
📦 Generating chunks.jsonl...
✅ Saved: output/tools.json (7 tools)
✅ Saved: output/docs.md (1,893 chars)
✅ Saved: output/chunks.jsonl (7 chunks)

🎉 Done! Output directory: output
```

## What Gets Generated

### 1. tools.json
Complete tool definitions with JSON Schema parameters, return types, HTTP metadata, and examples:

```json
{
  "api_name": "APIs.guru",
  "version": "2.2.0",
  "servers": ["https://api.apis.guru/v2"],
  "auth": {"type": "none"},
  "tools": [
    {
      "name": "listapis",
      "description": "List all APIs",
      "parameters": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {}
      },
      "returns": { "type": "object", ... },
      "x-http": {
        "method": "GET",
        "path_template": "/list.json",
        "arg_mapping": {},
        "success_code": 200,
        "response_pointer": "application/json",
        "auth_required": false,
        "content_types": {"request": [], "response": ["application/json"]}
      },
      "examples": {
        "curl": "curl -X GET 'https://api.apis.guru/v2/list.json'"
      },
      "errors": []
    }
  ],
  "components": {"schemas": {}}
}
```

### 2. docs.md
Human-readable markdown with organized endpoint documentation:

```markdown
# APIs.guru
**Version:** 2.2.0

## Base URLs
- https://api.apis.guru/v2

## Authentication
- None required

## Rate Limits
- Headers: X-RateLimit-Remaining, Retry-After

## Endpoints

### Listapis

#### `listapis`
**GET** `/list.json`

*List all APIs*

**Example:**
\`\`\`bash
curl -X GET 'https://api.apis.guru/v2/list.json'
\`\`\`
```

### 3. chunks.jsonl
Compact retrieval chunks (one JSON object per line):

```json
{"id":"listapis","tag":"listapis","method":"GET","path":"/list.json","text":"List all APIs Returns object.","meta":{"required":[],"auth":false}}
{"id":"getmetrics","tag":"getmetrics","method":"GET","path":"/metrics.json","text":"Get basic metrics Returns object.","meta":{"required":[],"auth":false}}
```

## Use Cases

### For AI Agents
- Load `tools.json` as function definitions
- Use `x-http` metadata to build actual HTTP requests
- Reference `arg_mapping` to place parameters correctly (path/query/header/body)

### For RAG Systems
- Index `chunks.jsonl` with vector embeddings
- Retrieve relevant endpoints based on user queries
- Inject compact context into LLM prompts

### For Developers
- Read `docs.md` for quick API reference
- Copy curl examples for testing
- Understand auth requirements and pagination patterns

## Advanced Usage

### Using a Different Server
If the OpenAPI spec defines multiple servers:

```bash
python3 new_main.py api.yaml --server-index 1
```

### Custom Output Location
```bash
python3 new_main.py api.yaml --out ~/my-project/api-docs
```

### With YAML Input
```bash
python3 new_main.py petstore.yaml --out ./petstore-docs
```

## Integration Examples

### Load tools in Python
```python
import json

with open('output/tools.json') as f:
    api = json.load(f)

for tool in api['tools']:
    print(f"Tool: {tool['name']}")
    print(f"  Method: {tool['x-http']['method']}")
    print(f"  Path: {tool['x-http']['path_template']}")
    print(f"  Auth: {tool['x-http']['auth_required']}")
```

### Index chunks for RAG
```python
import json

chunks = []
with open('output/chunks.jsonl') as f:
    for line in f:
        chunk = json.loads(line)
        chunks.append(chunk)

# Now embed chunk['text'] and store with chunk['id'] for retrieval
```

### Parse markdown for documentation site
```python
with open('output/docs.md') as f:
    markdown_content = f.read()

# Use markdown parser to convert to HTML for docs site
```

## Tips

1. **Large APIs**: The script handles large specs but may take a few seconds for 100+ endpoints
2. **Auth**: Check the `auth` field in tools.json to understand authentication requirements
3. **Pagination**: Look for `x-http.pagination` to understand how to handle paginated endpoints
4. **Errors**: Each tool includes an `errors` array with common error codes and descriptions
5. **Schema References**: Referenced schemas are automatically included in `components.schemas`

