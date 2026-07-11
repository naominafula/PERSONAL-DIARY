from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
from config import db
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    data = request.get_json()
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({"message": "User already exists"}), 400
    
    new_user = User(username=data.get('username'), password=data.get('password'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Account created successfully"}), 201

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username'), password=data.get('password')).first()
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200