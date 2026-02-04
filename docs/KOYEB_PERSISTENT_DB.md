# Koyeb Database Persistence (Updated for Free Tier)

## Problem: Koyeb Free Doesn't Support Volumes

**Important**: Koyeb Free tier **does not support persistent volumes**. If you try to add a volume, you'll see this message:

> "Volumes are not supported on the Free instance type"

This means data stored in the container (like `/app/backend/data/apiingest.db`) gets wiped on every deployment.

## Solution: External Database (Zero Cost)

Instead of relying on Koyeb volumes, use a **free external database service**. Your data lives outside the container and persists across all deployments.

### Recommended: Supabase PostgreSQL (Free)

Supabase offers 500MB of PostgreSQL storage for free, which is more than enough for hundreds of API specs.

#### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up
2. Create a new project
3. Wait for it to initialize (~2 minutes)
4. Go to **Settings** → **Database**
5. Find the **Connection String** under "Connection string"
   - Format: `postgresql://postgres:[PASSWORD]@[HOST]:5432/postgres`
   - Copy the URI format

#### Step 2: Prepare Connection String

SQLAlchemy requires a specific format. Modify your connection string:

```
# Original Supabase format:
postgresql://postgres:password@host.supabase.co:5432/postgres

# Change to (for psycopg3):
postgresql+psycopg://postgres:password@host.supabase.co:5432/postgres
```

#### Step 3: Configure Koyeb

1. Open your Koyeb service dashboard
2. Go to **Settings** → **Environment variables**
3. Add a new variable:
   - **Name**: `DATABASE_URL`
   - **Value**: Your modified connection string (with `postgresql+psycopg://`)
4. Save changes
5. Redeploy your service

#### Step 4: Verify

1. After deployment completes, visit your app
2. Upload an API spec
3. Trigger another deployment (push any change to git)
4. Check the marketplace - your spec should still be there! ✅

### Alternative: Neon PostgreSQL (Free)

Neon is another excellent free option with 10GB storage on the free tier.

1. Go to [neon.tech](https://neon.tech)
2. Create account and project
3. Copy connection string (already in correct format)
4. Add to Koyeb as `DATABASE_URL`
5. Deploy!

### How It Works

The updated codebase (`backend/models/database.py`) automatically detects which database to use:

```python
# In production (Koyeb):
DATABASE_URL = "postgresql+psycopg://..." → Uses external Postgres

# In local development:
DATABASE_URL not set → Uses SQLite (./data/apiingest.db)
```

No code changes needed - just set the environment variable!

## Data Migration

If you have existing specs in production that you want to preserve:

### Export Current Data

Before switching to external database:

```bash
# Export all current specs
curl https://api-ingest.com/api/specs?limit=1000 > backup-specs.json
```

### Re-import After Setup

After configuring the external database, you can:
1. **Option A**: Re-upload specs manually through the UI
2. **Option B**: Use the bulk import (see below)

## Backup Strategy (Recommended)

With external databases, backups are usually handled by the provider:

- **Supabase**: Automatic daily backups (can restore from dashboard)
- **Neon**: Point-in-time restore available
- **Manual**: Export via API endpoint

### Manual Export via API

```bash
# Export all specs as JSON
curl https://api-ingest.com/api/specs?limit=1000 > backup-$(date +%Y%m%d).json
```

## Troubleshooting

### "Connection refused" or "Could not connect"
- Check that `DATABASE_URL` is set correctly in Koyeb
- Verify the connection string format: `postgresql+psycopg://...`
- Make sure your database provider (Supabase/Neon) is active

### "relation does not exist"
- The database tables haven't been created yet
- They're auto-created on first startup via `init_db()`
- Check logs for any errors during initialization

### "Still using SQLite in production"
- `DATABASE_URL` environment variable not set
- Check Koyeb environment variables
- Make sure to redeploy after adding the variable

## Cost Comparison

| Provider | Free Tier | After Free | Best For |
|----------|-----------|------------|----------|
| **Supabase** | 500MB, unlimited API | $25/mo | Production apps |
| **Neon** | 10GB, 3 projects | $19/mo | More storage needs |
| Railway | 512MB | $5/mo usage | Hobby projects |

All options have generous free tiers perfect for your use case!
