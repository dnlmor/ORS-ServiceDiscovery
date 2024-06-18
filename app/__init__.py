from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.consul import register_consul_service

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)

    # Register Consul service
    register_consul_service(app)

    return app
