class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///service_discovery.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONSUL_HOST = 'consul_host_address'  # Update with your Consul host address
    CONSUL_PORT = 8500  # Default Consul port
    SERVICE_NAME = 'ORS-ServiceDiscovery'
    SERVICE_TAGS = ['microservice', 'python']
