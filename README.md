# API Ingest - Let LLMs work with APIs 

**Handy tool** that converts API specs (OpenAPI YAML/JSON, RAML, WSDL, GraphQL, API Blueprint) into structured, LLM-friendly markdown optimized for codegen agents. 

[![Deploy to Koyeb](https://img.shields.io/badge/Deploy%20to-Koyeb-blue)](https://www.koyeb.com/)

> *"AGGH 400, not again"*

Friday night. You finally have a peaceful moment to code your dream project — a cornflakes restock alert machine. You spin up Claude Code, the frontend looks great, but then your agent hits the Costco API and just... can't. 400 Bad requests everywhere. You tell it to read the docs. It scrapes 2 of 20 pages, gives up, and enters a confident hallucination loop.

API endpoint hallucination is one of the most common failure modes when building applications with agents. And the existing workarounds all kinda suck:

|  | Manual Spec Upload | Agent Web Search | Context7 | **API Ingest** |
|---|---|---|---|---|
| Structured for LLMs | ❌ raw schema with `$ref`s | ❌ scraped HTML | ❌ raw markdown dump | ✅ optimized format |
| Accuracy | ✅ | ❌ loops & misses pages | ❌ semantic search | ✅ deterministic search|
| Token efficient | ❌ full spec in context | ❌ bloated page scrapes | ✅ chunks (⚠️but noisy) | ✅ lazy loaded chunks |
| Self-contained chunks | ❌ | ❌ | ⚠️ | ✅ each chunk stands alone |
| Endpoint-level precision | ❌ | ❌ | ❌ | ✅ lookup by operationId / tag |
| Zero manual effort | ❌ find & paste spec | ✅ | ✅ | ✅ |

**API Ingest** takes OpenAPI specs and deterministically transforms them into LLM-optimized, chunked markdown — so your agent gets exactly the endpoint it needs, with auth, params, schemas, and curl examples baked in. 
Without `$ref` mayhem, no "lost in the middle", no hallucination loops. Available as MCP server, web UI, or CLI.

> *YES! This tool should die the day every API provider outside of big tech offers LLM-friendly docs, ([e.g. via this](https://gitbook.com/docs/publishing-documentation/mcp-servers-for-published-docs)). But let's be honest — that's gonna take a while. Until then, happy ingesting 💉.*

## ✨ Features

### Converter
- **Three output modes** — Monolithic markdown, chunked JSON (progressive disclosure), and JSON Schema tool definitions
- **Stable `operationId` anchors** — Each endpoint block includes its `operationId` for deterministic lookup
- **Self-contained endpoint blocks** — Base URL, auth, params, schemas, and curl example repeated per block so each chunk stands alone
- **Dereferences `$ref` schemas** — Inline references for readability
- **Runnable curl examples** — Auto-generated with auth placeholders
- **Strict separators** — Gitingest-style `====` delimiters prevent boundary confusion
- **Tag grouping** — Organized by tags, alphabetically sorted
- **Type normalization** — Clean type display (`string (uuid)`, `array<User>`, etc.)
- **Token-aware** — Endpoint blocks target 2-4K tokens

### MCP Server (in work 🛠️)
- **Progressive disclosure** — Manifest, tags, endpoints, and schemas exposed as individually addressable MCP resources
- **On-the-fly conversion** — `convert_spec` and `convert_spec_to_tools` MCP tools for specs not stored in the DB
- **Content-hash caching** — Avoids re-converting the same spec on repeated resource requests

### Web UI
- **Tabbed spec explorer** — Overview, Chunks, Tool Schemas, and Full Markdown tabs
- **Searchable chunk browser** — Filter endpoints and schemas by name within the Chunks tab
- **Copy-friendly tool schemas** — Expandable JSON with one-click copy

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/mohidbt/apic.git
cd apic

# Terminal 1 - Start Backend
cd backend
pip install -r requirements.txt
python main.py

# Terminal 2 - Start Frontend
cd frontend
npm install
npm run dev
```

Then open http://localhost:3000 in your browser!

### Using the Converter

1. **Web Interface** (Recommended)
   - Open http://localhost:3000
   - Drag and drop your API spec file (YAML, JSON, RAML, WSDL, GraphQL, or API Blueprint)
   - Click "Convert to Markdown"
   - Browse chunks, tool schemas, and full markdown in the spec detail modal

2. **Command Line**
   ```bash
   cd backend

   # Monolithic markdown (default)
   python transformation.py spec.yaml

   # Progressive-disclosure chunks as JSON
   python transformation.py spec.yaml --chunked

   # JSON Schema tool definitions for function-calling
   python transformation.py spec.yaml --tools
   ```

3. **API Endpoints**
   ```bash
   # Convert and download markdown
   curl -X POST http://localhost:8000/api/convert \
     -F "file=@openapi-spec.yaml"

   # Get chunked output for a stored spec
   curl http://localhost:8000/api/specs/1/chunks

   # Get tool schemas for a stored spec
   curl http://localhost:8000/api/specs/1/tools
   ```

## 📁 Project Structure

```
├── backend/                    # FastAPI + MCP server
│   ├── main.py                # API server (convert, specs CRUD, chunks, tools)
│   ├── transformation.py      # Core OpenAPI → Markdown/Chunks/Tools converter
│   ├── mcp_server.py          # MCP server exposing specs as resources + tools
│   ├── models/                # SQLAlchemy models (ApiSpec, database setup)
│   ├── crud/                  # Database query helpers
│   ├── schemas/               # Pydantic response schemas
│   ├── tests/                 # pytest suite (transformation, behavioral, robustness)
│   ├── scripts/               # Import utilities
│   └── requirements.txt
├── frontend/                   # Next.js web application
│   ├── src/
│   │   ├── app/               # App router pages (marketplace, spec detail)
│   │   ├── components/        # UI components (spec-detail-modal, etc.)
│   │   ├── lib/               # API client (fetchSpecChunks, fetchSpecTools)
│   │   └── types/             # TypeScript types (ChunkedSpec, ToolSchema)
│   └── package.json
├── examples/                   # Example OpenAPI specifications
├── docs/                       # Setup, deployment, and reference guides
└── README.md
```

## 📖 Output Format

The generated markdown follows a strict, LLM-optimized structure:

### Header Section
```markdown
# API Title
**Version:** 1.0.0

Brief description...

## Base URLs
  - https://api.example.com — Production
  - https://sandbox.api.example.com — Sandbox

## Authentication
  - bearerAuth: HTTP BEARER
  - apiKey: API Key (header: X-API-Key)
```

### Endpoint Blocks

Each endpoint uses strict delimiters (inspired by Gitingest) and is fully self-contained:

```
================================================================================
ENDPOINT: [GET] /users/{id}
OPERATION_ID: getUserById
BASE_URL: https://api.example.com
TAGS: Users
SUMMARY: Get a user by ID
DESCRIPTION: Retrieves detailed user information...
AUTH: BEARER token

REQUEST
  Path params:
  - id (string (uuid), required)
  Query params:
  - verbose (boolean, optional)
  Body:
  none

RESPONSES
  - 200 (application/json): Success
    - id: string (uuid, required)
    - name: string (required)
    - email: string (email, required)
  - 404: User not found

EXAMPLE (curl)
curl -X GET \
  "https://api.example.com/users/123?verbose=true" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
```

`OPERATION_ID` is the stable key used for chunked output, MCP resource URIs, and tool schema names. `BASE_URL` is repeated per block so each chunk stands alone without referencing the header.

## 🎯 Why This Format?

### LLM Benefits

1. **Strict Delimiters** — `=` bars prevent AI from confusing endpoint boundaries
2. **Self-contained blocks** — Each endpoint includes its own base URL and auth, so a single retrieved chunk has everything needed to construct a request
3. **Stable IDs** — `OPERATION_ID` provides a deterministic key for lookup, tool schemas, and MCP URIs
4. **Dereferenced Schemas** — No need to chase `$ref` pointers during code generation
5. **Progressive Disclosure** — Chunked output lets agents fetch manifest first, then only the endpoints they need (avoids "lost in the middle")
6. **Tool Schema Parity** — `generate_tool_schemas()` produces JSON Schema definitions that match the docs 1:1, so docs and callable tools stay isomorphic
7. **Token-Optimized** — Endpoint blocks target 2-4K tokens; agents never need to ingest the whole spec

### Inspired by Gitingest

This format borrows from [Gitingest](https://gitingest.com/)'s approach:
- Three-section structure (header, TOC, content)
- Repeated delimiters between entries
- Stable, deterministic ordering
- Noise filtering for clarity

## 🔌 MCP Server

The MCP server (`backend/mcp_server.py`) exposes stored API specs as discoverable resources and tools, implementing the progressive-disclosure pattern so agents spend minimal tokens.

### Resources

| URI | Description |
|-----|-------------|
| `docs://specs` | List all stored specs (id, name, version, token count) |
| `docs://specs/{id}/manifest` | Title, version, base URLs, auth, tag-grouped endpoint index |
| `docs://specs/{id}/tags/{tag}` | Per-tag endpoint listing with operationIds and summaries |
| `docs://specs/{id}/endpoints/{operationId}` | Full self-contained endpoint block |
| `docs://specs/{id}/schemas/{name}` | Single component schema definition |
| `docs://specs/{id}/tools` | JSON tool definitions for all endpoints |

### Tools

| Tool | Description |
|------|-------------|
| `convert_spec` | Convert raw OpenAPI YAML/JSON to chunked markdown on the fly |
| `convert_spec_to_tools` | Convert raw OpenAPI spec to JSON Schema tool definitions |

### Running the MCP server

The MCP server runs as a remote HTTP service with bearer-token authentication.

```bash
cd backend

# HTTP transport (production / remote clients)
MCP_API_TOKEN=your-secret-token python mcp_server.py
# Listens on 0.0.0.0:8080 by default — configurable via MCP_HOST / MCP_PORT

# stdio transport (local development / debugging)
MCP_TRANSPORT=stdio python mcp_server.py
```

| Env Var | Default | Description |
|---------|---------|-------------|
| `MCP_TRANSPORT` | `streamable-http` | `streamable-http` or `stdio` |
| `MCP_HOST` | `0.0.0.0` | Bind address for HTTP transport |
| `MCP_PORT` | `8080` | Listen port for HTTP transport |
| `MCP_API_TOKEN` | *(required for HTTP)* | Bearer token clients must send |

### Connecting clients

**Cursor** — add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "APIIngest": {
      "url": "https://your-deployed-host:8080/",
      "headers": {
        "Authorization": "Bearer your-secret-token"
      }
    }
  }
}
```

**Claude Code** — run:

```bash
claude mcp add --transport http APIIngest https://your-deployed-host:8080/ \
  --header "Authorization: Bearer your-secret-token"
```

An agent workflow typically looks like: fetch manifest (small) -> pick relevant endpoint by operationId -> fetch only that endpoint block. This avoids dumping the entire spec into context.

## 🌐 Deployment

### Deploy to Koyeb

**Two deployment options:**

#### Option 1: Single Service (Recommended for Simple Deployments)
Deploy backend + frontend together in one container.

See **[KOYEB_SINGLE_SERVICE.md](KOYEB_SINGLE_SERVICE.md)** for detailed instructions.

**Quick steps:**
1. Use root-level `Dockerfile`
2. Set environment variables (PORT, ALLOWED_ORIGINS, etc.)
3. Deploy as one service
4. Both services run together via supervisord

**Environment Variables:**
```bash
PORT=8000
ALLOWED_ORIGINS=https://{{ KOYEB_PUBLIC_DOMAIN }}/
NEXT_PUBLIC_API_URL=http://localhost:8000
NODE_ENV=production
```

#### Option 2: Two Separate Services (Recommended for Production)
Deploy backend and frontend as independent services.

See **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** for complete instructions.

**Quick Overview:**
1. Deploy backend service (FastAPI) from `backend/` directory
2. Deploy frontend service (Next.js) from `frontend/` directory
3. Set environment variables for both services
4. Update CORS settings with deployed URLs

## 🛠️ Technology Stack

### Backend
- **FastAPI** — Modern Python web framework
- **uvicorn** — ASGI server
- **PyYAML** — YAML parsing
- **MCP Python SDK** — Model Context Protocol server
- **tiktoken** — Token counting
- **Python 3.10+**

### Frontend
- **Next.js 15** — React framework
- **TypeScript** — Type safety
- **Tailwind CSS** — Styling
- **shadcn/ui** — UI components
- **Sonner** — Toast notifications

## 📚 Documentation

- **[SETUP.md](docs/SETUP.md)** — Detailed installation and configuration
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** — Koyeb deployment guide
- **[QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)** — Command reference
- **[Backend README](backend/README.md)** — API documentation
- **[Examples](examples/README.md)** — Example specifications

## 🧪 Testing

```bash
cd backend

# Run the full test suite
pytest tests/ -v

# Run specific test tiers
pytest tests/test_transformation.py -v    # Core converter logic
pytest tests/test_p1_behavioral.py -v     # Behavioral edge cases (allOf, security overrides, etc.)
pytest tests/test_p2_robustness.py -v     # Robustness (empty specs, perf guards, special chars)
```

The test suite covers monolithic, chunked, and tool-schema outputs, verifying cross-format consistency (same spec produces matching operationIds and endpoints across all three modes).

To try the converter manually:

```bash
python transformation.py ../examples/APIs.guru-swagger.yaml
```

## 🤝 Contributing

Contributions welcome! This project prioritizes LLM readability over human aesthetics.

**Key principles:**
1. **Strict structure** — Consistent delimiters and ordering
2. **Inline critical info** — Auth, types, examples per endpoint
3. **Token efficiency** — Truncate where necessary
4. **Deterministic output** — Same input = same output

## 📝 License

MIT — Feel free to use, modify, and distribute.

## 🔗 Related Projects

- [Gitingest](https://gitingest.com/) — LLM-optimized code repository digests

## 💡 Use Cases

- **AI Coding Assistants** — Feed API docs to Claude, GPT, etc.
- **MCP-connected agents** — Agents discover and fetch only the endpoints they need via the MCP server
- **Function-calling / tool use** — Generate JSON Schema tool definitions directly from any OpenAPI spec
- **RAG Systems** — Token-optimized chunks with natural split boundaries for retrieval
- **Developer Onboarding** — Clear, structured API references

## 🐛 Issues & Support

Found a bug or have a question?
- Open an issue on GitHub
- Check existing [documentation](docs/)
- Try with [example files](examples/)

## 🎉 Acknowledgments

Built with inspiration from:
- Gitingest's LLM-friendly formatting approach
- OpenAPI Specification community
- Context7 package versioning service for LLMs

---

**Made with ❤️ for developers working with LLMs**
