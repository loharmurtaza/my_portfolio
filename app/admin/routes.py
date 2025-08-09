from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.admin import bp
from app.models import Post, Contact, User, SiteSettings, Project, SkillCategory, Skill, Publication
from app.forms import PostForm, EmptyForm, SiteSettingsForm, ProjectForm, SkillCategoryForm, SkillForm, PublicationForm
from app import db
import re
import functools

def admin_required(f):
    """Decorator to check if user is admin"""
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    """Admin dashboard"""
    posts_count = Post.query.count()
    contacts_count = Contact.query.count()
    unread_contacts = Contact.query.filter_by(is_read=False).count()
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    recent_contacts = Contact.query.order_by(Contact.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         posts_count=posts_count,
                         contacts_count=contacts_count,
                         unread_contacts=unread_contacts,
                         recent_posts=recent_posts,
                         recent_contacts=recent_contacts)

# Settings
@bp.route('/settings', methods=['GET', 'POST'])
@login_required
@admin_required
def settings():
    settings = SiteSettings.query.first()
    form = SiteSettingsForm(obj=settings)
    if form.validate_on_submit():
        if settings is None:
            settings = SiteSettings()
            db.session.add(settings)
        form.populate_obj(settings)
        db.session.commit()
        flash('Settings saved.', 'success')
        return redirect(url_for('admin.settings'))
    return render_template('admin/settings.html', form=form)

# Posts
@bp.route('/posts')
@login_required
@admin_required
def posts():
    """List all posts"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    delete_form = EmptyForm()
    return render_template('admin/posts.html', posts=posts, delete_form=delete_form)

@bp.route('/posts/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_post():
    """Create new post"""
    form = PostForm()
    if form.validate_on_submit():
        # Generate slug from title
        slug = re.sub(r'[^\w\s-]', '', form.title.data.lower())
        slug = re.sub(r'[-\s]+', '-', slug).strip('-')
        
        post = Post(
            title=form.title.data,
            content=form.content.data,
            excerpt=form.excerpt.data,
            slug=slug,
            published=form.published.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('admin.posts'))
    return render_template('admin/post_form.html', form=form, title='New Post')

@bp.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_post(id):
    """Edit existing post"""
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.excerpt = form.excerpt.data
        post.published = form.published.data
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('admin.posts'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.excerpt.data = post.excerpt
        form.published.data = post.published
    return render_template('admin/post_form.html', form=form, title='Edit Post')

@bp.route('/posts/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_post(id):
    """Delete post"""
    form = EmptyForm()
    if form.validate_on_submit():
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully!', 'success')
    return redirect(url_for('admin.posts'))

# Projects
@bp.route('/projects')
@login_required
@admin_required
def projects():
    items = Project.query.order_by(Project.created_at.desc()).all()
    delete_form = EmptyForm()
    return render_template('admin/projects.html', projects=items, delete_form=delete_form)

@bp.route('/projects/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            technologies=form.technologies.data,
            github_url=form.github_url.data,
            live_url=form.live_url.data,
            image=form.image.data,
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created.', 'success')
        return redirect(url_for('admin.projects'))
    return render_template('admin/project_form.html', form=form, title='New Project')

@bp.route('/projects/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_project(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        form.populate_obj(project)
        db.session.commit()
        flash('Project updated.', 'success')
        return redirect(url_for('admin.projects'))
    return render_template('admin/project_form.html', form=form, title='Edit Project')

@bp.route('/projects/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_project(id):
    form = EmptyForm()
    if form.validate_on_submit():
        project = Project.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted.', 'success')
    return redirect(url_for('admin.projects'))

# Skills
@bp.route('/skills')
@login_required
@admin_required
def skills():
    categories = SkillCategory.query.order_by(SkillCategory.name.asc()).all()
    return render_template('admin/skills.html', categories=categories)

@bp.route('/skills/categories/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_skill_category():
    form = SkillCategoryForm()
    if form.validate_on_submit():
        db.session.add(SkillCategory(name=form.name.data))
        db.session.commit()
        flash('Category created.', 'success')
        return redirect(url_for('admin.skills'))
    return render_template('admin/skill_category_form.html', form=form, title='New Category')

@bp.route('/skills/categories/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_skill_category(id):
    category = SkillCategory.query.get_or_404(id)
    form = SkillCategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('Category updated.', 'success')
        return redirect(url_for('admin.skills'))
    return render_template('admin/skill_category_form.html', form=form, title='Edit Category')

@bp.route('/skills/categories/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_skill_category(id):
    form = EmptyForm()
    if form.validate_on_submit():
        category = SkillCategory.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted.', 'success')
    return redirect(url_for('admin.skills'))

@bp.route('/skills/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_skill():
    form = SkillForm()
    form.set_category_choices()
    if form.validate_on_submit():
        db.session.add(Skill(name=form.name.data, category_id=form.category_id.data))
        db.session.commit()
        flash('Skill created.', 'success')
        return redirect(url_for('admin.skills'))
    return render_template('admin/skill_form.html', form=form, title='New Skill')

@bp.route('/skills/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_skill(id):
    skill = Skill.query.get_or_404(id)
    form = SkillForm(obj=skill)
    form.set_category_choices()
    if form.validate_on_submit():
        skill.name = form.name.data
        skill.category_id = form.category_id.data
        db.session.commit()
        flash('Skill updated.', 'success')
        return redirect(url_for('admin.skills'))
    return render_template('admin/skill_form.html', form=form, title='Edit Skill')

@bp.route('/skills/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_skill(id):
    form = EmptyForm()
    if form.validate_on_submit():
        skill = Skill.query.get_or_404(id)
        db.session.delete(skill)
        db.session.commit()
        flash('Skill deleted.', 'success')
    return redirect(url_for('admin.skills'))

# Publications
@bp.route('/publications')
@login_required
@admin_required
def publications():
    pubs = Publication.query.order_by(Publication.year.desc().nullslast()).all()
    delete_form = EmptyForm()
    return render_template('admin/publications.html', publications=pubs, delete_form=delete_form)

@bp.route('/publications/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_publication():
    form = PublicationForm()
    if form.validate_on_submit():
        pub = Publication(
            title=form.title.data,
            authors=form.authors.data,
            venue=form.venue.data,
            year=form.year.data,
            status=form.status.data,
            link=form.link.data,
        )
        db.session.add(pub)
        db.session.commit()
        flash('Publication created.', 'success')
        return redirect(url_for('admin.publications'))
    return render_template('admin/publication_form.html', form=form, title='New Publication')

@bp.route('/publications/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_publication(id):
    pub = Publication.query.get_or_404(id)
    form = PublicationForm(obj=pub)
    if form.validate_on_submit():
        form.populate_obj(pub)
        db.session.commit()
        flash('Publication updated.', 'success')
        return redirect(url_for('admin.publications'))
    return render_template('admin/publication_form.html', form=form, title='Edit Publication')

@bp.route('/publications/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_publication(id):
    form = EmptyForm()
    if form.validate_on_submit():
        pub = Publication.query.get_or_404(id)
        db.session.delete(pub)
        db.session.commit()
        flash('Publication deleted.', 'success')
    return redirect(url_for('admin.publications'))

# Contacts
@bp.route('/contacts')
@login_required
@admin_required
def contacts():
    """List all contact messages"""
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    delete_form = EmptyForm()
    return render_template('admin/contacts.html', contacts=contacts, delete_form=delete_form)

@bp.route('/contacts/<int:id>')
@login_required
@admin_required
def view_contact(id):
    """View contact message"""
    contact = Contact.query.get_or_404(id)
    if not contact.is_read:
        contact.is_read = True
        db.session.commit()
    return render_template('admin/contact_detail.html', contact=contact)

@bp.route('/contacts/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_contact(id):
    """Delete contact message"""
    form = EmptyForm()
    if form.validate_on_submit():
        contact = Contact.query.get_or_404(id)
        db.session.delete(contact)
        db.session.commit()
        flash('Contact message deleted successfully!', 'success')
    return redirect(url_for('admin.contacts'))
