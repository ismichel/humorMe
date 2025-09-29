#!/bin/bash

# HumorMe Startup Script
echo "🎭 Starting HumorMe - AI Audio Humor Detection Demo"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✅ Dependencies installed successfully"
    else
        echo "❌ Failed to install dependencies"
        exit 1
    fi
else
    echo "⚠️  requirements.txt not found. Please ensure all dependencies are installed."
fi

# Start the Flask application
echo "🚀 Starting Flask application..."
echo "📱 Open your browser and navigate to: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

python3 app.py
