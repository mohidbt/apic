#!/usr/bin/env python3
"""
Import API specs from JSON export into the database.

Usage:
    python scripts/import_specs.py backup-specs.json

This script reads a JSON export from /api/specs and recreates
the specs in the database. Useful for migrating data between
databases or restoring from backups.
"""

import sys
import json
from pathlib import Path

# Add parent directory to path to import from backend
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.database import SessionLocal, init_db
from models.api_spec import ApiSpec, Tag
import crud.specs as crud
from schemas.api_spec import SpecCreate


def import_specs_from_json(json_file: str):
    """
    Import specs from a JSON export file.
    
    Args:
        json_file: Path to JSON file (from GET /api/specs?limit=1000)
    """
    # Initialize database (creates tables if they don't exist)
    print("Initializing database...")
    init_db()
    
    # Load JSON data
    print(f"Loading specs from {json_file}...")
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    specs_data = data.get('specs', [])
    print(f"Found {len(specs_data)} specs to import")
    
    # Create database session
    db = SessionLocal()
    
    imported = 0
    skipped = 0
    errors = 0
    
    try:
        for spec_data in specs_data:
            try:
                # Check if spec already exists
                existing = crud.get_spec_by_name_version(
                    db,
                    spec_data['name'],
                    spec_data['version']
                )
                
                if existing:
                    print(f"  ⏭️  Skipping {spec_data['name']} v{spec_data['version']} (already exists)")
                    skipped += 1
                    continue
                
                # Create spec
                spec_create = SpecCreate(
                    name=spec_data['name'],
                    version=spec_data['version'],
                    provider=spec_data.get('provider'),
                    original_filename=spec_data.get('original_filename'),
                    original_format=spec_data.get('original_format', 'json'),
                    original_content=spec_data.get('original_content', ''),
                    markdown_content=spec_data.get('markdown_content', ''),
                    file_size_bytes=spec_data.get('file_size_bytes', 0),
                    tags=spec_data.get('tags', [])
                )
                
                crud.create_spec(db, spec_create)
                print(f"  ✅ Imported {spec_data['name']} v{spec_data['version']}")
                imported += 1
                
            except Exception as e:
                print(f"  ❌ Error importing {spec_data.get('name', 'unknown')}: {e}")
                errors += 1
                continue
    
    finally:
        db.close()
    
    # Print summary
    print("\n" + "="*50)
    print("Import Summary:")
    print(f"  ✅ Imported: {imported}")
    print(f"  ⏭️  Skipped: {skipped}")
    print(f"  ❌ Errors: {errors}")
    print("="*50)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/import_specs.py <json_file>")
        print("\nExample:")
        print("  python scripts/import_specs.py backup-specs.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    if not Path(json_file).exists():
        print(f"Error: File not found: {json_file}")
        sys.exit(1)
    
    import_specs_from_json(json_file)


if __name__ == '__main__':
    main()
