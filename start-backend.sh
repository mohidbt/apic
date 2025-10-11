#!/bin/bash

echo "🚀 Starting OpenAPI to Markdown Converter - Backend"
echo "=================================================="
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt
echo ""
echo "Starting FastAPI server on http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo ""
python3 main.py

