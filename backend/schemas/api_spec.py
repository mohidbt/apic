"""
Pydantic schemas for API request and response validation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class TagCreate(BaseModel):
    """Schema for creating a new tag."""
    name: str = Field(..., min_length=1, max_length=100)


class TagResponse(BaseModel):
    """Schema for tag response."""
    id: int
    name: str
    spec_count: int = 0
    
    class Config:
        from_attributes = True


class SpecCreate(BaseModel):
    """Schema for creating a new API spec."""
    name: str = Field(..., min_length=1, max_length=255)
    version: str = Field(..., min_length=1, max_length=50)
    provider: Optional[str] = Field(None, max_length=255)
    original_filename: Optional[str] = Field(None, max_length=255)
    original_format: Optional[str] = Field(None, pattern='^(yaml|json)$')
    original_content: str = Field(..., min_length=1)
    markdown_content: str = Field(..., min_length=1)
    token_count: Optional[int] = Field(None, ge=0)
    uploaded_by: Optional[str] = Field(None, max_length=255)
    file_size_bytes: Optional[int] = Field(None, ge=0)
    tags: Optional[List[str]] = Field(default_factory=list)


class SpecResponse(BaseModel):
    """Schema for API spec response (without full content)."""
    id: int
    name: str
    version: str
    provider: Optional[str]
    original_filename: Optional[str]
    original_format: Optional[str]
    token_count: Optional[int]
    uploaded_at: datetime
    uploaded_by: Optional[str]
    file_size_bytes: Optional[int]
    tags: List[str] = []
    
    class Config:
        from_attributes = True


class SpecDetail(SpecResponse):
    """Schema for detailed API spec response (includes full content)."""
    original_content: str
    markdown_content: str
    
    class Config:
        from_attributes = True


class SpecListResponse(BaseModel):
    """Schema for paginated list of specs."""
    total: int
    page: int
    page_size: int
    specs: List[SpecResponse]

