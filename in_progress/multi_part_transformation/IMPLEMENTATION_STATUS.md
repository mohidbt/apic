# Implementation Status

This document tracks what has been implemented from `new_instructions.md`.

## ✅ Completed Features

### A. Parsing & normalization
- ✅ Accept `.yaml|.yml|.json` files
- ✅ Parse OpenAPI 3.0/3.1
- ✅ **Dereference** all `$ref` with cycle detection
- ✅ **Flatten** `allOf` (merge schemas)
- ✅ Handle datetime objects from YAML parsing
- ✅ Choose default **server** (first https or first available)
- ✅ Normalize types to JSON Schema Draft-07

### B. Auth extraction
- ✅ Read `components.securitySchemes`
- ✅ Normalize to: `apiKey|bearer|basic|oauth2`
- ✅ Extract OAuth2 scopes per operation
- ✅ Compute `auth_required` per operation

### C. Operation synthesis
- ✅ Build unique **operation name** (prefer `operationId`, else synthesize)
- ✅ Merge path-level & operation-level **parameters**
- ✅ Create **`parameters` JSON Schema object** with properties + required
- ✅ Build **`x-http.arg_mapping`** mapping properties to HTTP locations
- ✅ Extract **requestBody** (prefer JSON, then multipart, then form)
- ✅ Extract **returns** (pick canonical 2xx, prefer JSON)
- ✅ Build **errors** list from 4xx/5xx
- ✅ Generate concise **description** (trimmed to 160 chars)
- ✅ Generate **curl examples** with synthesized values

### D. Pagination heuristics
- ✅ Inspect parameters for `limit/offset/page/per_page/cursor/token`
- ✅ Inspect response schema for pagination hints
- ✅ Emit standardized `pagination` block

### E. Schema pruning & carry-over
- ✅ Track schemas used by `request_body`/`returns`
- ✅ Only include referenced schemas in components

### F. Output writers
- ✅ Emit **`tools.json`** (deterministic, sorted by path)
- ✅ Emit **`docs.md`** with index, tables, and endpoint cards
- ✅ Emit **`chunks.jsonl`** with compressed text (400-800 chars)

### G. CLI & config
- ✅ CLI: `python3 new_main.py INPUT.(yaml|json) --out outdir --server-index N`
- ✅ Flag: `--server-index` to choose server
- ✅ Flag: `--out` to specify output directory

### H. Robustness
- ✅ Deterministic name de-dupe (`pets_list`, `pets_list_2`)
- ✅ Handle datetime objects in YAML
- ✅ Cycle detection in $ref resolution

### I. Tests
- ✅ Basic validation test suite (`test.py`)
- ✅ Validates all path params appear in `arg_mapping`
- ✅ Validates required params are in properties
- ✅ Validates chunk text size limits (≤800 chars)
- ✅ Validates JSON Schema structure

## 🔄 Partially Implemented

### B. Auth extraction
- ⚠️ Only uses first security scheme (doesn't handle multiple schemes)
- ⚠️ OAuth2 scopes limited to first 10

### C. Operation synthesis
- ⚠️ `oneOf/anyOf` handling is basic (picks first option, doesn't record alternates)
- ⚠️ Request body for form-data is not fully tested

### D. Pagination heuristics
- ⚠️ Link header pagination not detected yet
- ⚠️ Heuristics may miss custom pagination patterns

### E. Schema pruning
- ⚠️ Doesn't inline tiny schemas (keeps all in components)
- ⚠️ Doesn't detect unused nested schemas

## ❌ Not Yet Implemented

### A. Parsing & normalization
- ❌ External `$ref` files (only internal refs supported)
- ❌ Record `oneOf/anyOf` alternates under `x-alt`

### C. Operation synthesis
- ❌ Advanced style/explode handling for arrays
- ❌ Response excerpts use placeholder instead of real examples

### F. Output writers
- ❌ Grouping by tag not perfectly aligned (uses name prefix heuristic)
- ❌ Doesn't sort by tag then name (sorts by path instead)

### G. CLI & config
- ❌ `--split-by=tag|path`
- ❌ `--keep-oneof`
- ❌ `--no-prune`
- ❌ `--prefer=json`
- ❌ `--max-enum=N`

### H. Robustness
- ❌ Stream parsing for huge specs (loads everything into memory)
- ❌ Description truncation is basic
- ❌ `--tags=...` to filter by tags
- ❌ Memory guardrails for 10k+ line specs
- ❌ Example size limits (not enforced)

### I. Tests
- ❌ Golden tests (Petstore, Stripe, GitHub)
- ❌ Round-trip smoke test
- ❌ Lint for description length
- ❌ Enum count limits

### J. RAG glue
- ❌ `embedding_text` field in chunks
- ❌ `index.csv` with `id,method,path,tag`

## Output Quality

### tools.json
- ✅ Valid JSON Schema
- ✅ Complete HTTP metadata
- ✅ Auth info surfaced
- ✅ Pagination hints
- ✅ Error codes
- ✅ Curl examples

### docs.md
- ✅ Clean markdown structure
- ✅ Grouped by inferred tags
- ✅ Required params highlighted
- ✅ Runnable curl examples
- ✅ Concise descriptions

### chunks.jsonl
- ✅ One JSON per line
- ✅ Text size: 29-800 chars
- ✅ Key metadata (method, path, required params)
- ✅ Auth flag

## Known Limitations

1. **Memory usage**: Loads entire spec into memory (not suitable for 100MB+ specs)
2. **Tag inference**: Uses name prefix as fallback when tags not present
3. **Example values**: Synthesized examples are basic (123, "value", etc.)
4. **Response examples**: Placeholder instead of real schema examples
5. **oneOf/anyOf**: Always picks first option without warning
6. **External refs**: Not supported yet
7. **Multipart/form-data**: Limited testing
8. **OAuth2 flows**: Only lists flow names, doesn't detail endpoints

## Testing Coverage

✅ Successfully tested with:
- APIs.guru OpenAPI 3.0 spec (JSON)
- APIs.guru OpenAPI 3.0 spec (YAML)

✅ Test suite validates:
- JSON structure and required fields
- Parameter/property consistency
- Path parameter mapping
- Chunk size limits
- Document sections

❌ Not yet tested with:
- Large specs (100+ endpoints)
- OpenAPI 3.1 features
- Complex allOf/oneOf/anyOf
- External $ref files
- Multipart uploads
- OAuth2 with multiple flows

## Usage Statistics

For the APIs.guru test spec:
- **Input**: 400 lines YAML
- **Output**: 
  - tools.json: ~1.3KB (7 tools)
  - docs.md: ~1.9KB
  - chunks.jsonl: ~800B (7 lines)
- **Processing time**: <1 second

## Next Steps for Production Use

Priority order:

1. **Golden tests** - Add test cases for common patterns (Stripe, GitHub, Petstore)
2. **External refs** - Support file:// and http:// references
3. **Better examples** - Use schema.example/default more intelligently
4. **Tag grouping** - Improve tag inference and grouping
5. **CLI polish** - Add --tags filter, --max-enum, etc.
6. **Stream parsing** - For 10k+ line specs
7. **oneOf/anyOf** - Record alternates for review
8. **Response examples** - Generate realistic response excerpts

