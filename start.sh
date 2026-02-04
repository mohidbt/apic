#!/bin/bash
set -e

# Create log directory
mkdir -p /var/log/supervisor

# Create database directory with proper permissions
mkdir -p /app/backend/data
chmod 755 /app/backend/data

# Set default environment variables
export PORT=${PORT:-8000}
export ALLOWED_ORIGINS=${ALLOWED_ORIGINS:-"http://localhost:3000,https://localhost:3000"}
export NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL:-""}
export NODE_ENV=${NODE_ENV:-"production"}
export DATABASE_PATH=${DATABASE_PATH:-"/app/backend/data/apiingest.db"}

echo "Starting APIIngest combined service..."
echo "Backend will run on port 8000"
echo "Frontend will run on port 3000"
echo "ALLOWED_ORIGINS: $ALLOWED_ORIGINS"
echo "NEXT_PUBLIC_API_URL: $NEXT_PUBLIC_API_URL"
echo "DATABASE_PATH: $DATABASE_PATH"

# Start supervisord
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf

