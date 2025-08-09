# My Portfolio Website

A modern, responsive portfolio website built with Python Flask, showcasing my skills, projects, and experience.

## Features

- **Responsive Design**: Mobile-first approach with modern CSS
- **Project Showcase**: Display your projects with descriptions and links
- **Skills Section**: Highlight your technical skills and expertise
- **Contact Form**: Easy way for visitors to get in touch
- **Blog Section**: Share your thoughts and experiences
- **Dark/Light Mode**: Toggle between themes

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5 + Custom CSS
- **Database**: SQLite (for blog posts and contact form)
- **Deployment**: Ready for Heroku, Vercel, or any Python hosting

## Project Structure

```
My Portfolio/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
├── templates/
├── instance/
├── requirements.txt
├── config.py
├── run.py
├── .gitignore
└── README.md
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/loharmurtaza/my_portfolio.git
   cd my_ortfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file (optional)
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000`

## Customization

### Personal Information
Edit `app/routes.py` to update:
- Your name, title, and bio
- Contact information
- Social media links

### Projects
Add your projects in `app/routes.py` in the projects list.

### Skills
Update the skills section with your expertise areas.

### Styling
Modify `app/static/css/style.css` to match your preferred color scheme and design.

## Deployment

### Heroku
1. Create a `Procfile`:
   ```
   web: gunicorn run:app
   ```

2. Deploy using Heroku CLI or GitHub integration.

### Vercel
1. Install Vercel CLI
2. Run `vercel` in the project directory

### Other Platforms
The app is compatible with any Python hosting platform.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue on GitHub or contact me directly.
