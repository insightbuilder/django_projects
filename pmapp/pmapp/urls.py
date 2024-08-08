"""
URL configuration for pmapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from danalysis.views import (
    ProjectViewSet,
    TaskViewSet,
    EmployeeViewSet,
    AssignmentViewSet,
    ProjectUpdateViewSet,
    DataAnalysisView,
)

# Here is where rest_framework router is coming in
router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"assignments", AssignmentViewSet)
router.register(r"project-updates", ProjectUpdateViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("danalysis/", include(router.urls)),
    path("danalysis/analysis", DataAnalysisView.as_view(), name="data-analysis"),
]
