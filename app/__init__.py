from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # Ensure instance folder exists
    instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "instance")
    os.makedirs(instance_path, exist_ok=True)

    # Configure the app with an absolute path
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(instance_path, 'db.sqlite')}"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "temporary_secret_key")

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # User loader for Flask-Login: tells Flask-Login how to retrieve a user by ID.
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from .routes import main_bp  # general routes
    from .auth import auth_bp  # authentication routes
    from .learning_routes import learning_bp # learning routes
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")  # auth routes will be prefixed with /auth
    app.register_blueprint(learning_bp)

    return app
