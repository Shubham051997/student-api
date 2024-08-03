import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


# Add the parent directory of the src module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src import routes, models
# Register the Blueprint

   # Import routes after the app and db are initialized
from src.routes import bp as students_bp
app.register_blueprint(students_bp)

app.register_blueprint(routes.bp)

@app.route('/api/v1/healthcheck', methods=['GET'])
def healthcheck():
    return {"status": "ok"}, 200


from src import create_app



if __name__ == '__main__':
    app = create_app()
    with app.test_request_context():
        print(app.url_map)
    app.run()
