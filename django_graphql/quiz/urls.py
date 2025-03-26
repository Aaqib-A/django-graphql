from django.urls import re_path
from graphene_django.views import GraphQLView
from quiz.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r"graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
