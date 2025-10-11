# Quickstart Guide

Get started with the OpenAPI to Agent Artifacts converter in 2 minutes.

## Installation

```bash
# Clone or navigate to the project
cd /path/to/bigberlinhack/new

# Install dependencies (PyYAML for YAML parsing)
pip install PyYAML>=6.0.1
```

## Basic Usage

### 1. Convert an OpenAPI spec

```bash
python3 new_main.py ../APIs.guru-swagger.json
```

This generates three files in `./output/`:
- `tools.json` - Machine-readable tool definitions
- `docs.md` - Human-readable API documentation  
- `chunks.jsonl` - RAG-ready chunks for LLM context injection

### 2. Specify output directory

```bash
python3 new_main.py api-spec.yaml --out ./my-api-docs
```

### 3. Choose a different server

If your OpenAPI spec has multiple servers:

```bash
python3 new_main.py api-spec.yaml --server-index 1
```

## Validate Output

```bash
python3 test.py output
```

This runs validation tests to ensure:
- ✅ tools.json has valid structure
- ✅ All path parameters are mapped correctly
- ✅ chunks.jsonl entries are under 800 chars
- ✅ Required sections exist in docs.md

## Example Workflow

```bash
# 1. Convert your OpenAPI spec
python3 new_main.py ../APIs.guru-swagger.yaml --out ./api-output

# 2. Validate the output
python3 test.py ./api-output

# 3. Use the artifacts
# - Load tools.json into your AI agent
# - Index chunks.jsonl for RAG retrieval
# - Share docs.md with your team
```

## Output Files Explained

### tools.json
Complete JSON Schema tool definitions with HTTP metadata:

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
      "parameters": {...},
      "returns": {...},
      "x-http": {
        "method": "GET",
        "path_template": "/list.json",
        "arg_mapping": {},
        "auth_required": false
      },
      "examples": {"curl": "..."}
    }
  ]
}
```

### docs.md
Clean markdown documentation:

```markdown
# APIs.guru
**Version:** 2.2.0

## Base URLs
- https://api.apis.guru/v2

## Authentication
- None required

## Endpoints

#### `listapis`
**GET** `/list.json`
*List all APIs*

**Example:**
\`\`\`bash
curl -X GET 'https://api.apis.guru/v2/list.json'
\`\`\`
```

### chunks.jsonl
One JSON object per line for RAG:

```json
{"id":"listapis","tag":"listapis","method":"GET","path":"/list.json","text":"List all APIs Returns object.","meta":{"required":[],"auth":false}}
```

## What Gets Processed

✅ **Dereferenced schemas** - All `$ref` pointers resolved  
✅ **Auth requirements** - apiKey, bearer, oauth2 normalized  
✅ **Base URLs** - Server URLs surfaced  
✅ **Path/query/header params** - All mapped to HTTP locations  
✅ **Request bodies** - JSON/multipart/form schemas extracted  
✅ **Response schemas** - Success responses documented  
✅ **Pagination** - Automatically detected patterns  
✅ **Error codes** - 4xx/5xx responses listed  
✅ **Curl examples** - Generated with placeholder values  

## Integration Examples

### Load in Python

```python
import json

# Load tools
with open('output/tools.json') as f:
    api = json.load(f)

# Iterate tools
for tool in api['tools']:
    print(f"{tool['name']}: {tool['x-http']['method']} {tool['x-http']['path_template']}")
```

### Index chunks for RAG

```python
import json

chunks = []
with open('output/chunks.jsonl') as f:
    for line in f:
        chunk = json.loads(line)
        # Embed chunk['text'] with your embedding model
        # Store with chunk['id'] for retrieval
        chunks.append(chunk)

print(f"Indexed {len(chunks)} endpoints")
```

### Use with OpenAI function calling

```python
import json

with open('output/tools.json') as f:
    api = json.load(f)

# Convert to OpenAI function format
functions = []
for tool in api['tools']:
    functions.append({
        "name": tool['name'],
        "description": tool['description'],
        "parameters": tool['parameters']
    })

# Use with OpenAI API
# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[...],
#     functions=functions
# )
```

## Common Issues

### "No such file or directory"
Make sure the input file path is correct:
```bash
python3 new_main.py /full/path/to/openapi.yaml
```

### "Object of type datetime is not JSON serializable"
This has been fixed - update to the latest version of `new_main.py`.

### "Missing required fields"
Your OpenAPI spec might be invalid. Validate it first:
```bash
# Use an OpenAPI validator like swagger-cli
npm install -g @apidevtools/swagger-cli
swagger-cli validate openapi.yaml
```

## Next Steps

- **Read** `USAGE_EXAMPLE.md` for detailed examples
- **Check** `IMPLEMENTATION_STATUS.md` for feature coverage
- **Refer to** `new_instructions.md` for the design blueprint
- **Run** `test.py` to validate your output

## Help & Support

For issues or questions:
1. Check `IMPLEMENTATION_STATUS.md` for known limitations
2. Validate your OpenAPI spec is well-formed
3. Try with the example: `python3 new_main.py ../APIs.guru-swagger.json`

## Performance

Typical processing times:
- Small APIs (1-10 endpoints): <1 second
- Medium APIs (10-50 endpoints): 1-3 seconds  
- Large APIs (50-100 endpoints): 3-10 seconds

Memory usage scales with spec complexity (dereferencing depth).

