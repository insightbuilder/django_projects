from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app_index',views.APP_INDEX, name='app_index'),
]

