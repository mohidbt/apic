# Quick Start Guide

Get APIIngest running in 2 minutes!

## 🚀 Super Quick Start

```bash
# Terminal 1 - Backend
./dev-backend.sh

# Terminal 2 - Frontend  
./dev-frontend.sh
```

Open http://localhost:3000 and start converting! 🎉

## 📋 Prerequisites

- **Python 3.8+** - Check: `python3 --version`
- **Node.js 20+** - Check: `node --version`
- **npm** - Check: `npm --version`

## 🔧 Manual Setup

If the helper scripts don't work on your system:

### Backend

```bash
cd backend

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start server
python main.py
```

Server runs on http://localhost:8000
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Start dev server
npm run dev
```

Frontend runs on http://localhost:3000

## 🎯 First Conversion

### Using the Web UI

1. Open http://localhost:3000
2. Drag & drop `examples/APIs.guru-swagger.yaml`
3. Click "Convert to Markdown"
4. File downloads automatically!

### Using Command Line

```bash
cd backend
python transformation.py ../examples/APIs.guru-swagger.yaml
# Output: APIs.guru-swagger.md
```

### Using the API

```bash
curl -X POST http://localhost:8000/convert \
  -F "file=@examples/APIs.guru-swagger.yaml" \
  -o output.md
```

## 🐳 Docker (Alternative)

```bash
# Start both services
docker-compose up

# Access:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:8000
```

## 🌐 Deploy to Koyeb

1. Push code to GitHub
2. Connect repository to Koyeb
3. Create two services:
   - **Backend**: Working dir `backend/`, Port 8000
   - **Frontend**: Working dir `frontend/`, Port 3000
4. Set environment variables (see [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md))

## 📚 Next Steps

- **[README.md](README.md)** - Full project overview
- **[docs/SETUP.md](docs/SETUP.md)** - Detailed setup guide
- **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Production deployment
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute

## 🆘 Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8000 (backend)
lsof -ti:8000 | xargs kill -9

# Kill process on port 3000 (frontend)
lsof -ti:3000 | xargs kill -9
```

### Module Not Found (Python)

```bash
cd backend
pip install -r requirements.txt
```

### Module Not Found (Node)

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### CORS Errors

Make sure:
1. Backend is running on port 8000
2. Frontend `.env.local` has `NEXT_PUBLIC_API_URL=http://localhost:8000`
3. No trailing slashes in URLs

### Backend Won't Start

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

## 💡 Tips

- Use `./dev-backend.sh` and `./dev-frontend.sh` for easiest setup
- Check example files in `examples/` directory
- View API docs at http://localhost:8000/docs while backend is running
- Frontend hot-reloads on code changes
- Backend auto-reloads on code changes

## 📞 Need Help?

- Check [docs/](docs/) for detailed documentation
- See [examples/](examples/) for sample files
- Open an issue on GitHub

---

**Happy converting! 🚀**

