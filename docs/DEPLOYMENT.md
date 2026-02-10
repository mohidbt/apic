# Deployment Guide

This guide covers deploying the APIIngest application to Koyeb.

## Overview

APIIngest is a full-stack application with:
- **Backend**: FastAPI (Python) server on port 8000
- **Frontend**: Next.js application on port 3000

The application is deployed as a **single container** on Koyeb, with both services managed by supervisord.

## Prerequisites

- Koyeb account (sign up at https://www.koyeb.com/)
- GitHub repository with your code
- Git repository connected to Koyeb
- PostgreSQL database (Supabase recommended - see KOYEB_PERSISTENT_DB.md)

## Architecture on Koyeb

```
┌─────────────────────────────────────────┐
│      Koyeb Single Container             │
│                                         │
│  ┌────────────────────────────────┐    │
│  │       Supervisord              │    │
│  │                                │    │
│  │  ┌──────────┐  ┌────────────┐ │    │
│  │  │ Backend  │  │  Frontend  │ │    │
│  │  │ FastAPI  │  │  Next.js   │ │    │
│  │  │ :8000    │◄─┤  :3000     │ │    │
│  │  └────┬─────┘  └────────────┘ │    │
│  └───────┼────────────────────────┘    │
│          │                             │
│          ▼                             │
│    Public Access                       │
│    Port 8000                           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│      External PostgreSQL DB             │
│      (Supabase)                         │
└─────────────────────────────────────────┘
```

### How It Works

1. **Single Container Deployment**: Both frontend and backend run in the same container
2. **Port Exposure**: Only port 8000 (backend) is exposed publicly
3. **Internal Communication**: Frontend SSR calls backend via `localhost:8000` (fast)
4. **Client Communication**: Browser calls backend via public domain
5. **Process Management**: Supervisord manages both processes

## Deployment Steps

### Step 1: Prepare Environment Variables

Create these environment variables in Koyeb:

```bash
# Required
ALLOWED_ORIGINS=https://{{ KOYEB_PUBLIC_DOMAIN }}/
DATABASE_URL=postgresql+psycopg://user:pass@host:5432/db
NEXT_PUBLIC_API_URL=https://{{ KOYEB_PUBLIC_DOMAIN }}
NODE_ENV=production
PORT=8000

# Optional (defaults provided)
DATABASE_PATH=/app/backend/data/apiingest.db  # SQLite fallback if DATABASE_URL not set
LOG_LEVEL=INFO
```

**Important Notes**:
- `{{ KOYEB_PUBLIC_DOMAIN }}` is automatically replaced by Koyeb with your service domain
- `NEXT_PUBLIC_API_URL` is used by the client browser
- Backend uses `localhost:8000` for internal SSR communication (automatic)
- Use PostgreSQL for production (SQLite is for development only)

### Step 2: Deploy to Koyeb

#### Option A: Via Koyeb Dashboard

1. Go to your Koyeb dashboard
2. Click **Create Service**
3. Select your GitHub repository
4. Configure the service:
   - **Name**: `apiingest` (or your preferred name)
   - **Builder**: Docker
   - **Dockerfile**: Use root `Dockerfile`
   - **Port**: 8000 (backend port - publicly exposed)
   - **Health check path**: `/health`

5. Add environment variables from Step 1
6. Click **Deploy**

#### Option B: Via Koyeb CLI

```bash
# Install Koyeb CLI
curl -fsSL https://cli.koyeb.com/install.sh | bash

# Login
koyeb login

# Deploy
koyeb service create apiingest \
  --git github.com/yourusername/apic \
  --git-branch main \
  --docker-dockerfile Dockerfile \
  --ports 8000:http \
  --routes /:8000 \
  --env ALLOWED_ORIGINS=https://\{\{KOYEB_PUBLIC_DOMAIN\}\}/ \
  --env DATABASE_URL=your_postgresql_url \
  --env NEXT_PUBLIC_API_URL=https://\{\{KOYEB_PUBLIC_DOMAIN\}\} \
  --env NODE_ENV=production \
  --env PORT=8000
```

### Step 3: Verify Deployment

After deployment completes:

1. **Check service status**: Should show "Running"
2. **Test backend health**:
   ```bash
   curl https://your-app.koyeb.app/health
   # Should return: {"status":"healthy"}
   ```
3. **Test frontend**: Visit `https://your-app.koyeb.app` in browser
4. **Check logs**: View both backend and frontend logs in Koyeb dashboard

## Server-Side Rendering (SSR) Configuration

The application uses Next.js SSR for optimal performance:

### How SSR Works in This Deployment

1. **Initial Page Load**:
   - User visits marketplace → Request hits backend port 8000
   - Backend proxies to Next.js (port 3000 internally)
   - Next.js SSR fetches data from `http://localhost:8000` (internal)
   - Fully rendered HTML sent to browser (no loading skeleton!)

2. **Client-Side Interactions**:
   - Browser fetches from `NEXT_PUBLIC_API_URL` (public domain)
   - No CORS issues (same domain)

### Performance Benefits

- **No Empty Skeleton**: Users see data immediately on first page load
- **Fast SSR**: Internal `localhost` communication (< 1ms latency)
- **Reduced Bandwidth**: No external HTTP calls during SSR
- **Better SEO**: Fully rendered HTML for search engines

### Code Implementation

The `frontend/src/lib/api.ts` automatically detects the environment:

```typescript
function getApiBaseUrl(): string {
  const isServer = typeof window === 'undefined'
  
  if (isServer) {
    // Server-side: use localhost for internal communication
    return 'http://localhost:8000'
  } else {
    // Client-side: use public URL
    return process.env.NEXT_PUBLIC_API_URL
  }
}
```

## Environment Variables Reference

### Complete Environment Variables

```bash
# Required for Production
ALLOWED_ORIGINS=https://{{ KOYEB_PUBLIC_DOMAIN }}/
DATABASE_URL=postgresql+psycopg://postgres:xxx@db.host.supabase.co:5432/postgres
NEXT_PUBLIC_API_URL=https://{{ KOYEB_PUBLIC_DOMAIN }}
NODE_ENV=production
PORT=8000

# Optional (with defaults)
DATABASE_PATH=/app/backend/data/apiingest.db
LOG_LEVEL=INFO
PYTHONUNBUFFERED=1
```

### Variable Descriptions

| Variable | Used By | Description |
|----------|---------|-------------|
| `ALLOWED_ORIGINS` | Backend | CORS configuration (trailing `/` required) |
| `DATABASE_URL` | Backend | PostgreSQL connection string (Supabase) |
| `NEXT_PUBLIC_API_URL` | Frontend (client) | Public API URL for browser requests |
| `NODE_ENV` | Both | Set to `production` for optimizations |
| `PORT` | Backend | Backend server port (must be 8000) |
| `DATABASE_PATH` | Backend | SQLite fallback path (dev only) |
| `LOG_LEVEL` | Backend | Logging verbosity (INFO/DEBUG/WARNING) |

## Container Build Process

The Dockerfile uses a multi-stage build:

1. **Stage 1**: Build Next.js frontend
   - Uses Node.js 20 Alpine
   - Installs dependencies
   - Runs production build
   - Outputs optimized static files

2. **Stage 2**: Combine backend + frontend
   - Uses Python 3.11 slim
   - Installs Node.js for Next.js runtime
   - Copies backend code and installs Python dependencies
   - Copies built frontend from Stage 1
   - Configures supervisord to manage both processes

3. **Runtime**: Both services start via supervisord
   - Backend: `uvicorn main:app --host 0.0.0.0 --port 8000`
   - Frontend: `npm start` (Next.js production server)

## Custom Domains (Optional)

### Adding a Custom Domain

1. Go to your service in Koyeb dashboard
2. Navigate to **Settings** → **Domains**
3. Click **Add Domain**
4. Enter your custom domain (e.g., `api.yourdomain.com`)
5. Update DNS records as instructed by Koyeb:
   ```
   Type: CNAME
   Name: api (or @)
   Value: <your-service>.koyeb.app
   ```

### Update Environment Variables

After adding a custom domain, update:

```bash
ALLOWED_ORIGINS=https://yourdomain.com/,https://www.yourdomain.com/
NEXT_PUBLIC_API_URL=https://yourdomain.com
```

Redeploy the service for changes to take effect.

## Monitoring and Logs

### View Logs

Koyeb provides real-time logs for both services:

1. Go to service dashboard
2. Click **Logs** tab
3. You'll see interleaved logs from both:
   - `[backend]` - FastAPI logs
   - `[frontend]` - Next.js logs
   - `[supervisord]` - Process management logs

### Health Monitoring

The backend includes a health endpoint:

```bash
curl https://your-app.koyeb.app/health
# Returns: {"status": "healthy"}
```

Configure Koyeb health checks:
- **Path**: `/health`
- **Port**: 8000
- **Interval**: 30s
- **Timeout**: 10s
- **Retries**: 3

### Metrics

Monitor in Koyeb dashboard:
- **CPU Usage**: Track processing load
- **Memory Usage**: Monitor for memory leaks
- **Request Rate**: API call frequency
- **Response Time**: API latency

## Database Configuration

### Using Supabase PostgreSQL

1. Create a Supabase project
2. Get connection string from Settings → Database
3. Add to Koyeb environment variables:
   ```bash
   DATABASE_URL=postgresql+psycopg://postgres:xxx@db.xxx.supabase.co:5432/postgres
   ```

### Important Notes

- **DO NOT use SQLite in production** (container filesystem is ephemeral)
- PostgreSQL connection pooling is handled automatically
- Database schema is created automatically on first run
- See `KOYEB_PERSISTENT_DB.md` for detailed database setup

## Troubleshooting

### CORS Errors

**Problem**: `Access-Control-Allow-Origin` errors in browser console

**Solutions**:
- Ensure `ALLOWED_ORIGINS` includes your domain with trailing `/`
  ```bash
  ALLOWED_ORIGINS=https://your-app.koyeb.app/
  ```
- If using custom domain, add both with and without www:
  ```bash
  ALLOWED_ORIGINS=https://yourdomain.com/,https://www.yourdomain.com/
  ```
- Redeploy service after updating environment variables

### Build Failures

**Problem**: Service fails to build or deploy

**Solutions**:
- Check build logs in Koyeb dashboard for specific errors
- Verify Dockerfile exists in repository root
- Ensure all dependencies are listed:
  - Python: `backend/requirements.txt`
  - Node.js: `frontend/package.json`
- Check that Docker build context has access to all files

### SSR Data Fetching Issues

**Problem**: Marketplace page shows empty table or errors during SSR

**Solutions**:
- Verify backend is running: `curl https://your-app.koyeb.app/health`
- Check that port 8000 is exposed in Koyeb service configuration
- Review logs for connection errors between frontend and backend
- Ensure `supervisord` is managing both processes correctly

### Database Connection Errors

**Problem**: `connection refused` or `database does not exist`

**Solutions**:
- Verify `DATABASE_URL` format:
  ```bash
  postgresql+psycopg://user:pass@host:5432/dbname
  ```
- Check Supabase database is running and accessible
- Verify database credentials are correct
- Check IP allowlist in Supabase (allow Koyeb IPs or use `0.0.0.0/0`)

### Frontend Not Loading

**Problem**: Frontend page shows 502 or doesn't respond

**Solutions**:
- Check that both processes are running in logs
- Verify port 3000 is accessible internally (not publicly exposed)
- Check supervisord configuration is correct
- Restart service if processes have crashed

### Memory Issues

**Problem**: Service restarts due to OOM (Out of Memory)

**Solutions**:
- Upgrade instance size in Koyeb
- Monitor memory usage in dashboard
- Check for memory leaks in application logs
- Consider separating frontend/backend if needed

## Scaling

### Vertical Scaling (Instance Size)

Increase resources for a single instance:
1. Go to service settings in Koyeb
2. Change **Instance Type**:
   - **Nano**: 0.1 vCPU, 512 MB RAM (development)
   - **Micro**: 0.5 vCPU, 1 GB RAM (small production)
   - **Small**: 1 vCPU, 2 GB RAM (recommended for production)
   - **Medium**: 2 vCPU, 4 GB RAM (high traffic)
3. Click **Update** and redeploy

### Horizontal Scaling (Multiple Instances)

Run multiple instances for high availability:
1. Go to service settings
2. Adjust **Instance Count** (2-10 instances)
3. Koyeb automatically load balances across instances

**Note**: Each instance needs its own connection to shared PostgreSQL database

### Recommended Scaling Strategy

- **Development**: 1 × Nano instance
- **Small Production**: 1 × Micro instance
- **Medium Production**: 2 × Small instances
- **High Traffic**: 3-5 × Small instances or 2 × Medium instances

## Cost Optimization

### Free Tier Usage

Koyeb offers a generous free tier:
- 2 web services
- Shared CPU (0.1 vCPU)
- 512 MB RAM per service
- 5 GB bandwidth/month

**Tip**: Use free tier for development and testing

### Production Cost Optimization

1. **Right-size instances**: Don't over-provision
2. **Monitor usage**: Use Koyeb dashboards to track actual resource usage
3. **Auto-scaling**: Set up min/max instance counts based on traffic patterns
4. **Database**: Use Supabase free tier (500 MB, 50 MB file uploads)
5. **CDN**: Enable Koyeb CDN for static assets

### Estimated Costs (Single Instance)

- **Nano** (0.1 vCPU, 512 MB): ~$0/month (free tier)
- **Micro** (0.5 vCPU, 1 GB): ~$5-10/month
- **Small** (1 vCPU, 2 GB): ~$15-20/month
- **Medium** (2 vCPU, 4 GB): ~$30-40/month

*Prices are approximate and subject to change*

## Security Best Practices

1. **Never commit sensitive data**:
   - Add `.env`, `.env.local` to `.gitignore`
   - Never commit database credentials or API keys
   - Use Koyeb's secret management for sensitive env vars

2. **Environment Variables**:
   - Use Koyeb environment variables (encrypted at rest)
   - Rotate database passwords regularly
   - Use strong, unique passwords for PostgreSQL

3. **HTTPS/TLS**:
   - HTTPS is automatic with Koyeb (free Let's Encrypt certificates)
   - Always use HTTPS URLs in `NEXT_PUBLIC_API_URL` and `ALLOWED_ORIGINS`

4. **CORS Configuration**:
   - Restrict `ALLOWED_ORIGINS` to specific domains (no wildcards)
   - Include trailing `/` in origin URLs
   - Example:
     ```bash
     ALLOWED_ORIGINS=https://yourdomain.com/,https://www.yourdomain.com/
     ```

5. **Dependency Management**:
   - Keep Python and Node.js dependencies updated
   - Run `npm audit` and `pip-audit` regularly
   - Review security advisories for critical packages

6. **Database Security**:
   - Use Supabase Row Level Security (RLS)
   - Never expose database credentials in frontend code
   - Use connection pooling to prevent connection exhaustion

## Local Testing Before Deploy

Test the production build locally with Docker:

```bash
# Build the production container
docker build -t apiingest:local .

# Run with production-like environment
docker run -p 8000:8000 \
  -e ALLOWED_ORIGINS="http://localhost:8000/" \
  -e DATABASE_URL="postgresql://..." \
  -e NEXT_PUBLIC_API_URL="http://localhost:8000" \
  -e NODE_ENV="production" \
  -e PORT="8000" \
  apiingest:local
```

Visit http://localhost:8000 to test.

### Alternative: Test with Docker Compose

For development with hot reload:

```bash
# Start both services
docker-compose up

# Backend: http://localhost:8000
# Frontend: http://localhost:3000
```

## Quick Start Summary

1. **Set up database**: Create Supabase PostgreSQL database
2. **Configure Koyeb**: Add environment variables
3. **Deploy**: Push to GitHub, Koyeb auto-deploys
4. **Verify**: Test `/health` endpoint and frontend
5. **Monitor**: Check logs and metrics

## Environment Variables Checklist

Before deploying, ensure you have:

- [ ] `ALLOWED_ORIGINS` - Your domain with trailing `/`
- [ ] `DATABASE_URL` - Supabase PostgreSQL connection string
- [ ] `NEXT_PUBLIC_API_URL` - Your public domain (client-side)
- [ ] `NODE_ENV` - Set to `production`
- [ ] `PORT` - Set to `8000`

## Post-Deployment Checklist

After deploying, verify:

- [ ] Service status shows "Running"
- [ ] Health endpoint responds: `curl https://your-app.koyeb.app/health`
- [ ] Frontend loads without errors
- [ ] Marketplace page shows data immediately (no skeleton on first load)
- [ ] API specs can be uploaded
- [ ] Database persists data across deploys
- [ ] Logs show both backend and frontend running
- [ ] SSL certificate is valid (HTTPS works)

## Support and Resources

### Documentation

- **Koyeb Documentation**: https://www.koyeb.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Next.js Docs**: https://nextjs.org/docs
- **Supabase Docs**: https://supabase.com/docs

### Getting Help

- **Project Issues**: [GitHub Issues](https://github.com/mohidbt/apic/issues)
- **Koyeb Support**: https://www.koyeb.com/support
- **Koyeb Community**: Koyeb Discord/Slack

### Related Documentation

- `KOYEB_PERSISTENT_DB.md` - Detailed database setup with Supabase
- `PROJECT_STATUS.md` - Current project status and features
- `README.md` - Project overview and local development setup

## Deployment Architecture Summary

```
User Request
    ↓
Koyeb Load Balancer (HTTPS)
    ↓
Container (Port 8000)
    ↓
┌─────────────────────────────┐
│      Supervisord           │
│  ┌──────────┐  ┌──────────┐│
│  │ FastAPI  │←─┤ Next.js  ││
│  │ :8000    │  │ :3000    ││
│  │ (public) │  │(internal)││
│  └────┬─────┘  └──────────┘│
└───────┼────────────────────┘
        ↓
    Supabase PostgreSQL
```

**Key Points**:
- Single container, dual process
- Only port 8000 exposed publicly
- SSR uses localhost for fast internal API calls
- Client uses public domain for API calls
- PostgreSQL for persistent storage

---

**Last Updated**: February 2026  
**Deployment Type**: Single Container (Backend + Frontend)  
**Platform**: Koyeb  
**Database**: Supabase PostgreSQL

