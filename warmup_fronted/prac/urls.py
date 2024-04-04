from django.urls import path
from .views import (
    welcome,
    get_name,
    get_req,
    post_req
)

urlpatterns = [
    path("", welcome, name='root'),
    path("gn/<str:name>", get_name, name='gn'),
    path("get_req/", get_req, name='get_req'),
    path("post_req/", post_req, name='post_req'),
]