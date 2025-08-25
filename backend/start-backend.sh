#!/bin/bash

echo "Starting Portfolio Backend Server..."
echo

cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Starting Flask API Server..."
echo "Server will run on: http://localhost:5000"
echo "API Base URL: http://localhost:5000/api"
echo
echo "Press Ctrl+C to stop the server"
echo

python run.py
