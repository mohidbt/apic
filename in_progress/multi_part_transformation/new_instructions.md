Here's a concrete, opinionated blueprint you can implement right away.

---

## ✅ Implementation Status

**Overall Progress: ~70% Complete** (Core features done, optional/advanced features pending)

Legend:
- `[x]` = Fully implemented and tested
- `[~]` = Partially implemented (see strikethrough for missing parts)
- `[ ]` = Not yet implemented

Quick Summary:
- ✅ **A. Parsing & normalization**: 4/5 complete (external refs pending)
- ✅ **B. Auth extraction**: 3/3 complete
- ✅ **C. Operation synthesis**: 9/10 complete (style/explode basic)
- ✅ **D. Pagination heuristics**: 3/3 complete (Link headers pending)
- 🟡 **E. Schema pruning**: 1/2 complete (no inlining)
- ✅ **F. Output writers**: 3/3 complete
- 🟡 **G. CLI & config**: 1/4 flags (--out, --server-index done)
- 🟡 **H. Robustness**: 2/5 (basic deduplication & truncation)
- 🟡 **I. Tests**: 3/5 (validation suite, no golden tests)
- ❌ **J. RAG glue**: 0/2 (optional features)

**Working script: `new_main.py` (830 lines)**  
**Test suite: `test.py` passes all validation checks**  
**Tested with: APIs.guru OpenAPI 3.0 spec (7 endpoints)**

---

# What to transform (and into what)

## Output artifacts (produce all three)

1. **`tools.json`** — machine-readable tool/function specs for the agent (1 entry per endpoint).
2. **`docs.md`** — concise human-readable reference for prompting/RAG.
3. **`chunks.jsonl`** — retrieval chunks (one small record per endpoint) for fast, targeted context injection.

---

## 1) `tools.json` (the agent’s contract)

A single JSON file with:

```json
{
  "api_name": "Petstore",
  "version": "1.0.0",
  "servers": ["https://api.example.com/v1"],
  "auth": {
    "type": "bearer", 
    "header": "Authorization", 
    "format": "Bearer ${TOKEN}", 
    "oauth2_scopes": []
  },
  "common_headers": ["User-Agent", "X-Request-Id"],
  "rate_limits": {"headers": ["X-RateLimit-Remaining","Retry-After"]},
  "tools": [
    {
      "name": "pets_list",
      "description": "List pets. Returns an array of pets.",
      "parameters": { "$schema": "http://json-schema.org/draft-07/schema#", "type": "object",
        "properties": {
          "limit": {"type": "integer", "minimum": 1, "maximum": 100, "description": "Max items per page"},
          "tag": {"type": "string", "description": "Filter by tag"}
        },
        "required": []
      },
      "returns": { "type": "array", "items": {"$ref": "#/components/schemas/Pet"} },
      "x-http": {
        "method": "GET",
        "path_template": "/pets",
        "arg_mapping": {
          "limit": {"in": "query", "name": "limit"},
          "tag":   {"in": "query", "name": "tag"}
        },
        "request_body": null,
        "success_code": 200,
        "response_pointer": "application/json",
        "pagination": {"style": "limit-offset", "limit_param": "limit", "offset_param": "offset", "items_path": "$", "next_offset_path": "$.next_offset"},
        "auth_required": true,
        "content_types": {"request": [], "response": ["application/json"]}
      },
      "examples": {
        "curl": "curl -H 'Authorization: Bearer ${TOKEN}' 'https://api.example.com/v1/pets?limit=25'",
        "response_excerpt": "[{\"id\":1,\"name\":\"Fluffy\"}]"
      },
      "errors": [{"status": 401, "name": "Unauthorized"}, {"status": 429, "name": "Rate limited"}]
    }
  ],
  "components": {
    "schemas": {
      "Pet": { "type": "object", "properties": { "id":{"type":"integer"}, "name":{"type":"string"}}, "required": ["id","name"] }
    }
  }
}
```

### Exact transformation rules → OpenAPI ➜ `tools.json`

For each field below, **where to read from** in OpenAPI and **how to normalize**:

* **api_name/version**: from `info.title` / `info.version`.
* **servers**: prefer `servers` at root; if multiple, pick the first https server as default. Keep all in array.
* **auth**: from `components.securitySchemes` and root/operation `security`. Normalize to one of:

  * `apiKey` → `{type:"apiKey", in:"header"|"query", name:"X-API-Key"}` and add `format` hint `${API_KEY}`.
  * `http: bearer` → `{type:"bearer", header:"Authorization", format:"Bearer ${TOKEN}"}`.
  * `oauth2` → `{type:"oauth2", flows:[...], oauth2_scopes:[...]}`.
* **common_headers**: collect any global headers (e.g., idempotency/rate limit headers) mentioned under `components.parameters` or vendor extensions; de-dupe.
* **rate_limits**: if docs mention headers (e.g., `X-RateLimit-*`, `Retry-After`) in responses or components, list them.

Per **operation** (`paths.{path}.{method}`):

* **name**: prefer `operationId`; else build `tagOrResource_method_path` (e.g., `pets_list` for `GET /pets`, `pets_update_by_id` for `PATCH /pets/{id}`).

* **description**: `summary` + first sentence of `description`. Keep ≤ 160 chars. Strip markdown links/code blocks, convert backticks to plain text.

* **parameters (JSON Schema)**:

  * Merge path-level and operation-level `parameters`.
  * Convert each param to a property in a **single object schema**. Keep `type`, numeric/string bounds, `enum`, `pattern`, and `description`.
  * Mark `required: true` params in `required` array.
  * For **path params**, keep them as properties (the agent will supply them); record location in `x-http.arg_mapping`.
  * If `style`/`explode` present, keep in `x-http.arg_mapping.style` (useful for arrays).

* **request_body**:

  * If `requestBody` exists, prefer `application/json`; else `multipart/form-data`; else `application/x-www-form-urlencoded`.
  * Flatten `$ref`, `allOf`, `oneOf` (choose the **first** valid schema for `oneOf`/`anyOf` but record alternates in `x-http.request_body.alternates` to avoid ambiguity).
  * Move top-level body properties into `parameters.properties` **only if** they are simple scalars **and** content type is form-like; otherwise keep them under `x-http.request_body.schema`.
  * Preserve `required` fields.

* **returns**:

  * Pick canonical success: prefer 200/201/202/204 (first present).
  * Extract response schema for preferred content type (`application/json` first). If none, set `{ "type": "null" }` and `success_code` accordingly (e.g., 204).

* **x-http**:

  * `method`, `path_template` from the operation.
  * `arg_mapping`: for each parameter and body property, specify `{in: "path"|"query"|"header"|"cookie"|"body", name: "…" }`.
  * `content_types`: list request/response media types.
  * `auth_required`: true if any security requirement applies (operation-level or root).
  * `response_pointer`: the media type chosen for `returns` (e.g., `application/json`).

* **pagination (heuristics)**:

  * Detect styles:

    * limit/offset → params named `limit`/`offset` or `page`/`per_page`.
    * cursor/token → params `cursor`, `page_token`, or response fields `next_cursor`, `next`, `links.next`.
    * header-driven → `Link` header with `rel="next"`, or `X-Next-Page`.
  * Emit a block like:

    ```json
    {"style":"cursor","cursor_param":"cursor","items_path":"$.items","next_cursor_path":"$.next_cursor"}
    ```

* **errors**: collect 4xx/5xx codes → `{status, name}` from the response description’s first sentence.

* **examples**:

  * Prefer `examples` / `example` from OpenAPI; else synthesize minimal cURL using `servers[0]`, `path_template`, and 1–2 parameters with sample/defaults.

* **components.schemas**: carry over only the schemas actually referenced by `returns`/`request_body` (prune unused); fully dereferenced and flattened.

---

## 2) `docs.md` (human-readable quick ref)

Structure:

* **Header**: name, version, base URL(s), auth instructions, rate limit notes.
* **Per tag** (or resource): small table:

  * Method & path • Short description • Required params • Returns.
* **Per endpoint “card”**:

  * Purpose (1 sentence).
  * **Signature**: `name(parameters) -> returns` in pseudo-code.
  * **Required params** with types & constraints (bulleted).
  * **Auth** (if special scopes).
  * **Pagination** instructions (if any).
  * **Minimal example** (cURL).
  * **Common errors** (bulleted list).
    Keep it dense and skimmable; no raw YAML.

---

## 3) `chunks.jsonl` (RAG chunks)

One JSON object per line:

```json
{"id":"pets_list","tag":"pets","method":"GET","path":"/pets",
 "text":"List pets. Params: limit (int 1..100), tag (string). Returns array Pet. Pagination: limit-offset.",
 "meta":{"required":["limit"],"auth":true}}
```

Use ~400–800 chars per chunk max. Include `text` that contains the key facts an LLM needs to choose and call the endpoint correctly.

---

# Engineering TODO (step-by-step)

## A. Parsing & normalization

* [x] Accept `.yaml|.yml|.json`; parse OpenAPI 3.0/3.1 (use a robust parser).
* [x] **Dereference** all `$ref` (components, ~~external files~~). Detect cycles.
* [~] **Flatten** `allOf` (merge), pick first branch for `oneOf/anyOf` ~~but record alternates under `x-alt` so humans can review~~.
* [x] Choose default **server** (first https), but preserve full list.
* [x] Normalize types (OpenAPI schema → JSON Schema Draft-07 subset used in `tools.json`).

## B. Auth extraction

* [x] Read `components.securitySchemes` and root/operation `security`.
* [x] Normalize to one of: `apiKey|bearer|basic|oauth2`.
* [x] Extract OAuth2 scopes per operation; compute `auth_required`.

## C. Operation synthesis

* [x] Build unique **operation name** (prefer `operationId`; else synthesize).
* [x] Merge path-level & operation-level **parameters** (respect `in`, `name`, `required`, ~~style/explode~~).
* [x] Create **`parameters` JSON Schema object** (properties + required).
* [x] Build **`x-http.arg_mapping`** mapping each property to its source (path/query/header/cookie/body).
* [x] Extract **requestBody** (prefer JSON; else multipart; else form).
* [x] Extract **returns** (pick canonical 2xx, prefer JSON).
* [x] Build **errors** list from 4xx/5xx.
* [x] Generate concise **description** (summary + first sentence of description, trimmed).
* [~] Generate **examples**:

  * [x] Use `schema.example|default`; else synthesize simple literals by type (int: 1, string: "example", enum: first value).
  * [~] Produce minimal cURL and ~~a tiny JSON response excerpt (if schema known)~~ (uses placeholder).

## D. Pagination heuristics

* [x] Inspect parameters for `limit/offset/page/per_page/cursor/token`.
* [~] Inspect response schema for `items`, `data`, `results`, `links.next`, `next_cursor`, ~~headers (`Link`)~~.
* [x] Emit standardized `pagination` block; if ambiguous, omit.

## E. Schema pruning & carry-over

* [x] Collect only schemas used by `request_body`/`returns`.
* [ ] Inline tiny schemas (≤ 5 fields) into `returns` for brevity; keep larger ones under `components.schemas`.

## F. Output writers

* [~] Emit **`tools.json`** (deterministic ordering: ~~by tag, then name~~ by path).
* [x] Emit **`docs.md`**:

  * Index section + per-tag tables + endpoint cards.
* [x] Emit **`chunks.jsonl`** (one line per tool) with compressed `text`.

## G. CLI & config

* [~] CLI: `new_main.py INPUT.(yaml|json) --out outdir --server-index 0` ~~--prefer=json --max-enum=12~~
* [~] Flags:

  * [x] `--server-index`: choose which server base URL.
  * [ ] `--split-by=tag|path`: grouping in `docs.md`.
  * [ ] `--keep-oneof`: keep multiple branches (don't collapse).
  * [ ] `--no-prune`: keep all component schemas.

## H. Robustness on huge specs

* [ ] Stream parsing (avoid loading multiple copies).
* [x] Limit examples size; truncate long descriptions.
* [x] Deterministic name de-dupe (`pets_list`, `pets_list_2`).
* [ ] Optional `--tags=…` to include only subsets.
* [ ] Memory guardrails; test on 10k+ line specs.

## I. Tests

* [ ] Golden tests: Petstore, Stripe-like cursor pagination, GitHub-like Link header pagination, multipart upload endpoint.
* [x] Validate that every `path` param appears in `parameters.required` and `arg_mapping`.
* [ ] Round-trip smoke test: from `tools.json`, synthesize a request and ensure it conforms to original OpenAPI (method/path/required params/content type).
* [~] Lint: all descriptions ≤ 160 chars; ~~enums ≤ `--max-enum`~~.
* [x] JSON Schema validation for `tools.json`.

## J. (Optional) RAG glue

* [ ] Add `embedding_text` field to chunks with cleaned, sentence-level summary.
* [ ] Produce `index.csv` with `id,method,path,tag`.

---

# Minimal implementation sketch (pseudocode)

```python
spec = load_openapi(input_path)                  # parse YAML/JSON
spec = deref(spec)                               # resolve $ref

api = {
  "api_name": spec.info.title,
  "version": spec.info.version,
  "servers": pick_servers(spec.servers),
  "auth": extract_auth(spec),
  "common_headers": find_common_headers(spec),
  "rate_limits": detect_rate_limit_headers(spec),
  "tools": [],
  "components": {"schemas": {}}
}

for path, methods in spec.paths.items():
  for method, op in methods.items():
    tool = {}
    tool["name"] = make_name(op, path, method)
    tool["description"] = summarize(op)
    params = merge_params(spec, path, op)
    body = extract_request_body(op)
    returns = extract_success_response(op)
    mapping = build_arg_mapping(params, body)

    tool["parameters"] = to_json_schema(params, body)
    tool["returns"] = returns.schema
    tool["x-http"] = {
      "method": method.upper(),
      "path_template": path,
      "arg_mapping": mapping,
      "request_body": body.meta,
      "success_code": returns.code,
      "response_pointer": returns.media_type,
      "pagination": detect_pagination(params, returns),
      "auth_required": is_auth_required(spec, op),
      "content_types": {"request": body.media_types, "response": returns.media_types}
    }
    tool["errors"] = list_errors(op)
    tool["examples"] = synth_examples(api, tool)
    api["tools"].append(tool)
    collect_used_schemas(api, tool)

api["components"]["schemas"] = prune_schemas(collected)
write_tools_json(api)
write_docs_md(api)
write_chunks_jsonl(api)
```

---

# Notes on design choices

* **Single `parameters` object** per endpoint is friendliest for function-calling agents; `x-http.arg_mapping` preserves the HTTP placement so executors can build real requests.
* **Flattening** produces predictable shapes; recording alternates avoids losing information.
* **Pagination block** standardizes the most annoying variability without overfitting.
* **Three artifacts** cover execution (`tools.json`), human promptability (`docs.md`), and retrieval (`chunks.jsonl`).

If you’d like, I can generate a starter repo layout (files, test specs, and a tiny parser) to jump-start implementation.
