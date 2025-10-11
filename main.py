#!/usr/bin/env python3
"""
FastAPI Backend for OpenAPI to Markdown Converter
Handles file uploads and returns converted markdown files
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io
import tempfile
from pathlib import Path
from transformation import OpenAPIToMarkdown

app = FastAPI(
    title="OpenAPI to Markdown Converter API",
    description="Convert OpenAPI YAML/JSON specs to LLM-ready markdown",
    version="1.0.0"
)

# Configure CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # Next.js default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "OpenAPI to Markdown Converter API",
        "version": "1.0.0"
    }


@app.post("/convert")
async def convert_openapi(file: UploadFile = File(...)):
    """
    Convert uploaded OpenAPI YAML/JSON file to markdown
    
    Args:
        file: Uploaded OpenAPI specification file (.yaml, .yml, or .json)
    
    Returns:
        Markdown file as downloadable response
    """
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
            if Path(temp_input_path).exists():
                Path(temp_input_path).unlink()
            raise HTTPException(
                status_code=500,
                detail=f"Error converting file: {str(e)}"
            )
    
    except HTTPException:
        raise
    except Exception as e:
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

