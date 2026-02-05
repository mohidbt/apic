#!/usr/bin/env python3
"""
FastAPI Backend for OpenAPI to Markdown Converter
Handles file uploads and returns converted markdown files
"""

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Query
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager
import io
import os
import tempfile
from pathlib import Path
from typing import Optional, List
from transformation import OpenAPIToMarkdown
import httpx
import logging

# Import database models and CRUD operations
from models.database import get_db, init_db
from models.api_spec import ApiSpec, Tag
import crud.specs as crud
from schemas.api_spec import (
    SpecCreate,
    SpecResponse,
    SpecDetail,
    SpecListResponse,
    TagResponse,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database on startup and cleanup on shutdown."""
    # Startup
    logger.info("Initializing database...")
    try:
        init_db()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise
    
    yield
    
    # Shutdown (if needed in the future)
    logger.info("Shutting down...")


app = FastAPI(
    title="OpenAPI to Markdown Converter API",
    description="Convert OpenAPI YAML/JSON specs to LLM-ready markdown",
    version="1.0.0",
    lifespan=lifespan
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


@app.post("/api/convert")
async def convert_openapi(
    file: UploadFile = File(...),
    save_to_db: bool = Query(True, description="Save conversion to database"),
    db: Session = Depends(get_db)
):
    """
    Convert uploaded OpenAPI YAML/JSON file to markdown
    
    Args:
        file: Uploaded OpenAPI specification file (.yaml, .yml, or .json)
        save_to_db: Whether to save the conversion to database (default: True)
        db: Database session
    
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
            
            # Save to database if requested
            if save_to_db:
                try:
                    spec_info = converter.spec.get('info', {})
                    
                    # Extract tag names from OpenAPI tags (which are objects with 'name' field)
                    raw_tags = converter.spec.get('tags', [])
                    tag_names = []
                    if isinstance(raw_tags, list):
                        for tag in raw_tags[:5]:  # Limit to 5 tags
                            if isinstance(tag, dict) and 'name' in tag:
                                tag_names.append(tag['name'])
                            elif isinstance(tag, str):
                                tag_names.append(tag)
                    
                    spec_data = SpecCreate(
                        name=spec_info.get('title', 'Untitled API'),
                        version=spec_info.get('version', '1.0.0'),
                        provider=spec_info.get('x-providerName') or spec_info.get('contact', {}).get('name'),
                        original_filename=file.filename,
                        original_format='yaml' if file_extension in ['.yaml', '.yml'] else 'json',
                        original_content=content.decode('utf-8'),
                        markdown_content=markdown_content,
                        file_size_bytes=len(content),
                        tags=tag_names
                    )
                    
                    # Check if spec already exists
                    existing_spec = crud.get_spec_by_name_version(
                        db, spec_data.name, spec_data.version
                    )
                    
                    if not existing_spec:
                        db_spec = crud.create_spec(db, spec_data)
                        logger.info(f"✅ Saved spec to database: ID={db_spec.id}")
                    else:
                        logger.info(f"ℹ️ Spec already exists in database: ID={existing_spec.id}")
                        
                except IntegrityError as e:
                    logger.warning(f"⚠️ Could not save to database (duplicate?): {e}")
                except Exception as e:
                    logger.error(f"⚠️ Error saving to database: {e}")
                    # Continue with conversion even if database save fails
            
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


# ============================================================================
# Database API Endpoints
# ============================================================================

@app.get("/api/specs", response_model=SpecListResponse)
async def list_specs(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Max records to return"),
    name: Optional[str] = Query(None, description="Filter by API name"),
    tag: Optional[str] = Query(None, description="Filter by tag"),
    db: Session = Depends(get_db)
):
    """
    List all API specs with pagination and optional filtering.
    
    Query parameters:
    - skip: Pagination offset (default: 0)
    - limit: Number of results (default: 20, max: 100)
    - name: Filter by exact API name (shows all versions)
    - tag: Filter by tag name
    """
    try:
        if tag:
            specs, total = crud.filter_by_tag(db, tag, skip, limit)
        else:
            specs, total = crud.list_specs(db, skip, limit, name)
        
        page = (skip // limit) + 1
        
        return SpecListResponse(
            total=total,
            page=page,
            page_size=limit,
            specs=[SpecResponse(**spec.to_dict()) for spec in specs]
        )
    except Exception as e:
        logger.error(f"Error listing specs: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/specs/search", response_model=SpecListResponse)
async def search_specs_endpoint(
    q: str = Query(..., min_length=1, description="Search query"),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Full-text search across API specs using FTS5.
    
    Searches in: API name, provider, and markdown content.
    """
    try:
        specs, total = crud.search_specs(db, q, skip, limit)
        page = (skip // limit) + 1
        
        return SpecListResponse(
            total=total,
            page=page,
            page_size=limit,
            specs=[SpecResponse(**spec.to_dict()) for spec in specs]
        )
    except Exception as e:
        logger.error(f"Error searching specs: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/specs/{spec_id}", response_model=SpecDetail)
async def get_spec_detail(
    spec_id: int,
    db: Session = Depends(get_db)
):
    """
    Get detailed information about a specific API spec, including full content.
    """
    spec = crud.get_spec(db, spec_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Spec not found")
    
    return SpecDetail(**spec.to_dict(include_content=True))


@app.delete("/api/specs/{spec_id}")
async def delete_spec_endpoint(
    spec_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an API spec by ID.
    """
    success = crud.delete_spec(db, spec_id)
    if not success:
        raise HTTPException(status_code=404, detail="Spec not found")
    
    return {"message": "Spec deleted successfully", "id": spec_id}


@app.get("/api/specs/{spec_id}/download/markdown")
async def download_markdown(
    spec_id: int,
    db: Session = Depends(get_db)
):
    """
    Download the markdown file for a specific API spec.
    """
    spec = crud.get_spec(db, spec_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Spec not found")
    
    # Create BytesIO object from markdown content
    markdown_bytes = io.BytesIO(spec.markdown_content.encode('utf-8'))
    
    # Generate filename
    filename = f"{spec.name}-v{spec.version}.md".replace(' ', '-')
    
    return StreamingResponse(
        markdown_bytes,
        media_type="text/markdown",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )


@app.get("/api/specs/{spec_id}/download/original")
async def download_original(
    spec_id: int,
    db: Session = Depends(get_db)
):
    """
    Download the original OpenAPI file for a specific API spec.
    """
    spec = crud.get_spec(db, spec_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Spec not found")
    
    # Create BytesIO object from original content
    content_bytes = io.BytesIO(spec.original_content.encode('utf-8'))
    
    # Determine media type and extension
    if spec.original_format == 'json':
        media_type = "application/json"
        ext = "json"
    else:
        media_type = "application/x-yaml"
        ext = "yaml"
    
    # Generate filename
    filename = f"{spec.name}-v{spec.version}.{ext}".replace(' ', '-')
    
    return StreamingResponse(
        content_bytes,
        media_type=media_type,
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )


@app.get("/api/tags", response_model=List[TagResponse])
async def list_tags_endpoint(
    db: Session = Depends(get_db)
):
    """
    List all tags with their spec counts.
    """
    try:
        tags = crud.list_tags(db)
        return [TagResponse(**tag.to_dict()) for tag in tags]
    except Exception as e:
        logger.error(f"Error listing tags: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/specs/{spec_id}/tags")
async def add_tags_endpoint(
    spec_id: int,
    tag_names: List[str],
    db: Session = Depends(get_db)
):
    """
    Add tags to an existing spec.
    
    Request body: List of tag names (strings)
    """
    spec = crud.add_tags_to_spec(db, spec_id, tag_names)
    if not spec:
        raise HTTPException(status_code=404, detail="Spec not found")
    
    return {
        "message": "Tags added successfully",
        "spec_id": spec_id,
        "tags": [tag.name for tag in spec.tags]
    }


@app.get("/api/specs/by-name/{name}/versions", response_model=List[SpecResponse])
async def get_api_versions(
    name: str,
    db: Session = Depends(get_db)
):
    """
    Get all versions of an API by its name.
    """
    try:
        specs = crud.get_versions(db, name)
        return [SpecResponse(**spec.to_dict()) for spec in specs]
    except Exception as e:
        logger.error(f"Error getting versions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Frontend Proxy Routes (Production only - for Koyeb single-port deployment)
# In local development, frontend runs separately on port 3000
# ============================================================================

@app.get("/")
async def frontend_root():
    """Proxy to frontend on port 3000 (production) or show API docs (development)"""
    # Check if we're in development mode (no frontend on 3000)
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=2.0) as client:
            response = await client.get("http://localhost:3000/", timeout=2.0)
            # Handle redirects
            if response.status_code in [301, 302, 303, 307, 308]:
                return RedirectResponse(url=response.headers.get("location", "/en"))
            return Response(
                content=response.content, 
                media_type=response.headers.get("content-type", "text/html"),
                status_code=response.status_code
            )
    except Exception:
        # Frontend not available (local dev), redirect to API docs
        return RedirectResponse(url="/docs")


@app.get("/{path:path}")
async def catch_all(path: str):
    """Proxy non-API requests to frontend (production deployment)"""
    # Never proxy /api routes - they should be handled by FastAPI endpoints above
    if path.startswith("api"):
        raise HTTPException(status_code=404, detail="API endpoint not found")
    
    # Try to proxy to frontend (production)
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=5.0) as client:
            response = await client.get(f"http://localhost:3000/{path}", timeout=5.0)
            # Handle redirects
            if response.status_code in [301, 302, 303, 307, 308]:
                return RedirectResponse(url=response.headers.get("location", f"/{path}"))
            return Response(
                content=response.content, 
                media_type=response.headers.get("content-type", "text/html"),
                status_code=response.status_code
            )
    except Exception:
        # Frontend not available (local dev without frontend running)
        raise HTTPException(status_code=404, detail="Not found")


if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FastAPI server...")
    print("📝 API docs available at: http://localhost:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

