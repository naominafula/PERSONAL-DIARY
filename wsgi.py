"""
WSGI entry point for gunicorn in production.
This ensures all blueprints are properly registered before the app starts.
"""
from app import app, db

# Ensure database tables are created
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()

