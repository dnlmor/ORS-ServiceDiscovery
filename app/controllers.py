from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

service_discovery_blueprint = Blueprint('service_discovery', __name__)

service_discovery_blueprint.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
