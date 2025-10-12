# Deployment Guide

This guide covers deploying the APIIngest application to Koyeb.

## Overview

APIIngest is a full-stack application with:
- **Backend**: FastAPI (Python) server on port 8000
- **Frontend**: Next.js application on port 3000

Both can be deployed together on Koyeb as separate services in the same project.

## Prerequisites

- Koyeb account (sign up at https://www.koyeb.com/)
- GitHub repository with your code
- Git repository connected to Koyeb

## Architecture on Koyeb

```
┌─────────────────────────────────────┐
│         Koyeb Project               │
│                                     │
│  ┌──────────────┐  ┌─────────────┐ │
│  │   Backend    │  │  Frontend   │ │
│  │   Service    │  │   Service   │ │
│  │ (FastAPI)    │  │ (Next.js)   │ │
│  │ Port: 8000   │  │ Port: 3000  │ │
│  └──────────────┘  └─────────────┘ │
│         ▲                 │         │
│         └─────────────────┘         │
│           API calls                 │
└─────────────────────────────────────┘
```

## Step 1: Deploy Backend

### 1.1 Create Backend Service

1. Go to your Koyeb dashboard
2. Click **Create Service**
3. Select your GitHub repository
4. Configure the service:
   - **Name**: `apiingest-backend`
   - **Builder**: Dockerfile or Buildpack
   - **Build command**: (leave empty if using Dockerfile)
   - **Run command**: `uvicorn main:app --host 0.0.0.0 --port 8000`
   - **Working directory**: `backend`
   - **Port**: 8000

### 1.2 Set Environment Variables

Add these environment variables to the backend service:

| Variable | Value | Description |
|----------|-------|-------------|
| `ALLOWED_ORIGINS` | `https://your-frontend-url.koyeb.app` | CORS allowed origins |
| `PORT` | `8000` | Server port |

**Note**: Update `ALLOWED_ORIGINS` after deploying the frontend.

### 1.3 Deploy

Click **Deploy** and wait for the build to complete. Note the backend URL (e.g., `https://apiingest-backend-xxx.koyeb.app`).

## Step 2: Deploy Frontend

### 2.1 Create Frontend Service

1. Click **Create Service** again
2. Select your GitHub repository
3. Configure the service:
   - **Name**: `apiingest-frontend`
   - **Builder**: Buildpack (auto-detects Next.js)
   - **Build command**: `npm install && npm run build`
   - **Run command**: `npm start`
   - **Working directory**: `frontend`
   - **Port**: 3000

### 2.2 Set Environment Variables

Add these environment variables to the frontend service:

| Variable | Value | Description |
|----------|-------|-------------|
| `NEXT_PUBLIC_API_URL` | `https://apiingest-backend-xxx.koyeb.app` | Backend API URL |
| `NODE_ENV` | `production` | Node environment |

**Important**: Use the backend URL from Step 1.3.

### 2.3 Deploy

Click **Deploy** and wait for the build to complete.

## Step 3: Update CORS Settings

After both services are deployed:

1. Go to backend service settings
2. Update `ALLOWED_ORIGINS` environment variable with the frontend URL
3. Redeploy the backend service

Example:
```
ALLOWED_ORIGINS=https://apiingest-frontend-xxx.koyeb.app,https://your-custom-domain.com
```

## Custom Domains (Optional)

### Backend Domain
1. Go to backend service → **Domains**
2. Add custom domain (e.g., `api.yourdomain.com`)
3. Update DNS records as instructed
4. Update frontend's `NEXT_PUBLIC_API_URL` to use the custom domain

### Frontend Domain
1. Go to frontend service → **Domains**
2. Add custom domain (e.g., `yourdomain.com`)
3. Update DNS records as instructed
4. Update backend's `ALLOWED_ORIGINS` to include the custom domain

## Environment Variables Reference

### Backend (`backend/`)

```bash
# Required
ALLOWED_ORIGINS=https://your-frontend.koyeb.app

# Optional
PORT=8000
```

### Frontend (`frontend/`)

```bash
# Required
NEXT_PUBLIC_API_URL=https://your-backend.koyeb.app

# Optional
NODE_ENV=production
```

## Dockerfile (Optional)

If you prefer using Docker, create these files:

### `backend/Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `frontend/Dockerfile`

```dockerfile
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:20-alpine AS runner

WORKDIR /app

COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

CMD ["npm", "start"]
```

## Monitoring

Koyeb provides built-in monitoring:
- View logs in the service dashboard
- Monitor CPU/memory usage
- Set up health checks on `/health` endpoint (backend)

## Health Checks

The backend includes a `/health` endpoint for monitoring:

```bash
curl https://your-backend.koyeb.app/health
# Returns: {"status": "healthy"}
```

## Troubleshooting

### CORS Errors
- Ensure `ALLOWED_ORIGINS` includes the frontend URL
- Check that URLs don't have trailing slashes
- Redeploy backend after updating environment variables

### Build Failures
- Check build logs in Koyeb dashboard
- Verify `package.json` scripts exist (`build`, `start`)
- Ensure all dependencies are in `requirements.txt` or `package.json`

### Connection Refused
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check backend service is running
- Ensure port 8000 is exposed in backend

### 404 Errors
- Verify working directory is set correctly (`backend/` or `frontend/`)
- Check run command paths are relative to working directory

## Scaling

Koyeb allows you to scale services:
1. Go to service settings
2. Adjust instance size or count
3. Apply changes

For this application:
- **Backend**: Scale based on conversion requests
- **Frontend**: Scale based on traffic

## Cost Optimization

- Use Koyeb's free tier for testing
- Scale down during low-traffic periods
- Monitor usage in the dashboard

## Security

1. **Never commit** `.env` files
2. Use environment variables for all secrets
3. Enable HTTPS (automatic with Koyeb)
4. Restrict CORS to specific domains
5. Keep dependencies updated

## Support

- **Koyeb Docs**: https://www.koyeb.com/docs
- **Project Issues**: GitHub repository issues
- **Community**: Koyeb Discord/Slack

## Local Testing Before Deploy

Test the production configuration locally:

```bash
# Terminal 1 - Backend
cd backend
export ALLOWED_ORIGINS="http://localhost:3000"
python main.py

# Terminal 2 - Frontend
cd frontend
export NEXT_PUBLIC_API_URL="http://localhost:8000"
npm run build
npm start
```

Visit http://localhost:3000 to test.

