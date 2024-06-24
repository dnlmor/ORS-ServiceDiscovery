import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Service as ServiceModel
from .resolvers import (
    resolve_register_service, resolve_deregister_service, resolve_get_service,
    resolve_list_services
)

class Service(SQLAlchemyObjectType):
    class Meta:
        model = ServiceModel

class Query(graphene.ObjectType):
    get_service = graphene.Field(Service, id=graphene.String(required=True))
    list_services = graphene.List(Service)

    def resolve_get_service(self, info, id):
        return resolve_get_service(info, id)

    def resolve_list_services(self, info):
        return resolve_list_services(info)

class RegisterService(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        host = graphene.String(required=True)
        port = graphene.Int(required=True)

    service = graphene.Field(lambda: Service)

    def mutate(self, info, name, host, port):
        return resolve_register_service(info, name, host, port)

class DeregisterService(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        return resolve_deregister_service(info, id)

class Mutation(graphene.ObjectType):
    register_service = RegisterService.Field()
    deregister_service = DeregisterService.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
