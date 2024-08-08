# api/tests/test_crud.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from danalysis.models import Project, Task, Employee, Assignment, ProjectUpdate


class CRUDTestCase(APITestCase):
    def setUp(self):
        self.project_data = {
            "name": "Test Project",
            "description": "Test Description",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "status": "Active",
        }
        self.task_data = {
            "title": "Test Task",
            "description": "Test Task Description",
            "due_date": "2023-06-01",
            "priority": "High",
        }
        self.employee_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "role": "Developer",
        }
        self.assignment_data = {"assigned_date": "2023-01-15", "status": "In Progress"}
        self.update_data = {
            "update_date": "2023-02-01",
            "update_text": "Initial update",
        }

    def tearDown(self):
        # Clean up after each test
        Project.objects.all().delete()
        Task.objects.all().delete()
        Employee.objects.all().delete()
        Assignment.objects.all().delete()
        ProjectUpdate.objects.all().delete()

    def test_create_project(self):
        response = self.client.post(reverse("project-list"), self.project_data)
        # Post and get the updated elements directly from the Project Table
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

    def test_create_task(self):
        project = Project.objects.create(**self.project_data)
        self.task_data["project"] = project.id
        response = self.client.post(reverse("task-list"), self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_create_employee(self):
        response = self.client.post(reverse("employee-list"), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

    def test_create_assignment(self):
        project = Project.objects.create(**self.project_data)
        task = Task.objects.create(project=project, **self.task_data)
        employee = Employee.objects.create(**self.employee_data)
        self.assignment_data["task"] = task.id
        self.assignment_data["employee"] = employee.id
        response = self.client.post(reverse("assignment-list"), self.assignment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Assignment.objects.count(), 1)

    def test_create_update(self):
        project = Project.objects.create(**self.project_data)
        self.update_data["project"] = project.id
        response = self.client.post(reverse("projectupdate-list"), self.update_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProjectUpdate.objects.count(), 1)
