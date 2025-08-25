from app import create_app, db
from app.models import User, Post, Contact

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Contact': Contact
    }

if __name__ == '__main__':
    print("🚀 Starting Portfolio Backend API Server...")
    print("📍 API Base URL: http://localhost:5000/api")
    print("📚 Available endpoints:")
    print("   - GET  /api/portfolio - Portfolio information")
    print("   - GET  /api/portfolio/skills - Skills list")
    print("   - GET  /api/portfolio/projects - Projects list")
    print("   - GET  /api/posts - Published blog posts")
    print("   - POST /api/contacts - Submit contact form")
    print("   - GET  /api/users - Users list (admin)")
    print("🔧 Server running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
