#!/bin/bash

echo "Starting Portfolio Frontend Development Server..."
echo

cd frontend

echo "Installing dependencies..."
npm install

echo
echo "Starting Vite Development Server..."
echo "Frontend will run on: http://localhost:3000"
echo
echo "Press Ctrl+C to stop the server"
echo

npm run dev
