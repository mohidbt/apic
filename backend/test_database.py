#!/usr/bin/env python3
"""
Quick test script to verify database functionality.
Run this after installing dependencies: pip install -r requirements.txt
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

from models.database import init_db, SessionLocal
from models.api_spec import ApiSpec, Tag
import crud.specs as crud
from schemas.api_spec import SpecCreate


def test_database():
    """Test basic database operations."""
    print("🧪 Testing database functionality...\n")
    
    # Initialize database
    print("1. Initializing database...")
    init_db()
    print("   ✅ Database initialized\n")
    
    # Create a session
    db = SessionLocal()
    
    try:
        # Test 1: Create a spec
        print("2. Creating test API spec...")
        spec_data = SpecCreate(
            name="Test API",
            version="1.0.0",
            provider="Test Provider",
            original_filename="test.yaml",
            original_format="yaml",
            original_content="openapi: 3.0.0\ninfo:\n  title: Test API\n  version: 1.0.0",
            markdown_content="# Test API\n**Version:** 1.0.0\n\nThis is a test.",
            file_size_bytes=100,
            tags=["test", "example"]
        )
        
        spec = crud.create_spec(db, spec_data)
        print(f"   ✅ Created spec with ID: {spec.id}\n")
        
        # Test 2: List specs
        print("3. Listing all specs...")
        specs, total = crud.list_specs(db, skip=0, limit=10)
        print(f"   ✅ Found {total} spec(s)\n")
        
        # Test 3: Get spec by ID
        print("4. Retrieving spec by ID...")
        retrieved = crud.get_spec(db, spec.id)
        print(f"   ✅ Retrieved: {retrieved.name} v{retrieved.version}\n")
        
        # Test 4: Full-text search
        print("5. Testing full-text search...")
        search_results, count = crud.search_specs(db, "test", skip=0, limit=10)
        print(f"   ✅ Search found {count} result(s)\n")
        
        # Test 5: List tags
        print("6. Listing tags...")
        tags = crud.list_tags(db)
        print(f"   ✅ Found {len(tags)} tag(s): {', '.join(t.name for t in tags)}\n")
        
        # Test 6: Filter by tag
        print("7. Filtering by tag 'test'...")
        tagged_specs, tagged_count = crud.filter_by_tag(db, "test", skip=0, limit=10)
        print(f"   ✅ Found {tagged_count} spec(s) with tag 'test'\n")
        
        # Test 7: Get versions
        print("8. Getting all versions of 'Test API'...")
        versions = crud.get_versions(db, "Test API")
        print(f"   ✅ Found {len(versions)} version(s)\n")
        
        # Test 8: Delete spec
        print("9. Deleting test spec...")
        success = crud.delete_spec(db, spec.id)
        print(f"   ✅ Deleted: {success}\n")
        
        print("=" * 60)
        print("✅ All tests passed! Database is working correctly.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()
    
    return True


if __name__ == "__main__":
    success = test_database()
    sys.exit(0 if success else 1)

