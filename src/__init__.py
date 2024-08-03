import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Add the parent directory of the src module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import routes inside the factory function to avoid circular imports
    from .routes import bp as students_bp
    app.register_blueprint(students_bp)

    @app.route('/api/v1/healthcheck', methods=['GET'])
    def healthcheck():
        return {"status": "ok"}, 200

    return app
