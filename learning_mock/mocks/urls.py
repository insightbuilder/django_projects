from django.urls import path
from . import views

app_name = 'mocks'

urlpatterns = [
    path('pdt/', views.product_view, name='pdt')
]