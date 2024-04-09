from django.urls import path, include
from .views import (
    dashboard,
    register
)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name='dash'),
    path("register/", register, name='register'),
]