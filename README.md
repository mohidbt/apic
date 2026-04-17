# API Ingest - Let Agents work with boring APIs 

**Handy tool** that converts API specs (OpenAPI YAML/JSON, RAML, WSDL, GraphQL, API Blueprint) into structured, LLM-friendly markdown optimized for codegen agents. 

> *"AGGH 400, not again"*

Friday night. You finally have a peaceful moment to code your dream project — a cornflakes restock alert machine. You spin up Claude Code, the frontend looks great, but then your agent hits the Costco API and fails. 400 Bad requests everywhere. You tell it to read the docs online. It scrapes 5 of 20 pages, then enters a confident hallucination loop.

API endpoint hallucination is one of the most common failures when building API-based software with agents. And the existing workarounds kinda suck:

|  | Manual Spec Upload | Agent Web Search | Context7 | **API Ingest** |
|---|---|---|---|---|
| Structured for LLMs | ❌ raw schema with `$ref`s | ❌ scraped HTML | ❌ raw markdown dump | ✅ optimized format |
| Accuracy | ⚠️ all info in context (but degradation with bigger specs) | ❌ loops & misses pages | ❌ semantic search | ✅ deterministic search|
| Token efficient | ❌ full spec in context | ❌ bloated page scrapes | ✅ chunks (⚠️but noisy) | ✅ lazy loaded chunks |
| Endpoint-level precision | ❌ | ❌ | ❌ | ✅ lookup by operationId / tag |
| Zero manual effort | ❌ find & paste spec | ✅ | ✅ | ✅ |

**API Ingest** takes OpenAPI specs and deterministically transforms them into LLM-optimized, chunked markdown — so your agent gets exactly the endpoint it needs, with auth, params, schemas, and curl examples baked in. 
Available as MCP server, web UI, or CLI.

> *YES! This tool should die the day every API provider outside of big tech offers LLM-friendly docs, ([e.g. via this](https://gitbook.com/docs/publishing-documentation/mcp-servers-for-published-docs)). But let's be honest — that's gonna take a while. Until then, happy ingesting 💉.*


<p align="center">
  <img src="assets/header.jpg" alt="API Ingest" width="600" />
</p>

---

### Connect to MCP server

**Claude Code:**

```bash
claude mcp add --transport http API-Ingest https://api-ingest.com/mcp \
  --header "Authorization: Bearer YOUR_TOKEN"
```

**Cursor** — add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "API-Ingest": {
      "url": "https://api-ingest.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```
Get the token from api-ingest.com

**Optional env var (self-hosted):**

| Variable | Default | Description |
| --- | --- | --- |
| `MCP_TOKEN_THRESHOLD` | `4000` | Token count above which `full_markdown` is omitted and only `manifest` + `chunks_available` are returned |

---

### What your agent can do

| Tool | What it does |
| --- | --- |
| `convert_spec` | Convert a raw spec (OpenAPI, RAML, GraphQL, etc.) into chunked, LLM-optimized markdown |
| `search_specs` | Search the marketplace for public API specs by name or tag |
| `load_spec` | Load a marketplace spec into the same smart-loading payload |
| `get_chunk` | Fetch a single endpoint, tag, or schema — self-contained, no full spec needed |

**How agents use it:**

1. `convert_spec` (local file) or `search_specs` → `load_spec` (marketplace)
2. Check `token_count` against `token_threshold` (default **4000 tokens**) — if small, use `full_markdown` directly
3. If large — read the manifest, then `get_chunk` for only the endpoints needed

Each chunk includes its own base URL, auth, params, schemas, and a curl example — so it stands alone without the rest of the spec.

---

### Web UI

Use the hosted web tool at **[api-ingest.com](https://api-ingest.com)** to convert specs interactively:

1. Drop an API spec file (YAML, JSON, RAML, WSDL, GraphQL, or API Blueprint)
2. Browse chunks, tool schemas, and full markdown in the explorer
3. Copy what you need

---

### Output format

The converter produces strict, deterministic markdown with self-contained endpoint blocks:

```
================================================================================
ENDPOINT: [GET] /users/{id}
OPERATION_ID: getUserById
BASE_URL: https://api.example.com
TAGS: Users
AUTH: BEARER token

REQUEST
  Path params:
  - id (string (uuid), required)

RESPONSES
  - 200 (application/json): Success
    - id: string (uuid, required)
    - name: string (required)
  - 404: User not found

EXAMPLE (curl)
curl -X GET "https://api.example.com/users/123" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
```

`OPERATION_ID` is the stable key for chunk lookups. `BASE_URL` is repeated per block so each chunk is fully self-contained. `====` delimiters prevent boundary confusion during retrieval.

---

### Why this format?

- **Self-contained blocks** — each chunk has everything needed to construct a request
- **No `$ref` chasing** — schemas are dereferenced inline
- **Stable IDs** — deterministic `operationId` keys for lookup and tool schemas
- **Token-optimized** — blocks target 2-4K tokens; agents never ingest the whole spec
- **Progressive disclosure** — manifest first, then fetch only what's needed

Inspired by [Gitingest](https://gitingest.com/)'s LLM-efficient formatting.

---

### Documentation

- [Quickstart](QUICKSTART.md) - get backend + frontend running quickly
- [Setup](docs/SETUP.md) - full local development setup
- [Deployment](docs/DEPLOYMENT.md) - production deployment guidance

---

### Contributing

Contributions welcome. 

```bash
git clone https://github.com/mohidbt/api-ingest.git
cd api-ingest/backend
pip install -r requirements.txt
pytest tests/ -v
```

[MIT License](LICENSE)
