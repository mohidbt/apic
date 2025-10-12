# Multi-stage build for combined backend + frontend deployment
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend

# Copy frontend package files
COPY frontend/package*.json ./

# Install frontend dependencies with legacy peer deps
RUN npm ci --legacy-peer-deps

# Copy frontend source
COPY frontend ./

# Build frontend
RUN npm run build

# Final stage - Python base with Node
FROM python:3.11-slim

WORKDIR /app

# Install Node.js and system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    supervisor \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend code
COPY backend ./backend

# Copy built frontend from builder stage
COPY --from=frontend-builder /app/frontend/.next ./frontend/.next
COPY --from=frontend-builder /app/frontend/public ./frontend/public
COPY --from=frontend-builder /app/frontend/node_modules ./frontend/node_modules
COPY --from=frontend-builder /app/frontend/package*.json ./frontend/

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Create startup script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Expose ports (Koyeb will use PORT env var, defaulting to 8000)
EXPOSE 8000 3000

# Health check on backend
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start supervisor to manage both processes
CMD ["/app/start.sh"]

