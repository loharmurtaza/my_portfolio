# My Portfolio Website - Independent Frontend & Backend

A modern, responsive portfolio website with **completely independent frontend and backend projects**. The backend provides a RESTful API built with Flask, while the frontend is a standalone JavaScript application that consumes the API.

## 🏗️ Architecture Overview

This project is divided into two **completely independent** applications:

- **Backend** (`/backend`): Flask API server with its own virtual environment
- **Frontend** (`/frontend`): Modern JavaScript application with its own Node.js setup

Both projects can be developed, deployed, and maintained independently while working together through the API.

## 🚀 Quick Start

### Prerequisites
- **Backend**: Python 3.8+
- **Frontend**: Node.js 16+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/my-portfolio.git
cd my-portfolio
```

### 2. Start Backend (Terminal 1)
```bash
cd backend

# Windows:
start-backend.bat

# Unix/Linux:
./start-backend.sh
```

The backend will start on `http://localhost:5000`

### 3. Start Frontend (Terminal 2)
```bash
cd frontend

# Windows:
start-frontend.bat

# Unix/Linux:
./start-frontend.sh
```

The frontend will start on `http://localhost:3000`

### 4. View Your Portfolio
Open `http://localhost:3000` in your browser!

## 📁 Project Structure

```
My Portfolio/
├── backend/                 # Independent Flask API Project
│   ├── app/                # Flask application code
│   │   ├── api/            # API endpoints
│   │   ├── models.py       # Database models
│   │   └── __init__.py     # Flask app factory
│   ├── venv/               # Python virtual environment
│   ├── config.py           # Backend configuration
│   ├── requirements.txt    # Python dependencies
│   ├── run.py             # Backend server entry point
│   ├── start-backend.bat  # Windows startup script
│   ├── start-backend.sh   # Unix/Linux startup script
│   └── README.md          # Backend documentation
│
├── frontend/               # Independent JavaScript Project
│   ├── src/                # Source files
│   │   ├── index.html     # Main HTML file
│   │   ├── js/            # JavaScript files
│   │   └── styles/        # CSS files
│   ├── node_modules/      # Node.js dependencies
│   ├── package.json       # Node.js dependencies
│   ├── vite.config.js     # Vite configuration
│   ├── start-frontend.bat # Windows startup script
│   ├── start-frontend.sh  # Unix/Linux startup script
│   └── README.md          # Frontend documentation
│
├── README.md              # Main project documentation
├── STARTUP.md             # Quick startup guide
└── .gitignore            # Git ignore file
```

## 🎯 Key Features

- **Responsive Design**: Mobile-first approach with modern CSS
- **API-First Backend**: RESTful Flask API with proper separation of concerns
- **Modern Frontend**: Vanilla JavaScript with ES6+ features
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **Contact Form**: Functional contact form with backend storage
- **Blog System**: Blog posts management via API
- **Dark/Light Theme**: Toggle between themes with local storage
- **Smooth Animations**: CSS animations and intersection observer effects

## 🛠️ Tech Stack

### Backend
- **Python Flask**: Web framework for API
- **SQLAlchemy**: Database ORM
- **Flask-Migrate**: Database migrations
- **Flask-CORS**: Cross-origin resource sharing
- **SQLite**: Database (easily changeable to PostgreSQL/MySQL)

### Frontend
- **Vanilla JavaScript**: Modern ES6+ features
- **CSS3**: Custom CSS with CSS variables and animations
- **HTML5**: Semantic HTML structure
- **Vite**: Build tool and development server
- **Responsive Design**: Mobile-first CSS Grid and Flexbox

## 📚 API Endpoints

### Portfolio Data
- `GET /api/portfolio` - Get complete portfolio information
- `GET /api/portfolio/skills` - Get skills list
- `GET /api/portfolio/projects` - Get projects list

### Blog Posts
- `GET /api/posts` - Get published blog posts
- `POST /api/posts` - Create new blog post
- `PUT /api/posts/<id>` - Update blog post
- `DELETE /api/posts/<id>` - Delete blog post

### Contact Form
- `POST /api/contacts` - Submit contact form
- `GET /api/contacts` - Get all contact messages (admin)

### Users
- `GET /api/users` - Get all users
- `POST /api/users` - Create new user

## 🔧 Development

### Independent Development
- **Backend**: Can be developed and tested independently
- **Frontend**: Can be developed with mock data or connected to any API
- **API Testing**: Use tools like Postman or curl to test endpoints
- **Frontend Testing**: Works offline with fallback data

### Adding Features
1. **Backend**: Add new endpoints in `backend/app/api/`
2. **Frontend**: Add new components in `frontend/src/`
3. **Database**: Modify models in `backend/app/models.py`
4. **Styling**: Update CSS in `frontend/src/styles/`

## 🚀 Deployment

### Backend Deployment
- Deploy to Heroku, PythonAnywhere, or any Python hosting
- Set environment variables for production
- Use production database (PostgreSQL recommended)

### Frontend Deployment
- Build with `npm run build` in frontend directory
- Deploy `dist/` folder to Vercel, Netlify, or any static hosting
- Update API base URL for production

## 🎨 Customization

### Personal Information
1. **Backend**: Edit `backend/app/api/portfolio.py`
2. **Frontend**: Update `frontend/src/js/main.js`

### Styling
- Modify `frontend/src/styles/main.css`
- Update CSS variables for theme colors
- Customize responsive breakpoints

### Content
- Update HTML structure in `frontend/src/index.html`
- Add new sections or modify existing ones

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes in the appropriate project
4. Test both frontend and backend
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- Modern CSS techniques and responsive design principles
- JavaScript ES6+ features and modern web APIs

---

**Note**: This architecture provides complete separation of concerns. The backend serves as a pure API, while the frontend is a standalone application. This approach enables independent development, testing, and deployment of both components while maintaining a clean, professional portfolio website.
