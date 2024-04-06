from django.urls import path
from .views import (
    welcome,
    get_name,
    get_req,
    post_req,
    streaming_view,
    streamer_load,
)

urlpatterns = [
    path("", welcome, name='root'),
    path("gn/<str:name>", get_name, name='gn'),
    path("get_req/", get_req, name='get_req'),
    path("post_req/", post_req, name='post_req'),
    path("stream/", streaming_view, name='stream'),
    path("load/", streamer_load, name='stload'),
]