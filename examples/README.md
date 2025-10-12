# Example OpenAPI Specifications

This directory contains example OpenAPI specification files that you can use to test the converter.

## Files

### APIs.guru Collection
- **`APIs.guru-swagger.yaml`** - OpenAPI specification from APIs.guru in YAML format
- **`APIs.guru-swagger.json`** - Same specification in JSON format
- **`APIs.guru-swagger.md`** - Pre-converted markdown output (for reference)

### Documented API
- **`openapi.documented.yml`** - Another example with rich documentation
- **`openapi.documented.md`** - Pre-converted markdown output

## Usage

### Command Line

```bash
# From the backend directory
cd backend

# Convert YAML to markdown
python transformation.py ../examples/APIs.guru-swagger.yaml

# Convert JSON to markdown
python transformation.py ../examples/APIs.guru-swagger.json output.md
```

### Web Interface

1. Start the application (see main README.md)
2. Open http://localhost:3000
3. Upload any of the example files
4. Download the converted markdown

### API

```bash
# Using curl
curl -X POST http://localhost:8000/convert \
  -F "file=@examples/APIs.guru-swagger.yaml" \
  -o converted.md
```

## File Formats

Both YAML and JSON OpenAPI specifications are supported:
- `.yaml` or `.yml` - YAML format (recommended for readability)
- `.json` - JSON format (common in API tooling)

## Creating Your Own Examples

To test with your own OpenAPI specifications:

1. Ensure your spec is valid OpenAPI 3.0+ format
2. Place it in this directory
3. Run the converter using any of the methods above

You can validate your OpenAPI spec at:
- https://editor.swagger.io/
- https://apitools.dev/swagger-parser/online/

