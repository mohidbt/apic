# Koyeb Single-Service Deployment Guide

This guide covers deploying the entire APIIngest application (backend + frontend) as a **single Koyeb service** using the root-level Dockerfile.

## 🎯 Overview

The root `Dockerfile` combines both:
- **Backend**: FastAPI (Python) on port 8000
- **Frontend**: Next.js on port 3000

Both services run together using supervisord as a process manager.

## 📋 Prerequisites

- Koyeb account (sign up at https://www.koyeb.com/)
- GitHub repository connected to Koyeb
- This repository with the root-level `Dockerfile`

## 🚀 Deployment Steps

### Step 1: Create New Service on Koyeb

1. Go to your Koyeb dashboard
2. Click **Create Service**
3. Select your GitHub repository (`mohidbt/apic` or your repo)
4. Select branch: `main`

### Step 2: Configure Builder (Section +3)

Click on **Builder** section and configure:

#### Build Method
- Select: **Dockerfile** ✅

#### Dockerfile Configuration
- **Dockerfile location**: Leave empty (uses root `Dockerfile`)
- **Entrypoint**: Leave empty (uses Dockerfile's CMD)
- **Command**: Leave empty (uses Dockerfile's CMD)
- **Target**: Leave empty
- **Work directory**: Leave empty (uses `/app` from Dockerfile)

#### Advanced Options
- **Privileged**: Leave unchecked

### Step 3: Configure Environment Variables (Section +4)

Click on **Environment variables and files** section.

Click **+ Add another** for each variable:

| Name | Value |
|------|-------|
| `PORT` | `8000` |
| `ALLOWED_ORIGINS` | `https://{{ KOYEB_PUBLIC_DOMAIN }}/,http://localhost:3000` |
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` |
| `NODE_ENV` | `production` |

**Note**: The special Koyeb variable `{{ KOYEB_PUBLIC_DOMAIN }}` will be replaced with your actual domain.

### Step 4: Configure Ports (Section +8)

The default port should be set to **8000** (the backend port).

- **Port**: `8000`
- **Protocol**: HTTP

**Important**: Koyeb will expose port 8000 publicly. The frontend on port 3000 will proxy API requests to `localhost:8000` internally.

### Step 5: Health Checks (Section +9)

Should automatically detect:
- **Type**: TCP health check
- **Port**: 8000

Or configure HTTP health check:
- **Path**: `/health`
- **Port**: 8000
- **Protocol**: HTTP

### Step 6: Instance Configuration (Section +5)

For free tier:
- **Instance**: Free (0.1 vCPU, 512MB RAM, 2000MB Disk)
- **Region**: Choose closest to your users

### Step 7: Service Name (Section +0)

- **Service name**: `apiingest` (or any name you prefer)

### Step 8: Deploy!

Click **Deploy** button and wait for:
1. Build to complete (~3-5 minutes)
2. Container to start
3. Health checks to pass

## 📊 How It Works

```
┌─────────────────────────────────────────┐
│         Koyeb Service                   │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │     Docker Container              │ │
│  │                                   │ │
│  │  ┌──────────┐    ┌─────────────┐ │ │
│  │  │ Backend  │    │  Frontend   │ │ │
│  │  │ FastAPI  │◄───┤  Next.js    │ │ │
│  │  │ :8000    │    │  :3000      │ │ │
│  │  └────▲─────┘    └─────────────┘ │ │
│  │       │                           │ │
│  │   supervisord                     │ │
│  └───────┼───────────────────────────┘ │
│          │                             │
│   Exposed Port: 8000                   │
└──────────┼─────────────────────────────┘
           │
    Public Internet
```

## 🔍 Verification

After deployment:

1. **Check Service Status**: Should show "Healthy" in Koyeb dashboard
2. **Test Backend API**:
   ```bash
   curl https://your-service.koyeb.app/health
   # Should return: {"status":"healthy"}
   ```

3. **Access Frontend**: 
   - Open browser to: `https://your-service.koyeb.app`
   - Note: You'll need to configure the frontend to be served on port 8000 or use a reverse proxy

## ⚠️ Important Notes

### Port Exposure
- Koyeb only exposes **one port** per service (port 8000 in this config)
- Frontend runs on port 3000 internally but is **not publicly accessible**
- You'll need to set up a reverse proxy in the backend to serve the frontend

### Adding Reverse Proxy to Backend

To make this work properly, you need to update `backend/main.py` to serve the frontend:

```python
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Add this after creating the FastAPI app
app.mount("/_next", StaticFiles(directory="../frontend/.next/static"), name="static")
app.mount("/static", StaticFiles(directory="../frontend/public"), name="public")

@app.get("/")
async def root():
    return FileResponse("../frontend/.next/server/pages/index.html")
```

**OR** configure Nginx/Caddy as a reverse proxy (recommended for production).

## 🐛 Troubleshooting

### Build Fails
- Check build logs in Koyeb dashboard
- Verify `package.json` has `build` and `start` scripts
- Ensure `requirements.txt` has all dependencies

### Service Won't Start
- Check runtime logs
- Verify supervisord is starting both processes
- Check environment variables are set correctly

### CORS Errors
- Verify `ALLOWED_ORIGINS` includes your domain
- Check that backend allows requests from the frontend

### Frontend Not Loading
- This is expected with current setup - port 3000 is not exposed
- You need to add reverse proxy to backend (see above)
- Or deploy as two separate services (see `docs/DEPLOYMENT.md`)

## 🔄 Alternative: Two-Service Deployment

If you need the frontend and backend on separate domains, use the two-service deployment approach described in `docs/DEPLOYMENT.md`.

## 📝 Environment Variables Reference

| Variable | Purpose | Default |
|----------|---------|---------|
| `PORT` | Main exposed port | `8000` |
| `ALLOWED_ORIGINS` | CORS allowed origins | Required |
| `NEXT_PUBLIC_API_URL` | Backend API URL for frontend | `http://localhost:8000` |
| `NODE_ENV` | Node environment | `production` |

## 💰 Costs

- **Free tier**: Includes 2 services with limited resources
- **Nano instance**: ~$5/month for better performance
- **Micro instance**: ~$10/month for production workloads

## 🔐 Security

1. Set `ALLOWED_ORIGINS` to only your domain (remove `http://localhost:3000` in production)
2. Use HTTPS (automatic with Koyeb)
3. Keep dependencies updated
4. Monitor logs for suspicious activity

## 📞 Support

- **Koyeb Docs**: https://www.koyeb.com/docs
- **Project Issues**: GitHub repository
- **Koyeb Community**: Discord

---

**Need help?** Check the [two-service deployment guide](docs/DEPLOYMENT.md) for a simpler alternative.

