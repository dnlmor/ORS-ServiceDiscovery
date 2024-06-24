from .models import Service
from .database import db_session
from .utils import generate_service_id, validate_service_name, validate_host, validate_port, format_service_data
from sqlalchemy.exc import IntegrityError

class ServiceDiscoveryService:
    @staticmethod
    def register_service(name, host, port):
        try:
            name = validate_service_name(name)
            host = validate_host(host)
            port = validate_port(port)
            
            service = Service(
                id=generate_service_id(),
                name=name,
                host=host,
                port=port
            )
            db_session.add(service)
            db_session.commit()
            return format_service_data(service)
        except IntegrityError:
            db_session.rollback()
            raise ValueError("Failed to register service")

    @staticmethod
    def deregister_service(id):
        service = Service.query.get(id)
        if not service:
            raise ValueError("Service not found")
        
        db_session.delete(service)
        db_session.commit()
        return True

    @staticmethod
    def get_service_by_id(id):
        service = Service.query.get(id)
        if not service:
            raise ValueError("Service not found")
        return format_service_data(service)

    @staticmethod
    def list_services():
        services = Service.query.all()
        return [format_service_data(service) for service in services]
