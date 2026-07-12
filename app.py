import sys

try:
    from config import app, db
    from auth import auth_bp
    from routes import routes_bp
except ModuleNotFoundError as e:
    sys.stderr.write(f"ModuleNotFoundError: {e}\n")
    sys.stderr.write("It looks like required packages are not installed in the active Python.\n")
    sys.stderr.write("Use the project's virtual environment:\n")
    sys.stderr.write("  source venv/bin/activate\n")
    sys.stderr.write("or run the app with the venv Python: ./venv/bin/python app.py\n")
    raise

# Register our split sections as blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Generates SQLite diary.db tables inside your project folder
    app.run(debug=True)