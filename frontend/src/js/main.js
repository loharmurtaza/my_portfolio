// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// API Service
class APIService {
    static async get(endpoint) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    static async post(endpoint, data) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }
}

// Portfolio Data Manager
class PortfolioManager {
    constructor() {
        this.portfolioData = null;
        this.init();
    }

    async init() {
        try {
            this.showLoading(true);
            await this.loadPortfolioData();
            this.renderPortfolio();
            this.setupEventListeners();
            this.showLoading(false);
        } catch (error) {
            console.error('Failed to initialize portfolio:', error);
            this.showError('Failed to load portfolio data');
            this.showLoading(false);
        }
    }

    async loadPortfolioData() {
        try {
            this.portfolioData = await APIService.get('/portfolio');
        } catch (error) {
            // Fallback data if API fails
            this.portfolioData = this.getFallbackData();
        }
    }

    getFallbackData() {
        return {
            personal_info: {
                name: 'Murtaza Lohar',
                title: 'Full Stack Developer',
                bio: 'Passionate developer with expertise in modern web technologies. I love creating innovative solutions and learning new technologies.',
                email: 'murtaza@example.com',
                github: 'https://github.com/yourusername',
                linkedin: 'https://linkedin.com/in/yourusername'
            },
            skills: [
                {name: 'Python', level: 90, category: 'Backend'},
                {name: 'JavaScript', level: 85, category: 'Frontend'},
                {name: 'React', level: 80, category: 'Frontend'},
                {name: 'Flask', level: 85, category: 'Backend'},
                {name: 'SQL', level: 80, category: 'Database'},
                {name: 'HTML/CSS', level: 90, category: 'Frontend'}
            ],
            projects: [
                {
                    id: 1,
                    title: 'Portfolio Website',
                    description: 'Modern portfolio website built with Flask and JavaScript',
                    technologies: ['Flask', 'JavaScript', 'HTML', 'CSS'],
                    github_url: 'https://github.com/yourusername/portfolio',
                    live_url: 'https://yourportfolio.com',
                    image: '/static/images/project1.jpg'
                },
                {
                    id: 2,
                    title: 'E-commerce Platform',
                    description: 'Full-stack e-commerce application',
                    technologies: ['React', 'Node.js', 'MongoDB'],
                    github_url: 'https://github.com/yourusername/ecommerce',
                    live_url: 'https://yourecommerce.com',
                    image: '/static/images/project2.jpg'
                }
            ]
        };
    }

    renderPortfolio() {
        this.renderAbout();
        this.renderSkills();
        this.renderProjects();
        this.renderContact();
    }

    renderAbout() {
        const personalInfo = this.portfolioData.personal_info;
        
        // Update bio
        const aboutBio = document.getElementById('about-bio');
        if (aboutBio) {
            aboutBio.textContent = personalInfo.bio;
        }

        // Update stats
        const experienceYears = document.getElementById('experience-years');
        const projectsCount = document.getElementById('projects-count');
        const skillsCount = document.getElementById('skills-count');

        if (experienceYears) experienceYears.textContent = '2+';
        if (projectsCount) projectsCount.textContent = this.portfolioData.projects.length;
        if (skillsCount) skillsCount.textContent = this.portfolioData.skills.length;
    }

    renderSkills() {
        const skillsContainer = document.getElementById('skills-container');
        if (!skillsContainer) return;

        const skillsHTML = this.portfolioData.skills.map(skill => `
            <div class="skill-card" data-category="${skill.category}">
                <div class="skill-header">
                    <h3>${skill.name}</h3>
                    <span class="skill-category">${skill.category}</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-progress" style="width: ${skill.level}%"></div>
                </div>
                <div class="skill-level">${skill.level}%</div>
            </div>
        `).join('');

        skillsContainer.innerHTML = skillsHTML;
    }

    renderProjects() {
        const projectsContainer = document.getElementById('projects-container');
        if (!projectsContainer) return;

        const projectsHTML = this.portfolioData.projects.map(project => `
            <div class="project-card">
                <div class="project-image">
                    <div class="project-placeholder">
                        <i class="fas fa-code"></i>
                    </div>
                </div>
                <div class="project-content">
                    <h3>${project.title}</h3>
                    <p>${project.description}</p>
                    <div class="project-technologies">
                        ${project.technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('')}
                    </div>
                    <div class="project-links">
                        <a href="${project.github_url}" target="_blank" class="btn btn-small">
                            <i class="fab fa-github"></i> Code
                        </a>
                        <a href="${project.live_url}" target="_blank" class="btn btn-small btn-primary">
                            <i class="fas fa-external-link-alt"></i> Live
                        </a>
                    </div>
                </div>
            </div>
        `).join('');

        projectsContainer.innerHTML = projectsHTML;
    }

    renderContact() {
        const personalInfo = this.portfolioData.personal_info;
        
        const contactEmail = document.getElementById('contact-email');
        const contactGithub = document.getElementById('contact-github');
        const contactLinkedin = document.getElementById('contact-linkedin');

        if (contactEmail) contactEmail.textContent = personalInfo.email;
        if (contactGithub) contactGithub.textContent = personalInfo.github.split('/').pop();
        if (contactLinkedin) contactLinkedin.textContent = personalInfo.linkedin.split('/').pop();
    }

    setupEventListeners() {
        // Contact form submission
        const contactForm = document.getElementById('contact-form');
        if (contactForm) {
            contactForm.addEventListener('submit', this.handleContactSubmit.bind(this));
        }

        // Mobile navigation toggle
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');
        if (navToggle && navMenu) {
            navToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
                navToggle.classList.toggle('active');
            });
        }

        // Smooth scrolling for navigation links
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href').substring(1);
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Theme toggle
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', this.toggleTheme.bind(this));
        }

        // Intersection Observer for animations
        this.setupIntersectionObserver();
    }

    async handleContactSubmit(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const contactData = {
            name: formData.get('name'),
            email: formData.get('email'),
            subject: formData.get('subject'),
            message: formData.get('message')
        };

        try {
            this.showLoading(true);
            await APIService.post('/contacts', contactData);
            this.showSuccess('Message sent successfully!');
            e.target.reset();
        } catch (error) {
            this.showError('Failed to send message. Please try again.');
        } finally {
            this.showLoading(false);
        }
    }

    toggleTheme() {
        document.body.classList.toggle('dark-theme');
        const themeToggle = document.getElementById('theme-toggle');
        const icon = themeToggle.querySelector('i');
        
        if (document.body.classList.contains('dark-theme')) {
            icon.className = 'fas fa-sun';
            localStorage.setItem('theme', 'dark');
        } else {
            icon.className = 'fas fa-moon';
            localStorage.setItem('theme', 'light');
        }
    }

    setupIntersectionObserver() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);

        // Observe all sections
        const sections = document.querySelectorAll('section');
        sections.forEach(section => observer.observe(section));
    }

    showLoading(show) {
        const spinner = document.getElementById('loading-spinner');
        if (spinner) {
            spinner.style.display = show ? 'flex' : 'none';
        }
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);
        
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
}

// Initialize the portfolio when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PortfolioManager();
    
    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            const icon = themeToggle.querySelector('i');
            icon.className = 'fas fa-sun';
        }
    }
});
