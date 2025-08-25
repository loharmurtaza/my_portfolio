# Portfolio Project Startup Guide

This project consists of two independent applications that work together:

## 🏗️ Project Structure

```
My Portfolio/
├── backend/          # Flask API Server (Port 5000)
├── frontend/         # JavaScript Frontend (Port 3000)
├── README.md         # Main project documentation
├── STARTUP.md        # This startup guide
└── .gitignore        # Git ignore file
```

## 🚀 Quick Start

### Option 1: Run Both Projects (Recommended for Development)

**Terminal 1 - Backend:**
```bash
cd backend
# Windows:
start-backend.bat
# Unix/Linux:
./start-backend.sh
```

**Terminal 2 - Frontend:**
```bash
cd frontend
# Windows:
start-frontend.bat
# Unix/Linux:
./start-frontend.sh
```

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Unix/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python run.py
```

#### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 🌐 Access URLs

- **Backend API**: http://localhost:5000
- **Frontend App**: http://localhost:3000
- **API Endpoints**: http://localhost:5000/api

## 🔧 Development Workflow

1. **Start Backend First** - The Flask API server must be running for the frontend to work
2. **Start Frontend** - The JavaScript app will connect to the backend API
3. **Make Changes** - Both servers support hot reload for development
4. **Test API** - Use tools like Postman or curl to test backend endpoints

## 📁 Independent Projects

Each project is completely independent with its own:
- **Virtual Environment** (backend/venv)
- **Dependencies** (backend/requirements.txt, frontend/package.json)
- **Configuration** (backend/config.py, frontend/vite.config.js)
- **Documentation** (backend/README.md, frontend/README.md)

## 🚨 Troubleshooting

### Backend Issues
- Ensure Python 3.8+ is installed
- Check virtual environment is activated
- Verify port 5000 is not in use

### Frontend Issues
- Ensure Node.js 16+ is installed
- Check npm dependencies are installed
- Verify port 3000 is not in use

### Connection Issues
- Ensure both servers are running
- Check browser console for CORS errors
- Verify API base URL in frontend code

## 📚 More Information

- **Backend Details**: See `backend/README.md`
- **Frontend Details**: See `frontend/README.md`
- **Main Project**: See `README.md`
