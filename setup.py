#!/usr/bin/env python3
"""
Setup script for the Portfolio website.
This script helps users get started with the application.
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version {sys.version.split()[0]} is compatible!")
    return True

def create_virtual_environment():
    """Create a virtual environment."""
    if os.path.exists('venv'):
        print("ℹ️  Virtual environment already exists!")
        return True
    
    return run_command('python -m venv venv', 'Creating virtual environment')

def install_dependencies():
    """Install required dependencies."""
    if os.name == 'nt':  # Windows
        pip_cmd = 'venv\\Scripts\\pip'
    else:  # Unix/Linux/macOS
        pip_cmd = 'venv/bin/pip'
    
    return run_command(f'{pip_cmd} install -r requirements.txt', 'Installing dependencies')

def initialize_database():
    """Initialize the database."""
    if os.name == 'nt':  # Windows
        python_cmd = 'venv\\Scripts\\python'
    else:  # Unix/Linux/macOS
        python_cmd = 'venv/bin/python'
    
    return run_command(f'{python_cmd} init_db.py', 'Initializing database')

def main():
    """Main setup function."""
    print("🚀 Welcome to the Portfolio Website Setup!")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Initialize database
    if not initialize_database():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n" + "=" * 50)
    print("📋 Next Steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    
    print("2. Start the development server:")
    print("   python run.py")
    
    print("3. Open your browser and visit:")
    print("   http://localhost:5000")
    
    print("\n🔐 Admin Access:")
    print("   Username: admin")
    print("   Password: admin123")
    print("   URL: http://localhost:5000/auth/login")
    
    print("\n📚 Documentation:")
    print("   Read the README.md file for more information")
    
    print("\n🌟 Happy coding!")

if __name__ == '__main__':
    main()
