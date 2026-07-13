import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Database configuration - supports both SQLite (development) and PostgreSQL (production)
database_url = os.getenv('DATABASE_URL', 'sqlite:///diary.db')
# Fix for SQLAlchemy 2.0+ PostgreSQL URL format
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key-change-in-production')

db = SQLAlchemy(app)
jwt = JWTManager(app)