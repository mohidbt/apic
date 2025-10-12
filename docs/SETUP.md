# Setup Guide: OpenAPI to Markdown Converter

This guide will help you set up and run the full-stack application that converts OpenAPI specifications to LLM-ready markdown.

## Architecture

- **Backend**: FastAPI (Python) - handles file uploads and conversions
- **Frontend**: Next.js 14 (React/TypeScript) - file upload interface
- **Converter**: Python module that transforms OpenAPI specs to markdown

## Prerequisites

- Python 3.8+
- Node.js 18+
- npm or yarn

## Backend Setup

1. **Navigate to the project root**:
   ```bash
   cd /Users/m0/Documents/Building/bigberlinhack
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This installs:
   - PyYAML (for parsing OpenAPI files)
   - FastAPI (web framework)
   - Uvicorn (ASGI server)
   - python-multipart (for file uploads)

3. **Start the backend server**:
   ```bash
   python main.py
   ```
   
   The API will be available at:
   - Main endpoint: http://localhost:8000
   - API docs (Swagger): http://localhost:8000/docs
   - Health check: http://localhost:8000/health

## Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend/nextjs-starter-template
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```
   
   The frontend will be available at: http://localhost:3000

## Usage

1. **Start both servers** (in separate terminals):
   - Terminal 1: `python main.py` (from project root)
   - Terminal 2: `npm run dev` (from frontend/nextjs-starter-template)

2. **Open your browser** to http://localhost:3000

3. **Upload a file**:
   - Click the upload area or drag and drop
   - Select a YAML, YML, or JSON OpenAPI specification file
   - Click "Convert to Markdown"

4. **Download result**:
   - The converted markdown file will automatically download
   - File will be named `{original-name}.md`

## API Endpoints

### `POST /convert`

Convert OpenAPI file to markdown.

**Request**:
- Method: POST
- Content-Type: multipart/form-data
- Body: file (YAML/JSON)

**Response**:
- Content-Type: text/markdown
- Body: Converted markdown file
- Headers: Content-Disposition with filename

**Example using curl**:
```bash
curl -X POST http://localhost:8000/convert \
  -F "file=@example/APIs.guru-swagger.yaml" \
  -o output.md
```

### `GET /health`

Health check endpoint.

**Response**:
```json
{
  "status": "healthy"
}
```

## Testing with Example Files

Test the converter with the example files in the `example/` directory:

```bash
# Using curl
curl -X POST http://localhost:8000/convert \
  -F "file=@example/APIs.guru-swagger.json" \
  -o test-output.md

# Or use the web interface at http://localhost:3000
```

## Troubleshooting

### Backend Issues

**"Module not found" errors**:
```bash
pip install -r requirements.txt
```

**Port 8000 already in use**:
```bash
# Find and kill the process
lsof -ti:8000 | xargs kill -9

# Or change the port in main.py:
uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
```

### Frontend Issues

**CORS errors**:
- Ensure the backend is running on port 8000
- Check that CORS is configured in `main.py` to allow `http://localhost:3000`

**"fetch failed" errors**:
- Ensure the backend server is running
- Check the browser console for specific error messages

**Toast notifications not showing**:
- The Sonner toaster component is included in the layout
- Check browser console for React errors

### File Upload Issues

**"Invalid file type" error**:
- Only `.yaml`, `.yml`, and `.json` files are accepted
- Check the file extension

**"Conversion failed" error**:
- Check the backend logs for detailed error messages
- Ensure the uploaded file is a valid OpenAPI specification
- Check the format of the YAML/JSON

## Development

### Backend Development

The backend code is in `main.py` and uses the converter from `transformation.py`.

To enable auto-reload during development, the server runs with `reload=True`.

### Frontend Development

The main page component is at:
```
frontend/nextjs-starter-template/src/app/[locale]/page.tsx
```

Hot reload is enabled by default with Next.js.

## Production Deployment

### Backend

For production, use a production-ready ASGI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend

Build the Next.js app:

```bash
cd frontend/nextjs-starter-template
npm run build
npm start
```

## Features

✨ **Backend**:
- FastAPI with automatic API documentation
- File upload validation
- Streaming response for efficient large file handling
- Temporary file cleanup
- CORS support for local development

✨ **Frontend**:
- Modern, responsive UI
- Drag and drop file upload
- Real-time validation
- Loading states with spinner
- Toast notifications for user feedback
- Dark mode support
- File size display
- Automatic file download

✨ **Converter**:
- Dereferences $ref schemas
- Surfaces authentication and base URLs
- Generates runnable curl examples
- Groups by tag, alphabetically ordered
- Keeps chunks under 2-4k tokens per endpoint

