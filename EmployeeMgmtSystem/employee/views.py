# employees/views.py
import io
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, SalaryHistory
from .forms import EmployeeForm, BulkImportForm
from io import TextIOWrapper
import matplotlib.pyplot as plt


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employees": employees})


def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "employee/employee_form.html", {"form": form})


def employee_update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employee/employee_form.html", {"form": form})


def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(
        request, "employee/employee_confirm_delete.html", {"employee": employee}
    )


def bulk_import(request):
    if request.method == "POST":
        form = BulkImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = TextIOWrapper(request.FILES["csv_file"].file, encoding="utf-8")
            reader = csv.DictReader(csv_file)
            for row in reader:
                employee, created = Employee.objects.update_or_create(
                    email=row["email"],
                    defaults={
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "phone_number": row["phone_number"],
                        "department": row["department"],
                        "position": row["position"],
                        "date_hired": row["date_hired"],
                        "salary": row["salary"],
                    },
                )
                if created or employee.salary != float(row["salary"]):
                    SalaryHistory.objects.create(
                        employee=employee, salary=row["salary"]
                    )
            messages.success(request, "Employees imported successfully.")
            return redirect("employee_list")
    else:
        form = BulkImportForm()
    return render(request, "employee/bulk_import.html", {"form": form})


def bulk_delete(request):
    if request.method == "POST":
        ids = request.POST.getlist("ids")
        Employee.objects.filter(id__in=ids).delete()
        return redirect("employee_list")
    employees = Employee.objects.all()
    return render(request, "employee/bulk_delete.html", {"employees": employees})


def salary_history(request, id):
    employee = Employee.objects.get(id=id)
    salary_history = SalaryHistory.objects.filter(employee=employee).values(
        "date", "salary"
    )
    salary_history_list = list(salary_history)
    for rec in salary_history_list:
        rec["salary"] = int(rec["salary"])

    chart_img = generate_salary_chart(id)

    return render(
        request,
        "employee/salary_history.html",
        {
            "employee": employee,
            "salary_history": salary_history,
            "chart_img": chart_img,
        },
    )


def generate_salary_chart(employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    salary_history = SalaryHistory.objects.filter(employee=employee).values(
        "date", "salary"
    )

    dates = [record["date"] for record in salary_history]
    salaries = [record["salary"] for record in salary_history]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, salaries, marker="o", linestyle="-", color="b")
    plt.title(f"Salary History for {employee.first_name} {employee.last_name}")
    plt.xlabel("Date")
    plt.ylabel("Salary")
    plt.grid(True)

    # Save plot to a BytesIO object and return it as an image
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()

    return img
