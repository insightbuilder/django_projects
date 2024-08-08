from io import BytesIO
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Project, Task, Employee, Assignment, ProjectUpdate
from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    EmployeeSerializer,
    AssignmentSerializer,
    ProjectUpdateSerializer,
)
import matplotlib.pyplot as plt
import pandas as pd


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class ProjectUpdateViewSet(viewsets.ModelViewSet):
    queryset = ProjectUpdate.objects.all()
    serializer_class = ProjectUpdateSerializer
    # Serializers are required when it is going to sent out as response


class DataAnalysisView(APIView):
    def get(self, request, *args, **kwargs):
        operation = request.query_params.get("operation")

        if operation == "bar_chart":
            return self.bar_chart()
        elif operation == "line_chart":
            return self.line_chart()
        elif operation == "scatter_plot":
            return self.scatter_plot()
        else:
            return Response({"error": "Invalid operation"}, status=400)

    def bar_chart(self):
        tasks = Task.objects.all()
        df = pd.DataFrame(list(tasks.values("title", "due_date")))

        plt.figure(figsize=(10, 6))
        df["title"].value_counts().plot(kind="bar")
        plt.title("Task Count by Title")
        plt.xlabel("Task Title")
        plt.ylabel("Count")

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close()

        return HttpResponse(buffer.getvalue(), content_type="image/png")

    def line_chart(self):
        assignments = Assignment.objects.all()
        df = pd.DataFrame(list(assignments.values("assigned_date", "status")))

        df["assigned_date"] = pd.to_datetime(df["assigned_date"])
        df = df.groupby("assigned_date").size()

        plt.figure(figsize=(10, 6))
        df.plot(kind="line")
        plt.title("Assignments Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Assignments")

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close()

        return HttpResponse(buffer.getvalue(), content_type="image/png")

    def scatter_plot(self):
        tasks = Task.objects.all()
        df = pd.DataFrame(list(tasks.values("due_date", "priority")))

        priority_mapping = {"High": 3, "Medium": 2, "Low": 1}
        df["priority"] = df["priority"].map(priority_mapping)

        plt.figure(figsize=(10, 6))
        plt.scatter(df["due_date"], df["priority"])
        plt.title("Task Priority by Due Date")
        plt.xlabel("Due Date")
        plt.ylabel("Priority")

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close()

        return HttpResponse(buffer.getvalue(), content_type="image/png")
