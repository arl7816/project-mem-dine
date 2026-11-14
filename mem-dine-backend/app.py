# backend/app.py
from flask import Flask
from flask_cors import CORS

from controllers.health_controller import health_blueprint
from controllers.user_controller import user_blueprint
from settings import settings

def create_app():
    application = Flask(__name__)
    CORS(application, resources={r"/*": {"origins": "http://localhost:5173"}})
    application.register_blueprint(user_blueprint)
    application.register_blueprint(health_blueprint)
    return application


app = create_app()

# to get me started up run 'python app.py'
if __name__ == '__main__':
    app.run(port=settings.port, debug=settings.debug)
