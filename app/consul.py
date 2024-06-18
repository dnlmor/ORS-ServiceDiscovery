import consul
from flask import current_app

def register_consul_service(app):
    consul_host = app.config.get('CONSUL_HOST')
    consul_port = app.config.get('CONSUL_PORT')
    service_name = app.config.get('SERVICE_NAME')
    service_tags = app.config.get('SERVICE_TAGS')

    # Initialize Consul client
    client = consul.Consul(host=consul_host, port=consul_port)

    # Register service with Consul
    app_address = 'http://localhost:5000'  # Replace with your service address
    check_url = f'{app_address}/health'   # Optional health check URL
    client.agent.service.register(
        service_name,
        service_id=service_name,
        address='localhost',
        port=5000,
        tags=service_tags,
        check=consul.Check.http(check_url, interval='10s') if check_url else None
    )
