# Portfolio Backend API

This is the backend API server for the portfolio website, built with Flask and providing RESTful endpoints for the frontend to consume.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables (optional)**
   Create a `.env` file in the backend directory:
   ```env
   SECRET_KEY=your-super-secret-key-here
   DATABASE_URL=sqlite:///app.db
   FLASK_ENV=development
   ```

6. **Initialize the database**
   ```bash
   python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

7. **Run the server**
   ```bash
   python run.py
   ```

The API server will start on `http://localhost:5000`

## 📚 API Endpoints

### Portfolio Data
- `GET /api/portfolio` - Get complete portfolio information
- `GET /api/portfolio/skills` - Get skills list
- `GET /api/portfolio/projects` - Get projects list

### Blog Posts
- `GET /api/posts` - Get published blog posts
- `GET /api/posts/all` - Get all blog posts (admin)
- `POST /api/posts` - Create new blog post
- `GET /api/posts/<id>` - Get specific blog post
- `PUT /api/posts/<id>` - Update blog post
- `DELETE /api/posts/<id>` - Delete blog post
- `PUT /api/posts/<id>/publish` - Publish/unpublish post

### Contact Form
- `POST /api/contacts` - Submit contact form
- `GET /api/contacts` - Get all contact messages (admin)
- `GET /api/contacts/<id>` - Get specific contact message
- `PUT /api/contacts/<id>` - Update contact message
- `DELETE /api/contacts/<id>` - Delete contact message

### Users
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get specific user
- `POST /api/users` - Create new user
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

## 🏗️ Architecture

### App Factory Pattern
The Flask application uses the factory pattern for better testing and configuration management.

### Blueprint Organization
API endpoints are organized into logical blueprints:
- `portfolio.py` - Portfolio data endpoints
- `posts.py` - Blog post management
- `contacts.py` - Contact form handling
- `users.py` - User management

### Database Models
- **User**: User accounts and authentication
- **Post**: Blog posts with publishing status
- **Contact**: Contact form submissions

## 🔧 Development

### Adding New Endpoints
1. Create or modify files in `app/api/`
2. Use the `@bp.route()` decorator
3. Import and register in `app/api/__init__.py`

### Database Changes
1. Modify models in `app/models.py`
2. Create and run migrations:
   ```bash
   flask db migrate -m "Description of changes"
   flask db upgrade
   ```

### Testing
```bash
# Run with Flask test mode
export FLASK_ENV=testing
python -m pytest tests/
```

## 🚀 Deployment

### Environment Variables
Set these for production:
- `SECRET_KEY`: Strong secret key
- `DATABASE_URL`: Production database URL
- `FLASK_ENV`: Set to 'production'

### Database
- **Development**: SQLite (default)
- **Production**: PostgreSQL or MySQL recommended

### Hosting Platforms
- **Heroku**: Add `Procfile` and set environment variables
- **PythonAnywhere**: Upload code and configure WSGI
- **DigitalOcean**: Use App Platform or Droplets
- **AWS**: Deploy to EC2 or use Elastic Beanstalk

## 📁 File Structure

```
backend/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   └── api/                 # API endpoints
│       ├── __init__.py      # Blueprint registration
│       ├── portfolio.py     # Portfolio endpoints
│       ├── posts.py         # Blog post endpoints
│       ├── contacts.py      # Contact endpoints
│       └── users.py         # User endpoints
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── run.py                  # Server entry point
└── README.md               # This file
```

## 🔒 Security Considerations

- CORS is enabled for frontend communication
- Input validation on all endpoints
- SQL injection protection via SQLAlchemy
- Environment variable configuration
- Secret key management

## 🐛 Troubleshooting

### Common Issues

1. **Database errors**: Ensure database is initialized
2. **Import errors**: Check virtual environment activation
3. **Port conflicts**: Change port in `run.py` if needed
4. **CORS issues**: Verify frontend URL in CORS configuration

### Debug Mode
```bash
export FLASK_DEBUG=1
python run.py
```

## 📝 License

This backend is part of the portfolio project and follows the same MIT license.
