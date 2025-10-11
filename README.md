# OpenAPI to LLM-Ready Markdown Converter

Convert OpenAPI YAML/JSON specifications into structured, LLM-friendly markdown format optimized for AI coding assistants.

## Features

✅ **Dereferences `$ref` schemas** — Inline references for readability  
✅ **Surfaces authentication** — Security schemes pulled into each endpoint  
✅ **Base URLs highlighted** — Server information prominently displayed  
✅ **Runnable examples** — Auto-generated curl commands with placeholders  
✅ **Strict separators** — Gitingest-style delimiters prevent boundary confusion  
✅ **Tag grouping** — Organized by tags, alphabetically sorted  
✅ **Type normalization** — Clean type display (string (uuid), array<User>, etc.)  
✅ **Noise removal** — Filters out vendor extensions (x-*) and unused components  
✅ **Token-aware** — Designed to keep endpoint chunks under 2-4K tokens  

## Installation

```bash
# Install dependencies (if needed)
pip3 install -r requirements.txt
```

## Usage

### Basic Conversion

```bash
# Convert OpenAPI file to markdown (auto-names output)
python3 main.py openapi-spec.yaml

# Specify custom output path
python3 main.py openapi-spec.yaml api-reference.md

# Works with JSON too
python3 main.py swagger.json api-docs.md

# Or make it executable
chmod +x main.py
./main.py openapi-spec.yaml
```

### Example

```bash
python3 main.py APIs.guru-swagger.json
# Output: APIs.guru-swagger.md
```

## Output Format

The generated markdown follows a strict, LLM-optimized structure:

### Header Section
```
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

### Table of Contents
```
## Endpoints by Tag

### Users
- **GET** `/users` — List all users
- **GET** `/users/{id}` — Get user by ID
- **POST** `/users` — Create new user
```

### Endpoint Blocks

Each endpoint uses strict delimiters (inspired by Gitingest's file separation):

```
================================================================================
ENDPOINT: [GET] /users/{id}
TAGS: Users
SUMMARY: Get a user by ID
DESCRIPTION: Retrieves detailed user information...
AUTH: Bearer token

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
    - created_at: string (date-time, required)
  - 404: User not found

EXAMPLE (curl)
curl -X GET \
  "https://api.example.com/users/123?verbose=true" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
```

### Components Appendix

Shared schemas are collected at the end:

```
================================================================================
## COMPONENTS APPENDIX
================================================================================

Shared schemas referenced throughout the API:

### User
Type: object
Description: User account model

- id: string (uuid, required)
- name: string (required)
- email: string (email, required)
- role: string (enum: admin, user, guest) (required)
```

## Why This Format?

### LLM Benefits

1. **Strict Delimiters** — `=` bars prevent the AI from confusing endpoint boundaries
2. **Dereferenced Schemas** — No need to chase `$ref` pointers during code generation
3. **Inline Auth** — Security requirements visible per-endpoint, not hidden in components
4. **Runnable Examples** — Copy-paste curl commands with placeholder variables
5. **Normalized Types** — Consistent type display helps pattern recognition
6. **Tag Grouping** — Logical organization mimics how developers think
7. **Token-Optimized** — Chunks designed to fit in context windows

### Inspired by Gitingest

This format borrows from [Gitingest](https://gitingest.com/)'s approach:
- Three-section structure (header, TOC, content)
- Repeated delimiters between entries
- Stable, deterministic ordering
- Noise filtering for clarity

## Advanced Features

### Schema Dereferencing

The script automatically resolves `$ref` pointers up to 3 levels deep:

```yaml
# Before (OpenAPI)
schema:
  $ref: "#/components/schemas/User"

# After (Markdown)
- id: string (uuid, required)
- name: string (required)
- email: string (email, required)
```

### Type Normalization

Types are enhanced with format and constraint info:

- `string` → `string`
- `string` + `format: uuid` → `string (uuid)`
- `string` + `enum: [a, b, c]` → `string (enum: a, b, c)`
- `array` + `items: User` → `array<User>`
- `object` + `properties: {...}` → `object (5 fields)`

### Example Generation

Curl examples use:
1. Spec's `example` values when available
2. Smart placeholders otherwise (123 for IDs, "example" for strings)
3. Environment variable style for auth (`$TOKEN`, `$API_KEY`)

### Security Schemes

All security types are supported:
- **API Key** — Header/query/cookie-based keys
- **HTTP Auth** — Basic, Bearer, etc.
- **OAuth2** — With flow types and scopes
- **OpenID Connect**

## Token Management

The format is designed to keep individual endpoint chunks under 2-4K tokens:
- Long descriptions truncated to 200 chars
- Schema depth limited to 3 levels
- Large enums show first 5 values + "..."
- Components moved to appendix

## Project Structure

```
.
├── main.py              # Main conversion script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── APIs.guru-swagger.json  # Example OpenAPI spec
└── *.md                # Generated markdown files
```

## Example Output

Run the converter on the included example:

```bash
python3 main.py APIs.guru-swagger.json
```

This generates `APIs.guru-swagger.md` with:
- 📄 ~100 lines of header/TOC
- 🎯 Endpoint blocks with strict separators
- 📚 Components appendix with shared schemas
- ✨ Runnable curl examples for every endpoint

## License

MIT — Feel free to use, modify, and distribute.

## Contributing

Contributions welcome! This script prioritizes LLM readability over human aesthetics.

Key principles:
1. **Strict structure** — Consistent delimiters and ordering
2. **Inline critical info** — Auth, types, examples per endpoint
3. **Token efficiency** — Truncate where necessary
4. **Deterministic output** — Same input = same output

## Related Projects

- [Gitingest](https://gitingest.com/) — LLM-optimized code repository digests
- [OpenAPI Generator](https://openapi-generator.tech/) — Code generation from OpenAPI
- [Swagger UI](https://swagger.io/tools/swagger-ui/) — Human-readable API docs

