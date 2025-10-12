# Changelog

All notable changes to APIIngest will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive deployment guide for Koyeb
- Docker support with docker-compose.yml
- Development helper scripts (dev-backend.sh, dev-frontend.sh)
- Frontend environment variable support for API URL
- Backend environment variable support for CORS origins
- Complete project documentation structure
- CONTRIBUTING.md with contribution guidelines
- MIT License
- Archive directory for historical exploration code

### Changed
- **BREAKING**: Restructured project into clear backend/frontend separation
- Moved backend files (main.py, transformation.py, requirements.txt) to backend/ directory
- Flattened frontend structure from frontend/nextjs-starter-template/ to frontend/
- Renamed example/ to examples/ for consistency
- Consolidated documentation into docs/ directory
- Updated all file paths in documentation to reflect new structure

### Removed
- Duplicate QUICKSTART.md files
- Root-level backend files (moved to backend/)
- Obsolete start-backend.sh and start-frontend.sh (replaced with dev-*.sh)
- Exploration folders from root (moved to .archive/exploration/)

### Fixed
- CORS configuration now uses environment variables
- API URL in frontend now configurable via environment variables
- Improved error handling in file conversion

## [1.0.0] - 2025-01-XX

### Added
- Initial release
- OpenAPI to Markdown conversion
- FastAPI backend with file upload
- Next.js frontend with drag-and-drop
- Support for YAML and JSON formats
- Gitingest-style formatting
- Schema dereferencing
- Curl example generation
- Tag-based organization
- Dark mode support

---

## Release Notes

### Deployment-Ready Structure (Current)

The project has been reorganized for production deployment:

**New Structure:**
```
apiingest/
├── backend/          # FastAPI server
├── frontend/         # Next.js app
├── examples/         # Sample files
├── docs/            # Documentation
├── .archive/        # Historical code
└── .koyeb/          # Deployment config
```

**Migration Guide:**

If you were using the old structure:

1. **Backend commands** - Add `cd backend/` prefix:
   ```bash
   # Old
   python main.py
   
   # New
   cd backend && python main.py
   # OR use helper
   ./dev-backend.sh
   ```

2. **Frontend commands** - Path stays the same but use helper:
   ```bash
   # Old
   cd frontend/nextjs-starter-template && npm run dev
   
   # New
   cd frontend && npm run dev
   # OR use helper
   ./dev-frontend.sh
   ```

3. **Environment variables** - Now required:
   ```bash
   # Backend
   export ALLOWED_ORIGINS="http://localhost:3000"
   
   # Frontend (.env.local)
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. **Examples** - Updated path:
   ```bash
   # Old
   python transformation.py example/file.yaml
   
   # New
   cd backend && python transformation.py ../examples/file.yaml
   ```

### What Moved Where

| Old Location | New Location | Notes |
|-------------|--------------|-------|
| `main.py` | `backend/main.py` | Backend server |
| `transformation.py` | `backend/transformation.py` | Core converter |
| `requirements.txt` | `backend/requirements.txt` | Python deps |
| `frontend/nextjs-starter-template/*` | `frontend/*` | Flattened |
| `example/` | `examples/` | Renamed |
| `SETUP.md` | `docs/SETUP.md` | Documentation |
| `bs/`, `in_progress/`, `new/` | `.archive/exploration/` | Archived |

### Benefits of New Structure

✅ **Deployment Ready** - Clear backend/frontend separation for Koyeb  
✅ **Clean Root** - Fewer files, better organization  
✅ **Easy Development** - Helper scripts for quick start  
✅ **Better Documentation** - Consolidated in docs/  
✅ **Production Focus** - Exploration code archived separately  
✅ **Environment Config** - Proper env variable support  

### Upgrade Path

For existing deployments:

1. Pull latest changes
2. Update deployment configuration to use new directories
3. Set environment variables as documented
4. Redeploy both services

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for details.

