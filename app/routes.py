from flask import Blueprint, request, jsonify
from app.models import Service
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['POST'])
def register_service():
    data = request.get_json()
    new_service = Service(name=data['name'], url=data['url'])
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'message': 'Service registered successfully'})

@bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([{'name': service.name, 'url': service.url} for service in services])
