#!/bin/bash
# Quick start script for frontend development

set -e

echo "🚀 Starting API Ingest Frontend..."
echo ""

cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
else
    echo "✅ Dependencies already installed"
fi

# Create .env.local if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "🔧 Creating .env.local..."
    cat > .env.local << EOF
NEXT_PUBLIC_API_URL=http://localhost:8000
EOF
fi

echo ""
echo "✅ Frontend ready!"
echo "🌐 Opening: http://localhost:3000"
echo ""

# Start the dev server
npm run dev

