#!/usr/bin/env python3
"""
Database initialization script for the Portfolio website.
This script creates the database tables and sets up an admin user.
"""

from app import create_app, db
from app.models import User, Post, Contact

def init_database():
    """Initialize the database and create tables."""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Check if admin user already exists
        admin_user = User.query.filter_by(username='admin').first()
        
        if not admin_user:
            # Create admin user
            admin_user = User(
                username='admin',
                email='admin@example.com',
                is_admin=True
            )
            admin_user.set_password('admin123')
            
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Admin user created successfully!")
            print("   Username: admin")
            print("   Password: admin123")
            print("   Email: admin@example.com")
        else:
            print("ℹ️  Admin user already exists!")
        
        # Create some sample blog posts
        sample_posts = [
            {
                'title': 'Welcome to My Portfolio',
                'content': '''
# Welcome to My Portfolio

This is my first blog post on my new portfolio website. I'm excited to share my journey in software development and the projects I've worked on.

## What I'll be sharing

- Technical insights and tutorials
- Project updates and case studies
- Industry trends and best practices
- Personal experiences and lessons learned

Stay tuned for more content!
                ''',
                'excerpt': 'Welcome to my portfolio website where I share my journey in software development.',
                'slug': 'welcome-to-my-portfolio',
                'published': True
            },
            {
                'title': 'Building a Portfolio with Flask',
                'content': '''
# Building a Portfolio with Flask

In this post, I'll share my experience building this portfolio website using Python Flask.

## Why Flask?

Flask is a lightweight and flexible web framework that's perfect for building portfolio websites. Here are some reasons why I chose it:

- **Simple and Clean**: Flask follows the principle of simplicity
- **Flexible**: You can structure your application however you want
- **Python**: Leverages Python's rich ecosystem
- **Easy to Deploy**: Works well with various hosting platforms

## Key Features

- Responsive design with Bootstrap 5
- Blog functionality with markdown support
- Contact form with email integration
- Admin panel for content management
- SEO optimized

The code is open source and available on GitHub!
                ''',
                'excerpt': 'Learn about my experience building this portfolio website using Python Flask.',
                'slug': 'building-portfolio-with-flask',
                'published': True
            }
        ]
        
        # Add sample posts if they don't exist
        for post_data in sample_posts:
            existing_post = Post.query.filter_by(slug=post_data['slug']).first()
            if not existing_post:
                post = Post(
                    title=post_data['title'],
                    content=post_data['content'],
                    excerpt=post_data['excerpt'],
                    slug=post_data['slug'],
                    published=post_data['published'],
                    author=admin_user
                )
                db.session.add(post)
                print(f"✅ Created sample post: {post_data['title']}")
        
        db.session.commit()
        print("\n🎉 Database initialization completed successfully!")
        print("\nNext steps:")
        print("1. Run 'python run.py' to start the development server")
        print("2. Visit http://localhost:5000 to see your portfolio")
        print("3. Login to admin panel at http://localhost:5000/auth/login")
        print("   Username: admin")
        print("   Password: admin123")

if __name__ == '__main__':
    init_database()
