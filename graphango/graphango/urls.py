from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# from cookbook.schema import schema

# urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
