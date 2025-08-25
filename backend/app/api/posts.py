from flask import request, jsonify
from app.api import bp
from app.models import Post, User
from app import db

@bp.route('/posts', methods=['GET'])
def get_posts():
    """Get all published blog posts"""
    posts = Post.query.filter_by(published=True).order_by(Post.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/posts/all', methods=['GET'])
def get_all_posts():
    """Get all blog posts (admin only)"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/posts', methods=['POST'])
def create_post():
    """Create a new blog post"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['title', 'content', 'author_id']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    post = Post(
        title=data['title'],
        content=data['content'],
        author_id=data['author_id'],
        published=data.get('published', False)
    )
    
    try:
        db.session.add(post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully', 'id': post.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create post'}), 500

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    """Get a specific blog post"""
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict())

@bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    """Update a blog post"""
    post = Post.query.get_or_404(id)
    data = request.get_json()
    
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    if 'published' in data:
        post.published = data['published']
    
    try:
        db.session.commit()
        return jsonify(post.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update post'}), 500

@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    """Delete a blog post"""
    post = Post.query.get_or_404(id)
    
    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete post'}), 500

@bp.route('/posts/<int:id>/publish', methods=['PUT'])
def publish_post(id):
    """Publish/unpublish a blog post"""
    post = Post.query.get_or_404(id)
    data = request.get_json()
    
    if 'published' in data:
        post.published = data['published']
    
    try:
        db.session.commit()
        return jsonify(post.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update post'}), 500
