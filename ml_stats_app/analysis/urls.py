# analysis/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("service/<str:service_id>/", views.service_page, name="service_page"),
    path("process/<str:service_id>/", views.process_data, name="process_data"),
    path("add_service/", views.add_service, name="add_service"),
    path("upload/", views.upload_dataset, name="upload_dataset"),
    path(
        "train_linear_regression/<int:dataset_id>/",
        views.train_linear_regression,
        name="train_linear_regression",
    ),
    path("mean/", views.mean_view, name="mean_view"),
    path("median/", views.median_view, name="median_view"),
    path("mode/", views.mode_view, name="mode_view"),
    path("std_dev/", views.standard_deviation_view, name="std_dev_view"),
    path("correlation/", views.correlation_view, name="correlation_view"),
    path("import_services/", views.import_services, name="import_services"),
]
