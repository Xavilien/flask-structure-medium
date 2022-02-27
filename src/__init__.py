"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database setup
db = SQLAlchemy()


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('src.config.Config')

    db.init_app(app)

    with app.app_context():
        from src.models.user import User  # this import allows us to create the table if it does not exist
        db.create_all()

        # Register Blueprints
        from src.users.routes import bp as users_bp
        app.register_blueprint(users_bp)

        return app
