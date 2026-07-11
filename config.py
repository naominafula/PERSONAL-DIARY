from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-this-in-production'

db = SQLAlchemy(app)
jwt = JWTManager(app)