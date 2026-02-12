"""
CRUD operations for API specifications and tags.
"""

from sqlalchemy.orm import Session
from sqlalchemy import func, or_, text
from typing import List, Optional, Tuple
from models.api_spec import ApiSpec, Tag
from schemas.api_spec import SpecCreate


def create_spec(
    db: Session,
    spec_data: SpecCreate
) -> ApiSpec:
    """
    Create a new API specification in the database.
    
    Args:
        db: Database session
        spec_data: Spec creation data
    
    Returns:
        Created ApiSpec instance
    
    Raises:
        IntegrityError: If spec with same name/version already exists
    """
    # Create the spec
    db_spec = ApiSpec(
        name=spec_data.name,
        version=spec_data.version,
        provider=spec_data.provider,
        original_filename=spec_data.original_filename,
        original_format=spec_data.original_format,
        original_content=spec_data.original_content,
        markdown_content=spec_data.markdown_content,
        token_count=spec_data.token_count,
        uploaded_by=spec_data.uploaded_by,
        file_size_bytes=spec_data.file_size_bytes,
    )
    
    # Add tags if provided
    if spec_data.tags:
        for tag_name in spec_data.tags:
            tag = get_or_create_tag(db, tag_name)
            db_spec.tags.append(tag)
    
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    
    return db_spec


def get_spec(db: Session, spec_id: int) -> Optional[ApiSpec]:
    """
    Get an API spec by ID.
    
    Args:
        db: Database session
        spec_id: Spec ID
    
    Returns:
        ApiSpec instance or None if not found
    """
    return db.query(ApiSpec).filter(ApiSpec.id == spec_id).first()


def get_spec_by_name_version(
    db: Session,
    name: str,
    version: str
) -> Optional[ApiSpec]:
    """
    Get an API spec by name and version.
    
    Args:
        db: Database session
        name: API name
        version: API version
    
    Returns:
        ApiSpec instance or None if not found
    """
    return db.query(ApiSpec).filter(
        ApiSpec.name == name,
        ApiSpec.version == version
    ).first()


def list_specs(
    db: Session,
    skip: int = 0,
    limit: int = 20,
    name: Optional[str] = None
) -> Tuple[List[ApiSpec], int]:
    """
    List API specs with pagination.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        name: Optional filter by API name (finds all versions)
    
    Returns:
        Tuple of (list of specs, total count)
    """
    query = db.query(ApiSpec)
    
    # Filter by name if provided
    if name:
        query = query.filter(ApiSpec.name == name)
    
    # Get total count
    total = query.count()
    
    # Get paginated results, ordered by upload date (newest first)
    specs = query.order_by(ApiSpec.uploaded_at.desc()).offset(skip).limit(limit).all()
    
    return specs, total


def search_specs(
    db: Session,
    query: str,
    skip: int = 0,
    limit: int = 20
) -> Tuple[List[ApiSpec], int]:
    """
    Search across API specs using simple substring matching.
    
    Searches in: name, provider, and markdown_content fields.
    Uses case-insensitive ILIKE for broad compatibility across databases.
    
    Args:
        db: Database session
        query: Search query string
        skip: Number of records to skip
        limit: Maximum number of records to return
    
    Returns:
        Tuple of (list of matching specs, total count)
    """
    # Build search filter using ILIKE (case-insensitive substring match)
    search_pattern = f"%{query}%"
    
    # Search across name, provider, and markdown content
    search_filter = or_(
        ApiSpec.name.ilike(search_pattern),
        ApiSpec.provider.ilike(search_pattern),
        ApiSpec.markdown_content.ilike(search_pattern)
    )
    
    # Build query with filter
    query_obj = db.query(ApiSpec).filter(search_filter)
    
    # Get total count
    total = query_obj.count()
    
    # Get paginated results, ordered by upload date (newest first)
    specs = query_obj.order_by(ApiSpec.uploaded_at.desc()).offset(skip).limit(limit).all()
    
    return specs, total


def filter_by_tag(
    db: Session,
    tag_name: str,
    skip: int = 0,
    limit: int = 20
) -> Tuple[List[ApiSpec], int]:
    """
    Filter API specs by tag.
    
    Args:
        db: Database session
        tag_name: Tag name to filter by
        skip: Number of records to skip
        limit: Maximum number of records to return
    
    Returns:
        Tuple of (list of specs with tag, total count)
    """
    # Find the tag
    tag = db.query(Tag).filter(Tag.name == tag_name).first()
    
    if not tag:
        return [], 0
    
    # Get specs with this tag
    query = db.query(ApiSpec).filter(ApiSpec.tags.contains(tag))
    total = query.count()
    specs = query.order_by(ApiSpec.uploaded_at.desc()).offset(skip).limit(limit).all()
    
    return specs, total


def get_versions(
    db: Session,
    name: str
) -> List[ApiSpec]:
    """
    Get all versions of an API by name.
    
    Args:
        db: Database session
        name: API name
    
    Returns:
        List of ApiSpec instances, ordered by version descending
    """
    return db.query(ApiSpec).filter(
        ApiSpec.name == name
    ).order_by(ApiSpec.version.desc()).all()


def delete_spec(db: Session, spec_id: int) -> bool:
    """
    Delete an API spec by ID.
    
    Args:
        db: Database session
        spec_id: Spec ID to delete
    
    Returns:
        True if deleted, False if not found
    """
    spec = get_spec(db, spec_id)
    if not spec:
        return False
    
    db.delete(spec)
    db.commit()
    return True


def get_or_create_tag(db: Session, tag_name: str) -> Tag:
    """
    Get existing tag or create new one.
    
    Args:
        db: Database session
        tag_name: Tag name
    
    Returns:
        Tag instance
    """
    tag = db.query(Tag).filter(Tag.name == tag_name).first()
    if not tag:
        tag = Tag(name=tag_name)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag


def add_tags_to_spec(
    db: Session,
    spec_id: int,
    tag_names: List[str]
) -> Optional[ApiSpec]:
    """
    Add tags to an existing spec.
    
    Args:
        db: Database session
        spec_id: Spec ID
        tag_names: List of tag names to add
    
    Returns:
        Updated ApiSpec instance or None if spec not found
    """
    spec = get_spec(db, spec_id)
    if not spec:
        return None
    
    for tag_name in tag_names:
        tag = get_or_create_tag(db, tag_name)
        if tag not in spec.tags:
            spec.tags.append(tag)
    
    db.commit()
    db.refresh(spec)
    return spec


def list_tags(db: Session) -> List[Tag]:
    """
    List all tags with their spec counts.
    
    Args:
        db: Database session
    
    Returns:
        List of Tag instances
    """
    return db.query(Tag).order_by(Tag.name).all()

