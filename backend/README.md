# Backend API

FastAPI server that converts OpenAPI specifications to LLM-ready markdown format.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

The server will start on `http://localhost:8000`

## API Documentation

Once running, visit:
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## Endpoints

### `POST /convert`
Convert an OpenAPI YAML/JSON file to markdown.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: File upload (`.yaml`, `.yml`, or `.json`)

**Response:**
- Content-Type: `text/markdown`
- Body: Converted markdown file

**Example:**
```bash
curl -X POST http://localhost:8000/convert \
  -F "file=@openapi-spec.yaml" \
  -o output.md
```

### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy"
}
```

## Environment Variables

- `ALLOWED_ORIGINS` - Comma-separated list of allowed CORS origins (default: `http://localhost:3000,http://localhost:3001`)
- `PORT` - Server port (default: `8000`)

## Development

The backend uses:
- **FastAPI** - Modern Python web framework
- **uvicorn** - ASGI server
- **PyYAML** - YAML parsing
- **transformation.py** - Core conversion logic

## Deployment

For production deployment:

```bash
# Set environment variables
export ALLOWED_ORIGINS="https://your-frontend.com"

# Run with production settings
uvicorn main:app --host 0.0.0.0 --port 8000
```

See `../docs/DEPLOYMENT.md` for Koyeb-specific instructions.

