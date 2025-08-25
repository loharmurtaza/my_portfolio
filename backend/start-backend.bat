@echo off
echo Starting Portfolio Backend Server...
echo.

cd backend

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask API Server...
echo Server will run on: http://localhost:5000
echo API Base URL: http://localhost:5000/api
echo.
echo Press Ctrl+C to stop the server
echo.

python run.py

pause
