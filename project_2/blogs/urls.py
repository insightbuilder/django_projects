from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('blog_list/',views.blog_list,name='blog_list'),
    path('<int:pk>/',views.blog_detail,name='blog_detail'),
    path('cat/<int:pk>/',views.cat_filter,name='cat_filter'),
    path('search/',views.search,name='search'),
    path('reg/',views.reg_search,name='reg_search'),
]
