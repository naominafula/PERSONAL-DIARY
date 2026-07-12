
from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import db
from models import JournalEntry

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def homepage():
    """Renders the main visual dashboard layout."""
    return render_template('index.html')



@routes_bp.route('/login-page', methods=['GET'])
def login_page():
    """Renders the visual frontend Login form."""
    return render_template('login.html')



@routes_bp.route('/signup-page', methods=['GET'])
def signup_page():
    """Renders the visual frontend Signup form."""
    return render_template('signup.html')

@routes_bp.route('/my-entries', methods=['GET'])
def entries_page():
    """Renders a clean visual page explaining the private data auth gate."""
    return render_template('entries.html')

@routes_bp.route('/public-prompts', methods=['GET'])
def get_public_prompts():
    prompts = [
        {"id": 1, "prompt": "What are three things you are grateful for today?"},
        {"id": 2, "prompt": "Describe your ideal day in detail."},
        {"id": 3, "prompt": "What is a major challenge you overcame recently?"}
    ]
    return jsonify({"daily_prompts": prompts}), 200
@routes_bp.route('/api/entries', methods=['POST'])
@jwt_required()
def create_entry():
    current_user = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"message": "Title and Content are required fields"}), 400

    new_entry = JournalEntry(
        username=current_user,
        title=data.get('title'),
        content=data.get('content'),
        mood=data.get('mood', 'Neutral')
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Diary entry saved!", "entry": new_entry.to_dict()}), 201
@routes_bp.route('/api/entries', methods=['GET'])
@jwt_required()
def get_my_entries():
    current_user = get_jwt_identity()
    user_entries = JournalEntry.query.filter_by(username=current_user).all()
    
    return jsonify([entry.to_dict() for entry in user_entries]), 200
@routes_bp.route('/api/entries/<int:entry_id>', methods=['DELETE'])
@jwt_required()
def delete_entry(entry_id):
    current_user = get_jwt_identity()
    entry = JournalEntry.query.get(entry_id)
    if not entry:
        return jsonify({"message": f"Entry ID {entry_id} not found"}), 404
    if entry.username != current_user:
        return jsonify({"message": "Unauthorized to delete this entry"}), 403
    try:
        db.session.delete(entry)
        db.session.commit()
        return jsonify({"message": "Entry deleted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500 