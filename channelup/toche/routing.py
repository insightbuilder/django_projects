from django.urls import re_path

from .consumers import ChatConsumer
from .another_consumer import NewConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    re_path(r"ws/(?P<oroute>\w+)/$", NewConsumer.as_asgi()),
]