from .services import ServiceDiscoveryService

def resolve_register_service(info, name, host, port):
    return ServiceDiscoveryService.register_service(name, host, port)

def resolve_deregister_service(info, id):
    return ServiceDiscoveryService.deregister_service(id)

def resolve_get_service(info, id):
    return ServiceDiscoveryService.get_service_by_id(id)

def resolve_list_services(info):
    return ServiceDiscoveryService.list_services()
