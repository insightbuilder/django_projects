from django.urls import path
from .views import (
    index,
    roomname,
)

urlpatterns = [
    path('', index, name='home'),
    path('<str:room_name>/', roomname, name='room'),
]