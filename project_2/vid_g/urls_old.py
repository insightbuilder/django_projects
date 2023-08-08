from django.urls import path
from . import views

urlpatterns = [
    path('',views.HOME,name='home'),
    path('gallery',views.GALLERY,name='gallery'),
    path('filter/<slug:slug>',views.FILTER_PL, name='filter'),
]

