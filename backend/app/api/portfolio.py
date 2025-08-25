from flask import jsonify
from app.api import bp

@bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    """Get portfolio information"""
    portfolio_data = {
        'personal_info': {
            'name': 'Murtaza Lohar',
            'title': 'Full Stack Developer',
            'bio': 'Passionate developer with expertise in modern web technologies',
            'email': 'murtaza@example.com',
            'location': 'Your Location',
            'github': 'https://github.com/yourusername',
            'linkedin': 'https://linkedin.com/in/yourusername'
        },
        'skills': [
            {'name': 'Python', 'level': 90, 'category': 'Backend'},
            {'name': 'JavaScript', 'level': 85, 'category': 'Frontend'},
            {'name': 'React', 'level': 80, 'category': 'Frontend'},
            {'name': 'Flask', 'level': 85, 'category': 'Backend'},
            {'name': 'SQL', 'level': 80, 'category': 'Database'},
            {'name': 'HTML/CSS', 'level': 90, 'category': 'Frontend'}
        ],
        'projects': [
            {
                'id': 1,
                'title': 'Portfolio Website',
                'description': 'Modern portfolio website built with Flask and JavaScript',
                'technologies': ['Flask', 'JavaScript', 'HTML', 'CSS'],
                'github_url': 'https://github.com/yourusername/portfolio',
                'live_url': 'https://yourportfolio.com',
                'image': '/static/images/project1.jpg'
            },
            {
                'id': 2,
                'title': 'E-commerce Platform',
                'description': 'Full-stack e-commerce application',
                'technologies': ['React', 'Node.js', 'MongoDB'],
                'github_url': 'https://github.com/yourusername/ecommerce',
                'live_url': 'https://yourecommerce.com',
                'image': '/static/images/project2.jpg'
            }
        ],
        'experience': [
            {
                'company': 'Tech Company',
                'position': 'Full Stack Developer',
                'duration': '2022 - Present',
                'description': 'Developed and maintained web applications'
            },
            {
                'company': 'Startup',
                'position': 'Frontend Developer',
                'duration': '2021 - 2022',
                'description': 'Built responsive user interfaces'
            }
        ]
    }
    
    return jsonify(portfolio_data)

@bp.route('/portfolio/skills', methods=['GET'])
def get_skills():
    """Get skills information"""
    skills = [
        {'name': 'Python', 'level': 90, 'category': 'Backend'},
        {'name': 'JavaScript', 'level': 85, 'category': 'Frontend'},
        {'name': 'React', 'level': 80, 'category': 'Frontend'},
        {'name': 'Flask', 'level': 85, 'category': 'Backend'},
        {'name': 'SQL', 'level': 80, 'category': 'Database'},
        {'name': 'HTML/CSS', 'level': 90, 'category': 'Frontend'}
    ]
    return jsonify(skills)

@bp.route('/portfolio/projects', methods=['GET'])
def get_projects():
    """Get projects information"""
    projects = [
        {
            'id': 1,
            'title': 'Portfolio Website',
            'description': 'Modern portfolio website built with Flask and JavaScript',
            'technologies': ['Flask', 'JavaScript', 'HTML', 'CSS'],
            'github_url': 'https://github.com/yourusername/portfolio',
            'live_url': 'https://yourportfolio.com',
            'image': '/static/images/project1.jpg'
        },
        {
            'id': 2,
            'title': 'E-commerce Platform',
            'description': 'Full-stack e-commerce application',
            'technologies': ['React', 'Node.js', 'MongoDB'],
            'github_url': 'https://github.com/yourusername/ecommerce',
            'live_url': 'https://yourecommerce.com',
            'image': '/static/images/project2.jpg'
        }
    ]
    return jsonify(projects)
