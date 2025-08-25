from flask import request, jsonify
from app.api import bp
from app.models import Contact
from app import db

@bp.route('/contacts', methods=['GET'])
def get_contacts():
    """Get all contact messages (admin only)"""
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return jsonify([contact.to_dict() for contact in contacts])

@bp.route('/contacts', methods=['POST'])
def create_contact():
    """Create a new contact message"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['name', 'email', 'subject', 'message']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    contact = Contact(
        name=data['name'],
        email=data['email'],
        subject=data['subject'],
        message=data['message']
    )
    
    try:
        db.session.add(contact)
        db.session.commit()
        return jsonify({'message': 'Contact message sent successfully', 'id': contact.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to send message'}), 500

@bp.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    """Get a specific contact message"""
    contact = Contact.query.get_or_404(id)
    return jsonify(contact.to_dict())

@bp.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    """Update contact message (mark as read)"""
    contact = Contact.query.get_or_404(id)
    data = request.get_json()
    
    if 'read' in data:
        contact.read = data['read']
    
    try:
        db.session.commit()
        return jsonify(contact.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update contact'}), 500

@bp.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    """Delete a contact message"""
    contact = Contact.query.get_or_404(id)
    
    try:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'message': 'Contact message deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete contact'}), 500
