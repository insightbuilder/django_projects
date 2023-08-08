from django.urls import path
from . import views

urlpatterns = [
    path('',views.HOME,name='home'),
    path('video_filter/<slug:slug>',views.VIDEO_FILTER,name='video_filter'),
]
