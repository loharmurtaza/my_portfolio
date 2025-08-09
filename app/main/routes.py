from flask import render_template, request, flash, redirect, url_for, current_app
from app.main import bp
from app.models import Post, Contact, Project, SkillCategory, Publication, SiteSettings
from app import db
from app.forms import ContactForm
import re

@bp.route('/')
@bp.route('/index')
def index():
    settings = SiteSettings.query.first()
    hero = {
        'name': (settings.hero_name if settings and settings.hero_name else 'Murtaza'),
        'title': (settings.hero_title if settings and settings.hero_title else 'Full Stack Developer & IoT Engineer')
    }
    featured_projects = Project.query.order_by(Project.created_at.desc()).limit(3).all()
    return render_template('main/index.html', hero=hero, featured_projects=featured_projects)

@bp.route('/about')
def about():
    settings = SiteSettings.query.first()
    return render_template('main/about.html', settings=settings)

@bp.route('/projects')
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('main/projects.html', projects=projects)

@bp.route('/publications')
def publications():
    pubs = Publication.query.order_by(Publication.year.desc().nullslast()).all()
    return render_template('main/publications.html', publications=pubs)

@bp.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True).order_by(Post.created_at.desc()).paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    return render_template('main/blog.html', posts=posts)

@bp.route('/blog/<slug>')
def post(slug):
    post = Post.query.filter_by(slug=slug, published=True).first_or_404()
    return render_template('main/post.html', post=post)

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        flash('Your message has been sent successfully! I will get back to you soon.', 'success')
        return redirect(url_for('main.contact'))
    return render_template('main/contact.html', form=form)

@bp.route('/skills')
def skills():
    categories = SkillCategory.query.order_by(SkillCategory.name.asc()).all()
    return render_template('main/skills.html', categories=categories)
