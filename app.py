from config import app, db
from auth import auth_bp
from routes import routes_bp

# Register our split sections as blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Generates SQLite diary.db tables inside your project folder
    app.run(debug=True)