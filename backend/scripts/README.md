# Database Migration Scripts

This directory contains scripts for exporting and importing API specs between databases.

## Export Specs

Export all specs from a running instance:

```bash
# Export from production
./backend/scripts/export_specs.sh

# Or manually with curl
curl "https://api-ingest.com/api/specs?limit=1000" > backup-specs.json
```

This creates a JSON file containing all your specs with their metadata and content.

## Import Specs

Import specs into a new database:

```bash
# Make sure you're in the backend directory
cd backend

# Import from JSON export
python scripts/import_specs.py ../backup-specs.json
```

The import script will:
- ✅ Create specs that don't exist
- ⏭️ Skip specs that already exist (by name + version)
- ❌ Report any errors

## Use Cases

### Migrating to External Database

1. Export current production data:
   ```bash
   ./backend/scripts/export_specs.sh
   ```

2. Set up your external database (Supabase/Neon)

3. Configure `DATABASE_URL` in Koyeb

4. Import the data:
   ```bash
   cd backend
   python scripts/import_specs.py ../backup-specs-*.json
   ```

### Regular Backups

Add to cron or run periodically:

```bash
# Backup every day at 2 AM
0 2 * * * /path/to/backend/scripts/export_specs.sh
```

### Local Development with Production Data

1. Export from production
2. Import locally (uses SQLite automatically):
   ```bash
   cd backend
   python scripts/import_specs.py backup-specs.json
   ```

## File Format

The export JSON format matches the `/api/specs` endpoint response:

```json
{
  "total": 2,
  "page": 1,
  "page_size": 20,
  "specs": [
    {
      "id": 1,
      "name": "OpenAI API",
      "version": "2.3.0",
      "provider": "OpenAI",
      "original_filename": "openapi.yaml",
      "original_format": "yaml",
      "original_content": "...",
      "markdown_content": "...",
      "uploaded_at": "2024-01-01T00:00:00",
      "file_size_bytes": 12345,
      "tags": ["ai", "ml"]
    }
  ]
}
```
