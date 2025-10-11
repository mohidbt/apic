# Quick Start Guide

Get up and running in 30 seconds.

## TL;DR

```bash
# Convert your OpenAPI spec
python3 main.py your-api-spec.yaml

# Output: your-api-spec.md (ready for LLM consumption)
```

## Common Commands

```bash
# Basic conversion (auto-names output)
python3 main.py api.yaml

# Custom output name
python3 main.py api.yaml my-api-reference.md

# Works with JSON too
python3 main.py swagger.json

# Make executable (one-time setup)
chmod +x main.py
./main.py api.yaml
```

## What You Get

Input: `api.yaml` (your OpenAPI spec)  
Output: `api.md` (LLM-optimized markdown)

The output includes:
- ✅ Header with base URLs and auth schemes
- ✅ Table of contents grouped by tag
- ✅ Detailed endpoint blocks with strict separators
- ✅ Dereferenced schemas (no `$ref` chasing)
- ✅ Runnable curl examples for every endpoint
- ✅ Components appendix for shared schemas

## Use Cases

### 1. AI Coding Assistant Context

**Cursor, GitHub Copilot, Claude Code, etc.**

```bash
# Convert your API spec
python3 main.py company-api.yaml

# Then in your AI chat:
# "Using the endpoints in company-api.md, write a client 
# that fetches all users and creates a new one"
```

The AI will have complete context including types, auth, and examples.

### 2. RAG System Ingestion

**LlamaIndex, LangChain, etc.**

```bash
# Convert API to markdown
python3 main.py large-api.yaml api-reference.md

# Chunk the output by endpoint (using the === separators)
# Feed chunks into your vector database
```

Each endpoint block is self-contained and token-efficient.

### 3. Prompt Engineering

**Few-shot examples, function calling schemas**

```bash
python3 main.py api.yaml

# Extract specific endpoints for prompt examples
# The strict format makes parsing easy
```

### 4. Documentation Generation

**For AI-assisted docs writing**

```bash
python3 main.py api.yaml api-ref.md

# Feed to AI: "Convert this API reference into user-friendly 
# documentation with code examples in Python, JavaScript, and Go"
```

## File Locations

After running the script:

```
your-project/
├── main.py              # The converter script
├── requirements.txt     # Dependencies (just PyYAML)
├── api.yaml            # Your OpenAPI spec (input)
└── api.md              # Generated markdown (output)
```

## Troubleshooting

### "command not found: python"

Use `python3` instead:
```bash
python3 main.py api.yaml
```

### "No module named 'yaml'"

Install dependencies:
```bash
pip3 install -r requirements.txt
```

### "File not found"

Make sure you're in the right directory:
```bash
cd /path/to/your/project
python3 main.py api.yaml
```

### Large output file

This is normal for big APIs. The format is token-efficient:
- Each endpoint: ~200-500 tokens
- 50 endpoints: ~25K tokens (fits in most LLM contexts)

## Advanced Usage

### Custom Output Location

```bash
python3 main.py api.yaml docs/api-reference.md
```

### Batch Processing

```bash
# Convert multiple specs
for file in specs/*.yaml; do
  python3 main.py "$file"
done
```

### Integration with Scripts

```python
from main import OpenAPIToMarkdown

converter = OpenAPIToMarkdown('api.yaml', 'output.md')
markdown = converter.convert()
converter.save(markdown)

# Or just get the markdown string
print(markdown[:500])  # Preview first 500 chars
```

## Example Output Preview

Your converted markdown will look like this:

```markdown
# Your API Name
**Version:** 1.0.0

## Base URLs
  - https://api.example.com

## Authentication
  - bearerAuth: HTTP BEARER

## Endpoints by Tag

### Users
- **GET** `/users` — List all users
- **POST** `/users` — Create new user

## Endpoint Details

================================================================================
ENDPOINT: [GET] /users
TAGS: Users
SUMMARY: List all users
AUTH: BEARER token

REQUEST
  Query params:
  - limit (integer, optional)

RESPONSES
  - 200 (application/json): Success
    array<User>

EXAMPLE (curl)
curl -X GET \
  "https://api.example.com/users?limit=20" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
```

## Next Steps

1. **Convert your API**: `python3 main.py your-spec.yaml`
2. **Test with LLM**: Feed the output to your AI coding assistant
3. **Iterate**: Adjust the script if needed (see `main.py`)

## Questions?

- 📖 See `EXAMPLES.md` for detailed before/after comparisons
- 📚 See `README.md` for full documentation
- 🔧 Edit `main.py` to customize output format

---

**Pro tip**: Keep both the original OpenAPI spec and the generated markdown in your repo. The markdown is for AI consumption, the spec is for tooling (Swagger UI, code generators, etc.).

