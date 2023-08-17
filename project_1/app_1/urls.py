from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app_index',views.APP_INDEX, name='app_index'),
    path('book',views.BOOK_DATA,name='book'),
    path('query_detail/<slug:slug>',views.QUERY_DETAIL,name='query_detail'),
    path('ggml',views.AI_GGML,name='ggml'),
    path('aipage',views.AI_PAGE,name='aipage'),
    path('chat',views.CHAT_PAGE,name='chat'),
    path('falconpg',views.F_PAGE, name='falconpg'),
    path('falcon', views.AI_FALCON, name='falcon'),
    path('video_detail/<slug:slug>', views.VIDEO_DETAIL, name='video_detail'),
    path('playlist_detail/<slug:slug>', views.PLAYLIST_DETAIL, name='playlist_detail'),
    path('gallery',views.GALLERY,name='gallery'),
    path('search',views.SEARCH,name='search')
]

