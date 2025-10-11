# OpenAPI to Agent Artifacts Converter

A rudimentary script to transform OpenAPI YAML/JSON specifications into LLM-friendly artifacts.

## What it does

Converts OpenAPI specs into **three output files**:

1. **`tools.json`** - Machine-readable tool/function specs for AI agents (JSON Schema format)
2. **`docs.md`** - Human-readable markdown reference for prompting and RAG
3. **`chunks.jsonl`** - Compact retrieval chunks (one per endpoint) for fast context injection

## Features

✅ **Dereferences** `$ref` schemas with cycle detection  
✅ **Flattens** `allOf` schemas  
✅ **Normalizes** authentication (apiKey, bearer, oauth2)  
✅ **Detects** pagination patterns (limit/offset, cursor, page-based)  
✅ **Generates** runnable curl examples  
✅ **Synthesizes** unique operation names  
✅ **Surfaces** base URLs, auth requirements, and rate limit headers  
✅ **Groups** endpoints by tag for better organization  

## Usage

```bash
python3 new_main.py <input-file> [--out <output-dir>] [--server-index <N>]
```

### Examples

```bash
# Basic usage - outputs to ./output/
python3 new_main.py ../APIs.guru-swagger.json

# Custom output directory
python3 new_main.py api-spec.yaml --out ./my-api-docs

# Use a different server (if multiple servers defined)
python3 new_main.py api-spec.yaml --server-index 1
```

## Output Structure

```
output/
├── tools.json      # Full tool definitions with JSON Schema
├── docs.md         # Human-readable markdown docs
└── chunks.jsonl    # RAG-ready chunks (400-800 chars each)
```

## Requirements

- Python 3.8+
- PyYAML (for YAML input files)

```bash
pip install PyYAML>=6.0.1
```

## Design

Based on the blueprint in `new_instructions.md`, this implementation:

- **Single `parameters` object** per endpoint (friendlier for function-calling agents)
- **`x-http.arg_mapping`** preserves HTTP placement info (path/query/header/body)
- **Pagination block** standardizes common pagination patterns
- **Schema pruning** only includes referenced schemas in components
- **Deterministic naming** with deduplication for operation names

## Limitations

This is a **rudimentary** implementation focused on core functionality:

- Basic error handling
- Simplified oneOf/anyOf handling (picks first option)
- No advanced CLI flags yet (--keep-oneof, --no-prune, etc.)
- No streaming for huge specs
- No golden tests yet

## Examples

See `test-output/` for sample output from the APIs.guru spec.

## Development Roadmap

See `new_instructions.md` for the full TODO list of features to implement.

