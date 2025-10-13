#!/bin/bash
set -e

# Create log directory
mkdir -p /var/log/supervisor

# Set default environment variables
export PORT=${PORT:-8000}
export ALLOWED_ORIGINS=${ALLOWED_ORIGINS:-"http://localhost:3000,https://localhost:3000"}
export NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL:-""}
export NODE_ENV=${NODE_ENV:-"production"}

echo "Starting APIIngest combined service..."
echo "Backend will run on port 8000"
echo "Frontend will run on port 3000"
echo "ALLOWED_ORIGINS: $ALLOWED_ORIGINS"
echo "NEXT_PUBLIC_API_URL: $NEXT_PUBLIC_API_URL"

# Start supervisord
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf

