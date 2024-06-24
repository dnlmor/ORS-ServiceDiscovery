import uuid
import re

def generate_service_id():
    """
    Generate a unique service ID using UUID.
    """
    return str(uuid.uuid4())

def validate_service_name(name):
    """
    Validate the service name.
    - Must be between 2 and 50 characters
    - Can only contain letters, numbers, spaces, and hyphens
    """
    if not 2 <= len(name) <= 50:
        raise ValueError("Service name must be between 2 and 50 characters")
    if not re.match(r'^[a-zA-Z0-9\s-]+$', name):
        raise ValueError("Service name can only contain letters, numbers, spaces, and hyphens")
    return name

def validate_host(host):
    """
    Validate the host.
    - Must be a valid IP address or hostname
    """
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format")
    return host

def validate_port(port):
    """
    Validate the port.
    - Must be an integer between 1 and 65535
    """
    if not (1 <= port <= 65535):
        raise ValueError("Port must be between 1 and 65535")
    return port

def format_service_data(service):
    """
    Format the service data for display.
    """
    return {
        'id': service.id,
        'name': service.name,
        'host': service.host,
        'port': service.port,
        'registered_at': service.registered_at.isoformat()
    }
