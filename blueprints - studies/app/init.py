from flask import Flask
from .auth import auth_bp
from .main import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    return app