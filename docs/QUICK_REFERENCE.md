# Quick Reference Card

## 🚀 Start the Application

```bash
# Terminal 1 - Backend
./start-backend.sh
# or manually: python main.py

# Terminal 2 - Frontend  
./start-frontend.sh
# or manually: cd frontend && npm run dev
```

## 🌐 Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://localhost:3000 | Web interface |
| Backend API | http://localhost:8000 | REST API |
| API Docs | http://localhost:8000/docs | Swagger UI |
| Health Check | http://localhost:8000/health | Status check |

## 📝 File Types Supported

- `.yaml` - OpenAPI YAML specification
- `.yml` - OpenAPI YAML specification (alternate extension)
- `.json` - OpenAPI JSON specification

## 🔄 Conversion Flow

```
1. Upload file → 2. Validate → 3. Convert → 4. Download
   (Frontend)     (Frontend)    (Backend)    (Automatic)
```

## 📡 API Usage

### Upload & Convert
```bash
curl -X POST http://localhost:8000/convert \
  -F "file=@your-api-spec.yaml" \
  -o output.md
```

### Health Check
```bash
curl http://localhost:8000/health
```

## 🎯 Command Line (Direct)

```bash
# Use the transformation script directly
python transformation.py input.yaml output.md
```

## 📁 Example Files

Test with provided examples:
```bash
example/APIs.guru-swagger.json
example/APIs.guru-swagger.yaml
```

## 🐛 Troubleshooting

### Backend not starting?
```bash
pip install -r requirements.txt
```

### Frontend not starting?
```bash
cd frontend
npm install
```

### Port conflicts?
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### CORS errors?
- Ensure backend is on port 8000
- Ensure frontend is on port 3000
- Check browser console

## 📦 Dependencies

### Backend (Python)
- PyYAML
- FastAPI
- Uvicorn
- python-multipart

### Frontend (Node.js)
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- shadcn/ui

## 🎨 UI Components Used

- File input (hidden)
- Upload area (drag-and-drop)
- Button (convert action)
- Toast notifications (feedback)
- Icons (Upload, FileText, Loader2)

## ✅ Quick Test

1. Start both servers
2. Open http://localhost:3000
3. Upload `example/APIs.guru-swagger.json`
4. Click "Convert to Markdown"
5. File downloads as `APIs.guru-swagger.md`

## 📚 Documentation

- **README.md** - Overview and features
- **SETUP.md** - Detailed setup instructions
- **INTEGRATION_COMPLETE.md** - Technical details
- **QUICK_REFERENCE.md** - This file

## 🔑 Key Files

| File | Purpose |
|------|---------|
| `backend/main.py` | FastAPI backend server |
| `backend/transformation.py` | Core conversion logic |
| `frontend/src/app/[locale]/page.tsx` | Main UI component |
| `frontend/src/app/[locale]/layout.tsx` | Root layout |

## 💡 Pro Tips

1. Use helper scripts (`start-*.sh`) for convenience
2. Check API docs at `/docs` for testing
3. Use browser DevTools to debug frontend
4. Check terminal logs for backend errors
5. Test with example files first

## 🎯 Common Use Cases

### Convert Single File
Upload via web interface or use API

### Batch Convert (Command Line)
```bash
for file in *.yaml; do
  python transformation.py "$file" "${file%.yaml}.md"
done
```

### Integrate in CI/CD
```bash
curl -X POST http://your-api/convert \
  -F "file=@openapi.yaml" \
  -o docs/api-reference.md
```

## 🔒 Security Notes

- No authentication required (local dev)
- Files processed in memory
- Temp files cleaned up automatically
- No data stored permanently
- Add auth for production use

## 📊 Performance

- Small files (< 1MB): < 1 second
- Medium files (1-10MB): 1-5 seconds
- Large files (> 10MB): 5+ seconds

## 🌟 What Gets Generated

- Structured markdown document
- Table of contents by tag
- Endpoint details with examples
- Runnable curl commands
- Authentication requirements
- Request/response schemas
- Components appendix

## 📞 Support

For detailed information, see:
- `SETUP.md` for installation help
- `INTEGRATION_COMPLETE.md` for technical details
- `README.md` for feature overview

