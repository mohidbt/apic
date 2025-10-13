#!/usr/bin/env python3
"""
FastAPI Backend for OpenAPI to Markdown Converter
Handles file uploads and returns converted markdown files
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import io
import os
import tempfile
from pathlib import Path
from transformation import OpenAPIToMarkdown
import httpx
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="OpenAPI to Markdown Converter API",
    description="Convert OpenAPI YAML/JSON specs to LLM-ready markdown",
    version="1.0.0"
)

# Configure CORS to allow frontend requests
# Get allowed origins from environment variable or use defaults for local development
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:3001").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "OpenAPI to Markdown Converter API",
        "version": "1.0.0"
    }


@app.get("/")
async def frontend_root():
    """Proxy to frontend on port 3000"""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get("http://localhost:3000/", timeout=10.0)
            # Handle redirects
            if response.status_code in [301, 302, 303, 307, 308]:
                return RedirectResponse(url=response.headers.get("location", "/en"))
            return Response(
                content=response.content, 
                media_type=response.headers.get("content-type", "text/html"),
                status_code=response.status_code
            )
        except Exception as e:
            return {"error": f"Frontend not available: {str(e)}"}


@app.get("/{path:path}")
async def catch_all(path: str):
    """Proxy all other requests to frontend"""
    # Skip API routes - only block these specific paths
    if path in ["api", "convert", "health"] or path.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not found")
    
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get(f"http://localhost:3000/{path}", timeout=10.0)
            # Handle redirects
            if response.status_code in [301, 302, 303, 307, 308]:
                return RedirectResponse(url=response.headers.get("location", f"/{path}"))
            return Response(
                content=response.content, 
                media_type=response.headers.get("content-type", "text/html"),
                status_code=response.status_code
            )
        except Exception:
            # Return 404 if frontend doesn't have the route
            raise HTTPException(status_code=404, detail="Not found")


@app.post("/convert")
async def convert_openapi(file: UploadFile = File(...)):
    """
    Convert uploaded OpenAPI YAML/JSON file to markdown
    
    Args:
        file: Uploaded OpenAPI specification file (.yaml, .yml, or .json)
    
    Returns:
        Markdown file as downloadable response
    """
    logger.info(f"Received conversion request for file: {file.filename}")
    
    # Validate file extension
    allowed_extensions = ['.yaml', '.yml', '.json']
    file_extension = Path(file.filename).suffix.lower()
    
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(allowed_extensions)}"
        )
    
    try:
        # Read uploaded file content
        content = await file.read()
        
        # Create temporary files for processing
        with tempfile.NamedTemporaryFile(
            mode='wb',
            suffix=file_extension,
            delete=False
        ) as temp_input:
            temp_input.write(content)
            temp_input_path = temp_input.name
        
        try:
            # Convert using the transformation module
            converter = OpenAPIToMarkdown(temp_input_path)
            markdown_content = converter.convert()
            
            # Create output filename
            output_filename = Path(file.filename).stem + '.md'
            
            # Create a BytesIO object for the response
            markdown_bytes = io.BytesIO(markdown_content.encode('utf-8'))
            
            # Clean up temporary input file
            Path(temp_input_path).unlink()
            
            logger.info(f"Successfully converted {file.filename} to {output_filename}")
            
            # Return markdown file as downloadable response
            return StreamingResponse(
                markdown_bytes,
                media_type="text/markdown",
                headers={
                    "Content-Disposition": f"attachment; filename={output_filename}"
                }
            )
            
        except Exception as e:
            # Clean up on error
            logger.error(f"Conversion error: {str(e)}")
            if Path(temp_input_path).exists():
                Path(temp_input_path).unlink()
            raise HTTPException(
                status_code=500,
                detail=f"Error converting file: {str(e)}"
            )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing upload: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing upload: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FastAPI server...")
    print("📝 API docs available at: http://localhost:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

