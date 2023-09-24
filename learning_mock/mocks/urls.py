from django.urls import path
from . import views

urlpatterns = [
    path('pdt/', views.product_view, name='pdt')
]