# employees/urls.py

from django.urls import path
from .views import (
    employee_list,
    employee_create,
    employee_update,
    employee_delete,
    bulk_import,
    salary_history,
    bulk_delete,
)

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("create/", employee_create, name="employee_create"),
    path("update/<int:id>/", employee_update, name="employee_update"),
    path("delete/<int:id>/", employee_delete, name="employee_delete"),
    path("import/", bulk_import, name="bulk_import"),
    path("bulk_delete/", bulk_delete, name="bulk_delete"),
    path("salary_history/<int:id>/", salary_history, name="salary_history"),
]
