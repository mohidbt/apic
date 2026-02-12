"""
SQLAlchemy models for API specifications, tags, and relationships.
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


# Many-to-many association table for specs and tags
spec_tags = Table(
    'spec_tags',
    Base.metadata,
    Column('spec_id', Integer, ForeignKey('api_specs.id', ondelete='CASCADE'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True)
)


class ApiSpec(Base):
    """
    Model for storing API specifications with original content and markdown conversion.
    """
    __tablename__ = 'api_specs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    version = Column(String(50), nullable=False)
    provider = Column(String(255), nullable=True)
    original_filename = Column(String(255), nullable=True)
    original_format = Column(String(10), nullable=True)  # 'yaml' or 'json'
    original_content = Column(Text, nullable=False)
    markdown_content = Column(Text, nullable=False)
    token_count = Column(Integer, nullable=True)
    uploaded_at = Column(DateTime, nullable=False, server_default=func.now(), index=True)
    uploaded_by = Column(String(255), nullable=True)
    file_size_bytes = Column(Integer, nullable=True)
    
    # Relationships
    tags = relationship('Tag', secondary=spec_tags, back_populates='specs')
    
    # Unique constraint on name + version
    __table_args__ = (
        Index('idx_name', 'name'),
        Index('idx_uploaded_at', 'uploaded_at'),
        Index('uq_name_version', 'name', 'version', unique=True),
    )
    
    def to_dict(self, include_content=False):
        """
        Convert model to dictionary for API responses.
        
        Args:
            include_content: If True, include full original and markdown content.
                           If False, only include metadata (for listings).
        """
        data = {
            'id': self.id,
            'name': self.name,
            'version': self.version,
            'provider': self.provider,
            'original_filename': self.original_filename,
            'original_format': self.original_format,
            'token_count': self.token_count,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None,
            'uploaded_by': self.uploaded_by,
            'file_size_bytes': self.file_size_bytes,
            'tags': [tag.name for tag in self.tags] if self.tags else []
        }
        
        if include_content:
            data['original_content'] = self.original_content
            data['markdown_content'] = self.markdown_content
        
        return data
    
    def __repr__(self):
        return f"<ApiSpec(id={self.id}, name='{self.name}', version='{self.version}')>"


class Tag(Base):
    """
    Model for tags/categories to organize API specifications.
    """
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    
    # Relationships
    specs = relationship('ApiSpec', secondary=spec_tags, back_populates='tags')
    
    __table_args__ = (
        Index('idx_tag_name', 'name'),
    )
    
    def to_dict(self):
        """Convert tag to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'spec_count': len(self.specs) if self.specs else 0
        }
    
    def __repr__(self):
        return f"<Tag(id={self.id}, name='{self.name}')>"

