# APIIngest - OpenAPI to LLM-Ready Markdown Converter

🚀 **Full-stack web application** that converts OpenAPI YAML/JSON specifications into structured, LLM-friendly markdown format optimized for AI coding assistants.

[![Deploy to Koyeb](https://img.shields.io/badge/Deploy%20to-Koyeb-blue)](https://www.koyeb.com/)

## ✨ Features

### Converter Features
**Dereferences `$ref` schemas** — Inline references for readability  
**Surfaces authentication** — Security schemes pulled into each endpoint  
**Base URLs highlighted** — Server information prominently displayed  
**Runnable examples** — Auto-generated curl commands with placeholders  
**Strict separators** — Delimiters prevent boundary confusion  (Inspired by GitIngest, see below)
**Tag grouping** — Organized by tags, alphabetically sorted  
**Type normalization** — Clean type display (string (uuid), array<User>, etc.)  
**Token-aware** — Designed to keep endpoint chunks under 2-4K tokens  

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/mohidbt/apic.git
cd apic

# Terminal 1 - Start Backend
cd backend
pip install -r requirements.txt
python main.py

# Terminal 2 - Start Frontend
cd frontend
npm install
npm run dev
```

Then open http://localhost:3000 in your browser!

### Using the Converter

1. **Web Interface** (Recommended)
   - Open http://localhost:3000
   - Drag and drop your OpenAPI YAML/JSON file
   - Click "Convert to Markdown"
   - Download starts automatically!

2. **Command Line**
   ```bash
   cd backend
   python transformation.py ../examples/APIs.guru-swagger.yaml
   ```

3. **API Endpoint**
   ```bash
   curl -X POST http://localhost:8000/convert \
     -F "file=@openapi-spec.yaml" \
     -o output.md
   ```

## 📁 Project Structure

```
apiingest/
├── backend/               # FastAPI server
│   ├── main.py           # API server with file upload
│   ├── transformation.py # Core OpenAPI→Markdown converter
│   ├── requirements.txt  # Python dependencies
│   └── README.md         # Backend documentation
├── frontend/             # Next.js web application
│   ├── src/              # React components and pages
│   ├── public/           # Static assets
│   ├── package.json      # Node dependencies
│   └── .env.example      # Environment variables template
├── examples/             # Example OpenAPI specifications
│   ├── APIs.guru-swagger.yaml
│   ├── APIs.guru-swagger.json
│   └── README.md
├── docs/                 # Documentation
│   ├── SETUP.md         # Detailed setup guide
│   ├── DEPLOYMENT.md    # Koyeb deployment instructions
│   └── QUICK_REFERENCE.md
├── .koyeb/              # Deployment configuration
│   └── config.yaml
└── README.md            # This file
```

## 📖 Output Format

The generated markdown follows a strict, LLM-optimized structure:

### Header Section
```markdown
# API Title
**Version:** 1.0.0

Brief description...

## Base URLs
  - https://api.example.com — Production
  - https://sandbox.api.example.com — Sandbox

## Authentication
  - bearerAuth: HTTP BEARER
  - apiKey: API Key (header: X-API-Key)
```

### Endpoint Blocks

Each endpoint uses strict delimiters (inspired by Gitingest):

```
================================================================================
ENDPOINT: [GET] /users/{id}
TAGS: Users
SUMMARY: Get a user by ID
DESCRIPTION: Retrieves detailed user information...
AUTH: Bearer token

REQUEST
  Path params:
  - id (string (uuid), required)
  Query params:
  - verbose (boolean, optional)
  Body:
  none

RESPONSES
  - 200 (application/json): Success
    - id: string (uuid, required)
    - name: string (required)
    - email: string (email, required)
  - 404: User not found

EXAMPLE (curl)
curl -X GET \
  "https://api.example.com/users/123?verbose=true" \
  -H "Authorization: Bearer $TOKEN"
================================================================================
```

## 🎯 Why This Format?

### LLM Benefits

1. **Strict Delimiters** — `=` bars prevent AI from confusing endpoint boundaries
2. **Dereferenced Schemas** — No need to chase `$ref` pointers during code generation
3. **Inline Auth** — Security requirements visible per-endpoint
4. **Runnable Examples** — Copy-paste curl commands with placeholder variables
5. **Normalized Types** — Consistent type display helps pattern recognition
6. **Tag Grouping** — Logical organization mimics developer thinking
7. **Token-Optimized** — Chunks designed to fit in context windows

### Inspired by Gitingest

This format borrows from [Gitingest](https://gitingest.com/)'s approach:
- Three-section structure (header, TOC, content)
- Repeated delimiters between entries
- Stable, deterministic ordering
- Noise filtering for clarity

## 🌐 Deployment

### Deploy to Koyeb

**Two deployment options:**

#### Option 1: Single Service (Recommended for Simple Deployments)
Deploy backend + frontend together in one container.

See **[KOYEB_SINGLE_SERVICE.md](KOYEB_SINGLE_SERVICE.md)** for detailed instructions.

**Quick steps:**
1. Use root-level `Dockerfile`
2. Set environment variables (PORT, ALLOWED_ORIGINS, etc.)
3. Deploy as one service
4. Both services run together via supervisord

**Environment Variables:**
```bash
PORT=8000
ALLOWED_ORIGINS=https://{{ KOYEB_PUBLIC_DOMAIN }}/
NEXT_PUBLIC_API_URL=http://localhost:8000
NODE_ENV=production
```

#### Option 2: Two Separate Services (Recommended for Production)
Deploy backend and frontend as independent services.

See **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** for complete instructions.

**Quick Overview:**
1. Deploy backend service (FastAPI) from `backend/` directory
2. Deploy frontend service (Next.js) from `frontend/` directory
3. Set environment variables for both services
4. Update CORS settings with deployed URLs

## 🛠️ Technology Stack

### Backend
- **FastAPI** — Modern Python web framework
- **uvicorn** — ASGI server
- **PyYAML** — YAML parsing
- **Python 3.8+**

### Frontend
- **Next.js 15** — React framework
- **TypeScript** — Type safety
- **Tailwind CSS** — Styling
- **shadcn/ui** — UI components
- **Sonner** — Toast notifications

## 📚 Documentation

- **[SETUP.md](docs/SETUP.md)** — Detailed installation and configuration
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** — Koyeb deployment guide
- **[QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)** — Command reference
- **[Backend README](backend/README.md)** — API documentation
- **[Examples](examples/README.md)** — Example specifications

## 🧪 Testing

Try it with the included examples:

```bash
# Backend directory
cd backend

# Convert example spec
python transformation.py ../examples/APIs.guru-swagger.yaml

# Start API server for testing
python main.py
```

## 🤝 Contributing

Contributions welcome! This project prioritizes LLM readability over human aesthetics.

**Key principles:**
1. **Strict structure** — Consistent delimiters and ordering
2. **Inline critical info** — Auth, types, examples per endpoint
3. **Token efficiency** — Truncate where necessary
4. **Deterministic output** — Same input = same output

## 📝 License

MIT — Feel free to use, modify, and distribute.

## 🔗 Related Projects

- [Gitingest](https://gitingest.com/) — LLM-optimized code repository digests

## 💡 Use Cases

- **AI Coding Assistants** — Feed API docs to Claude, GPT, etc.
- **API Documentation** — Generate readable docs from OpenAPI specs
- **Developer Onboarding** — Clear, structured API references
- **RAG Systems** — Token-optimized chunks for retrieval
- **Code Generation** — Help AI understand your API structure

## 🐛 Issues & Support

Found a bug or have a question?
- Open an issue on GitHub
- Check existing [documentation](docs/)
- Try with [example files](examples/)

## 🎉 Acknowledgments

Built with inspiration from:
- Gitingest's LLM-friendly formatting approach
- OpenAPI Specification community
- Modern web development best practices

---

**Made with ❤️ for developers working with LLMs**
