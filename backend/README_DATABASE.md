# Database Implementation Guide

## Overview

This backend now includes a SQLite database with FTS5 (Full-Text Search) to store converted API specifications. The database allows users to:

- **Store** all converted specs automatically
- **Search** using full-text search across API names, providers, and content
- **Browse** all specs with pagination
- **Filter** by tags
- **Track versions** of APIs
- **Download** markdown or original files anytime

## Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run Test Script

Test that the database works:

```bash
python test_database.py
```

You should see all tests pass with ✅ marks.

### 3. Start the Server

```bash
python main.py
```

The database will initialize automatically on first startup.

## Database Schema

### Tables

**api_specs** - Main table for storing API specifications
- `id` - Primary key
- `name` - API name
- `version` - API version
- `provider` - API provider/company
- `original_filename` - Original uploaded filename
- `original_format` - 'yaml' or 'json'
- `original_content` - Full original OpenAPI content
- `markdown_content` - Converted markdown
- `uploaded_at` - Timestamp
- `uploaded_by` - User identifier (optional)
- `file_size_bytes` - File size

**specs_fts** - FTS5 virtual table for full-text search
- Synced automatically with api_specs via triggers
- Searches across: name, provider, markdown_content

**tags** - Tags for categorizing specs
- `id` - Primary key
- `name` - Unique tag name

**spec_tags** - Many-to-many relationship between specs and tags

## API Endpoints

### Storage Endpoints

#### POST /convert
Convert and optionally save to database
- Query param: `save_to_db=true` (default)
- Automatically saves converted specs

#### GET /api/specs
List all specs with pagination
- Query params: `skip=0`, `limit=20`, `name=`, `tag=`
- Returns: Paginated list of specs

#### GET /api/specs/{id}
Get detailed spec by ID
- Returns: Full spec with original and markdown content

#### DELETE /api/specs/{id}
Delete a spec by ID

### Search Endpoints

#### GET /api/specs/search?q={query}
Full-text search using FTS5
- Query param: `q` (required), `skip=0`, `limit=20`
- Searches: API name, provider, markdown content

### Tag Endpoints

#### GET /api/tags
List all tags with spec counts

#### POST /api/specs/{id}/tags
Add tags to a spec
- Body: List of tag names (JSON array)

### Download Endpoints

#### GET /api/specs/{id}/download/markdown
Download markdown file

#### GET /api/specs/{id}/download/original
Download original OpenAPI file

### Version Endpoints

#### GET /api/specs/by-name/{name}/versions
Get all versions of an API by name

## Usage Examples

### Using curl

```bash
# Convert and save to database
curl -X POST http://localhost:8000/convert \
  -F "file=@openapi.yaml"

# List all specs
curl http://localhost:8000/api/specs

# Search for specs
curl "http://localhost:8000/api/specs/search?q=stripe"

# Filter by tag
curl "http://localhost:8000/api/specs?tag=payments"

# Get spec details
curl http://localhost:8000/api/specs/1

# Download markdown
curl http://localhost:8000/api/specs/1/download/markdown -o api.md

# List all tags
curl http://localhost:8000/api/tags
```

### Using Python

```python
import requests

# Convert and save
with open('openapi.yaml', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/convert',
        files={'file': f}
    )
    markdown = response.content

# Search
response = requests.get(
    'http://localhost:8000/api/specs/search',
    params={'q': 'authentication', 'limit': 10}
)
results = response.json()

print(f"Found {results['total']} specs")
for spec in results['specs']:
    print(f"- {spec['name']} v{spec['version']}")
```

## Database Location

**Local Development:**
- Database file: `backend/data/apiingest.db`
- Automatically created on first run
- Ignored by git (see `.gitignore`)

**Production (Koyeb):**
- Database file: `/app/data/apiingest.db`
- Persists across deployments
- Set env var: `DATABASE_PATH=/app/data/apiingest.db`

## Backup and Restore

### Manual Backup

```bash
# Copy the database file
cp backend/data/apiingest.db backup-$(date +%Y%m%d).db
```

### Export to JSON

```python
from models.database import SessionLocal
from models.api_spec import ApiSpec
import json

db = SessionLocal()
specs = db.query(ApiSpec).all()

with open('backup.json', 'w') as f:
    json.dump([spec.to_dict(include_content=True) for spec in specs], f)

db.close()
```

## Koyeb Deployment

### Environment Variables

Set in Koyeb dashboard:
```
DATABASE_PATH=/app/data/apiingest.db
```

### Persistent Storage

Koyeb automatically persists the `/app` directory, so your database will survive deployments and restarts.

### First Deployment

1. Push code to GitHub
2. Koyeb auto-deploys
3. Database initializes automatically on first request
4. No manual setup needed!

## Troubleshooting

### Database locked error
- SQLite can handle multiple readers but only one writer
- For this use case (low write volume), this is not an issue
- If you get locked errors, it means another process is writing

### FTS5 not working
- Ensure SQLite version supports FTS5 (3.9.0+)
- Check Python's sqlite3 module: `python -c "import sqlite3; print(sqlite3.sqlite_version)"`

### Migration to PostgreSQL

If you outgrow SQLite:

1. Export data to JSON (see above)
2. Change `DATABASE_URL` in `models/database.py`
3. Install `psycopg2-binary`
4. Run initialization
5. Import data

Estimated effort: 2-4 hours

## Architecture

```
FastAPI Backend
    ↓
SQLAlchemy ORM
    ↓
SQLite + FTS5
    ↓
Persistent File (data/apiingest.db)
```

- **Models** (`models/api_spec.py`) - SQLAlchemy models
- **CRUD** (`crud/specs.py`) - Database operations
- **Schemas** (`schemas/api_spec.py`) - Pydantic validation
- **Endpoints** (`main.py`) - FastAPI routes

## Performance

**Expected Performance at Scale:**

| Records | Query Time | Search Time |
|---------|-----------|-------------|
| 100     | < 5ms     | < 10ms      |
| 1,000   | < 10ms    | < 20ms      |
| 10,000  | < 50ms    | < 100ms     |

FTS5 provides excellent performance for full-text search on thousands of records.

## Next Steps

1. ✅ Database is set up and working
2. ✅ All endpoints implemented
3. 🔄 Test locally with example files
4. 🔄 Deploy to Koyeb
5. 📝 Optional: Build frontend browse/search UI

