"""
SQLAlchemy models for users and API tokens (MCP authentication).
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    github_id = Column(Integer, unique=True, nullable=False, index=True)
    github_login = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    avatar_url = Column(String(512), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    tokens = relationship("ApiToken", back_populates="user", cascade="all, delete-orphan")

    def to_dict(self, is_admin: bool = False):
        return {
            "id": self.id,
            "github_id": self.github_id,
            "github_login": self.github_login,
            "name": self.name,
            "avatar_url": self.avatar_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "is_admin": is_admin,
        }

    def __repr__(self):
        return f"<User(id={self.id}, github_login='{self.github_login}')>"


class ApiToken(Base):
    __tablename__ = "api_tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token_hash = Column(String(64), unique=True, nullable=False, index=True)
    label = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    last_used_at = Column(DateTime, nullable=True)
    revoked_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="tokens")

    __table_args__ = (
        Index("idx_token_hash", "token_hash"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_used_at": self.last_used_at.isoformat() if self.last_used_at else None,
            "is_revoked": self.revoked_at is not None,
        }

    def __repr__(self):
        return f"<ApiToken(id={self.id}, label='{self.label}')>"
