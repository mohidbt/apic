"""
Database configuration and session management for SQLite (local) or PostgreSQL (production).
"""

from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool, QueuePool
import os
from pathlib import Path

# Determine database type and URL
# Prefer DATABASE_URL (for Postgres in production) over DATABASE_PATH (SQLite for local dev)
DATABASE_URL_ENV = os.getenv("DATABASE_URL")

if DATABASE_URL_ENV:
    # Production: Use external database (PostgreSQL, etc.)
    DATABASE_URL = DATABASE_URL_ENV
    IS_SQLITE = DATABASE_URL.startswith("sqlite")
else:
    # Local development: Use SQLite
    DATABASE_PATH = os.getenv("DATABASE_PATH", "./data/apiingest.db")
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    IS_SQLITE = True
    
    # Ensure data directory exists for SQLite
    db_dir = os.path.dirname(DATABASE_PATH)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

# Create SQLAlchemy engine with appropriate configuration
if IS_SQLITE:
    # SQLite: StaticPool ensures connection is reused in single-threaded SQLite
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=False,  # Set to True for SQL debugging
    )
else:
    # PostgreSQL or other: Use normal connection pooling
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Verify connections before using
        pool_size=5,
        max_overflow=10,
        echo=False,  # Set to True for SQL debugging
    )

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base for models
Base = declarative_base()


if IS_SQLITE:
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_conn, connection_record):
        """
        Enable important SQLite pragmas when connection is established.
        - foreign_keys: Enable foreign key constraints
        """
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def get_db():
    """
    Dependency function for FastAPI to get database session.
    
    Usage:
        @app.get("/endpoint")
        def endpoint(db: Session = Depends(get_db)):
            # Use db here
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Initialize database by creating all tables.
    Should be called on application startup.
    """
    # Import models to ensure they're registered
    from .api_spec import ApiSpec, Tag, spec_tags
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create FTS5 virtual table and triggers manually (SQLite only)
    # PostgreSQL and other databases will use simple substring search instead
    if IS_SQLITE:
        # SQLAlchemy doesn't support FTS5 directly, so we use raw SQL
        with engine.connect() as conn:
            # Check if FTS table exists
            result = conn.execute(
                text("SELECT name FROM sqlite_master WHERE type='table' AND name='specs_fts'")
            )
            if not result.fetchone():
                # Create FTS5 virtual table
                conn.execute(text("""
                    CREATE VIRTUAL TABLE specs_fts USING fts5(
                        name, provider, markdown_content,
                        content='api_specs',
                        content_rowid='id'
                    )
                """))
                
                # Create triggers to keep FTS in sync
                conn.execute(text("""
                    CREATE TRIGGER specs_fts_insert AFTER INSERT ON api_specs BEGIN
                        INSERT INTO specs_fts(rowid, name, provider, markdown_content)
                        VALUES (new.id, new.name, new.provider, new.markdown_content);
                    END
                """))
                
                conn.execute(text("""
                    CREATE TRIGGER specs_fts_delete AFTER DELETE ON api_specs BEGIN
                        DELETE FROM specs_fts WHERE rowid = old.id;
                    END
                """))
                
                conn.execute(text("""
                    CREATE TRIGGER specs_fts_update AFTER UPDATE ON api_specs BEGIN
                        UPDATE specs_fts SET 
                            name = new.name,
                            provider = new.provider,
                            markdown_content = new.markdown_content
                        WHERE rowid = new.id;
                    END
                """))
                
                conn.commit()

