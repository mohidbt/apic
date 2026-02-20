#!/usr/bin/env python3
"""
FastAPI Backend for OpenAPI to Markdown Converter
Handles file uploads and returns converted markdown files
"""

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Query, Form, Request
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.concurrency import run_in_threadpool
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager
import io
import os
import tempfile
import time
import json
import yaml
from pathlib import Path
from typing import Optional, List, Dict, Any
from uuid import uuid4
from transformation import OpenAPIToMarkdown
import httpx
import logging
import tiktoken

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

MAX_UPLOAD_BYTES = int(os.getenv("MAX_UPLOAD_BYTES", str(10 * 1024 * 1024)))
UPLOAD_CHUNK_SIZE = int(os.getenv("UPLOAD_CHUNK_SIZE", str(1024 * 1024)))


async def write_upload_to_temp(
    upload: UploadFile,
    suffix: str,
    max_bytes: int,
) -> tuple[str, int, float, float]:
    """Write an uploaded file to disk in chunks and return timings."""
    temp_input_path = ""
    total_bytes = 0
    read_seconds = 0.0
    write_seconds = 0.0

    tmp_dir = os.getenv("TMPDIR")
    if tmp_dir:
        Path(tmp_dir).mkdir(parents=True, exist_ok=True)

    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=suffix,
            delete=False,
            dir=tmp_dir or None,
        ) as temp_input:
            temp_input_path = temp_input.name
            while True:
                read_start = time.perf_counter()
                chunk = await upload.read(UPLOAD_CHUNK_SIZE)
                read_seconds += time.perf_counter() - read_start
                if not chunk:
                    break

                total_bytes += len(chunk)
                if total_bytes > max_bytes:
                    raise HTTPException(
                        status_code=413,
                        detail=f"File too large. Max size is {max_bytes // (1024 * 1024)} MB.",
                    )

                write_start = time.perf_counter()
                temp_input.write(chunk)
                write_seconds += time.perf_counter() - write_start
    except Exception:
        if temp_input_path and Path(temp_input_path).exists():
            Path(temp_input_path).unlink()
        raise

    await upload.seek(0)
    return temp_input_path, total_bytes, read_seconds, write_seconds


def load_openapi_spec(path: str, file_extension: str) -> Dict[str, Any]:
    """Load OpenAPI spec as dict from a file path."""
    with open(path, "r", encoding="utf-8") as f:
        if file_extension in [".yaml", ".yml"]:
            return yaml.safe_load(f) or {}
        return json.load(f)


def estimate_token_count(text: str, model: str = "gpt-4") -> int:
    """
    Estimate token count for markdown content using tiktoken.
    Falls back to cl100k_base encoding if model lookup fails.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


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

# Configure CORS to allow frontend requests.
# Normalize origins to avoid trailing slash mismatches (Origin header has no trailing slash).
allowed_origins_raw = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:3001")
allowed_origins = [
    origin.strip().rstrip("/")
    for origin in allowed_origins_raw.split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[
        "X-Request-ID",
        "X-Request-Duration-Ms",
        "X-Stage-Timings",
        "X-Token-Count",
        "X-Marketplace-Save-Status",
        "X-Marketplace-Spec-Id",
    ],
)


@app.get("/api")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "OpenAPI to Markdown Converter API",
        "version": "1.0.0"
    }


# Cache for GitHub stats (simple in-memory cache)
_github_stats_cache = {
    "data": None,
    "timestamp": 0,
    "cache_duration": 3600  # 1 hour in seconds
}


@app.get("/api/github/stats")
async def get_github_stats():
    """
    Get GitHub repository statistics with caching
    
    Returns cached data if available and fresh (< 1 hour old),
    otherwise fetches from GitHub API
    
    Returns:
        Repository stats including star count
    """
    import time
    
    current_time = time.time()
    cache = _github_stats_cache
    
    # Return cached data if available and fresh
    if cache["data"] and (current_time - cache["timestamp"]) < cache["cache_duration"]:
        logger.debug("Returning cached GitHub stats")
        return {
            **cache["data"],
            "cached": True,
            "cache_age_seconds": int(current_time - cache["timestamp"])
        }
    
    # Fetch fresh data from GitHub API
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.github.com/repos/mohidbt/apic",
                timeout=5.0,
                headers={"Accept": "application/vnd.github.v3+json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract relevant stats
                stats = {
                    "stargazers_count": data.get("stargazers_count", 0),
                    "forks_count": data.get("forks_count", 0),
                    "watchers_count": data.get("watchers_count", 0),
                    "open_issues_count": data.get("open_issues_count", 0),
                    "cached": False
                }
                
                # Update cache
                cache["data"] = stats
                cache["timestamp"] = current_time
                
                logger.info(f"Fetched fresh GitHub stats: {stats['stargazers_count']} stars")
                return stats
            else:
                logger.warning(f"GitHub API returned status {response.status_code}")
                # Return cached data even if stale, or default values
                if cache["data"]:
                    return {**cache["data"], "cached": True, "stale": True}
                return {"stargazers_count": 0, "cached": False, "error": "API unavailable"}
                
    except Exception as e:
        logger.error(f"Error fetching GitHub stats: {e}")
        # Return cached data if available, even if stale
        if cache["data"]:
            return {**cache["data"], "cached": True, "stale": True}
        return {"stargazers_count": 0, "cached": False, "error": str(e)}


@app.post("/api/convert")
async def convert_openapi(
    request: Request,
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
    request_id = request.headers.get("X-Request-ID", str(uuid4()))
    started_at = time.perf_counter()
    stage_times: Dict[str, int] = {
        "read_ms": 0,
        "write_ms": 0,
        "convert_ms": 0,
        "token_ms": 0,
        "db_ms": 0,
    }
    temp_input_path = ""

    logger.info("Received conversion request id=%s file=%s", request_id, file.filename)

    allowed_extensions = [".yaml", ".yml", ".json"]
    safe_filename = file.filename or "upload.json"
    file_extension = Path(safe_filename).suffix.lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(allowed_extensions)}",
        )

    try:
        temp_input_path, file_size, read_seconds, write_seconds = await write_upload_to_temp(
            file,
            file_extension,
            MAX_UPLOAD_BYTES,
        )
        stage_times["read_ms"] = int(read_seconds * 1000)
        stage_times["write_ms"] = int(write_seconds * 1000)

        converter = OpenAPIToMarkdown(temp_input_path)

        convert_started = time.perf_counter()
        markdown_content = await run_in_threadpool(converter.convert)
        stage_times["convert_ms"] = int((time.perf_counter() - convert_started) * 1000)

        token_started = time.perf_counter()
        token_count = await run_in_threadpool(estimate_token_count, markdown_content)
        stage_times["token_ms"] = int((time.perf_counter() - token_started) * 1000)

        output_filename = Path(safe_filename).stem + ".md"
        marketplace_save_status = "skipped"
        marketplace_spec_id = ""

        if save_to_db:
            db_started = time.perf_counter()
            try:
                spec_info = converter.spec.get("info", {})
                raw_tags = converter.spec.get("tags", [])
                tag_names = []
                if isinstance(raw_tags, list):
                    for tag in raw_tags[:5]:
                        if isinstance(tag, dict) and "name" in tag:
                            tag_names.append(tag["name"])
                        elif isinstance(tag, str):
                            tag_names.append(tag)

                original_content = Path(temp_input_path).read_text(encoding="utf-8")
                spec_data = SpecCreate(
                    name=spec_info.get("title", "Untitled API"),
                    version=spec_info.get("version", "1.0.0"),
                    provider=spec_info.get("x-providerName") or spec_info.get("contact", {}).get("name"),
                    original_filename=safe_filename,
                    original_format="yaml" if file_extension in [".yaml", ".yml"] else "json",
                    original_content=original_content,
                    markdown_content=markdown_content,
                    token_count=token_count,
                    file_size_bytes=file_size,
                    tags=tag_names,
                )

                existing_spec = crud.get_spec_by_name_version(db, spec_data.name, spec_data.version)
                if not existing_spec:
                    db_spec = crud.create_spec(db, spec_data)
                    logger.info("Saved spec to database id=%s request_id=%s", db_spec.id, request_id)
                    marketplace_save_status = "created"
                    marketplace_spec_id = str(db_spec.id)
                else:
                    logger.info("Spec already exists id=%s request_id=%s", existing_spec.id, request_id)
                    marketplace_save_status = "exists"
                    marketplace_spec_id = str(existing_spec.id)
            except IntegrityError as e:
                logger.warning("Could not save spec (duplicate) request_id=%s err=%s", request_id, e)
                marketplace_save_status = "exists"
            except Exception as e:
                logger.error("Error saving spec request_id=%s err=%s", request_id, e)
                marketplace_save_status = "failed"
            finally:
                stage_times["db_ms"] = int((time.perf_counter() - db_started) * 1000)

        total_ms = int((time.perf_counter() - started_at) * 1000)
        logger.info(
            "Converted file request_id=%s file=%s size_bytes=%s timings=%s total_ms=%s",
            request_id,
            safe_filename,
            file_size,
            stage_times,
            total_ms,
        )

        return Response(
            content=markdown_content,
            media_type="text/markdown",
            headers={
                "Content-Disposition": f"attachment; filename={output_filename}",
                "X-Request-ID": request_id,
                "X-Request-Duration-Ms": str(total_ms),
                "X-Stage-Timings": json.dumps(stage_times, separators=(",", ":")),
                "X-Token-Count": str(token_count),
                "X-Marketplace-Save-Status": marketplace_save_status,
                "X-Marketplace-Spec-Id": marketplace_spec_id,
            },
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error processing upload request_id=%s err=%s", request_id, e)
        raise HTTPException(status_code=500, detail=f"Error processing upload: {str(e)}")
    finally:
        if temp_input_path and Path(temp_input_path).exists():
            Path(temp_input_path).unlink()


@app.post("/api/specs/share")
async def share_converted_spec(
    request: Request,
    file: UploadFile = File(...),
    markdown_content: str = Form(...),
    token_count: Optional[int] = Form(None),
    db: Session = Depends(get_db),
):
    """
    Save a previously converted markdown + original spec without re-running conversion.
    """
    request_id = request.headers.get("X-Request-ID", str(uuid4()))
    started_at = time.perf_counter()
    temp_input_path = ""

    allowed_extensions = [".yaml", ".yml", ".json"]
    safe_filename = file.filename or "upload.json"
    file_extension = Path(safe_filename).suffix.lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(allowed_extensions)}",
        )

    try:
        temp_input_path, file_size, _, _ = await write_upload_to_temp(
            file,
            file_extension,
            MAX_UPLOAD_BYTES,
        )
        spec = load_openapi_spec(temp_input_path, file_extension)
        spec_info = spec.get("info", {})

        raw_tags = spec.get("tags", [])
        tag_names = []
        if isinstance(raw_tags, list):
            for tag in raw_tags[:5]:
                if isinstance(tag, dict) and "name" in tag:
                    tag_names.append(tag["name"])
                elif isinstance(tag, str):
                    tag_names.append(tag)

        resolved_token_count = token_count
        if resolved_token_count is None:
            resolved_token_count = await run_in_threadpool(estimate_token_count, markdown_content)

        original_content = Path(temp_input_path).read_text(encoding="utf-8")
        spec_data = SpecCreate(
            name=spec_info.get("title", "Untitled API"),
            version=spec_info.get("version", "1.0.0"),
            provider=spec_info.get("x-providerName") or spec_info.get("contact", {}).get("name"),
            original_filename=safe_filename,
            original_format="yaml" if file_extension in [".yaml", ".yml"] else "json",
            original_content=original_content,
            markdown_content=markdown_content,
            token_count=resolved_token_count,
            file_size_bytes=file_size,
            tags=tag_names,
        )

        existing_spec = crud.get_spec_by_name_version(db, spec_data.name, spec_data.version)
        if existing_spec:
            status = "exists"
            spec_id = existing_spec.id
        else:
            db_spec = crud.create_spec(db, spec_data)
            status = "created"
            spec_id = db_spec.id

        total_ms = int((time.perf_counter() - started_at) * 1000)
        logger.info(
            "Shared converted spec request_id=%s status=%s spec_id=%s total_ms=%s",
            request_id,
            status,
            spec_id,
            total_ms,
        )
        return {
            "status": status,
            "spec_id": str(spec_id),
            "request_id": request_id,
            "duration_ms": total_ms,
        }
    except HTTPException:
        raise
    except IntegrityError:
        return {"status": "exists", "spec_id": "", "request_id": request_id}
    except Exception as e:
        logger.error("Error sharing converted spec request_id=%s err=%s", request_id, e)
        raise HTTPException(status_code=500, detail=f"Failed to share spec: {str(e)}")
    finally:
        if temp_input_path and Path(temp_input_path).exists():
            Path(temp_input_path).unlink()


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

