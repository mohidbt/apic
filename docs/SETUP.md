# Setup Guide

Use this guide for local development when you want more detail than `QUICKSTART.md`.

## Prerequisites

- Python 3.8+
- Node.js 20+
- npm

## Repository Layout

- `backend/` - FastAPI API + conversion logic
- `frontend/` - Next.js web app
- `examples/` - sample API specs for local testing

## Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```

Backend endpoints:

- API root: `http://localhost:8000/api`
- Swagger docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

## Frontend Setup

```bash
cd frontend
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
npm run dev
```

Frontend URL:

- App: `http://localhost:3000`

## API Smoke Test

```bash
curl -X POST "http://localhost:8000/api/convert?save_to_db=false" \
  -F "file=@examples/APIs.guru-swagger.yaml"
```

Expected response:

- HTTP `202`
- JSON containing a `job_id`

Then poll/download:

```bash
curl "http://localhost:8000/api/convert/<job_id>"
curl -o output.md "http://localhost:8000/api/convert/<job_id>/download"
```

## Common Issues

### Backend import/module errors

```bash
cd backend
pip install -r requirements.txt
```

### Frontend dependency issues

```bash
cd frontend
rm -rf node_modules
npm install
```

### CORS issues

Ensure:

1. Backend is running on `:8000`
2. Frontend uses `NEXT_PUBLIC_API_URL=http://localhost:8000`
3. `ALLOWED_ORIGINS` includes frontend origin when customized

## Related Docs

- `QUICKSTART.md` - fastest local startup
- `docs/DEPLOYMENT.md` - production deployment
- `backend/README.md` - backend-specific details

