#!/bin/bash
# Quick start script for backend development

set -e

echo "🚀 Starting APIIngest Backend..."
echo ""

cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Set environment variables for development
export ALLOWED_ORIGINS="http://localhost:3000,http://localhost:3001"
export PORT=8000

echo ""
echo "✅ Backend ready!"
echo "📝 API docs: http://localhost:8000/docs"
echo "🏥 Health check: http://localhost:8000/health"
echo ""

# Start the server
python main.py

