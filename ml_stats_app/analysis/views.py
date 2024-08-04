# analysis/views.py
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.http import HttpResponse
from .models import Dataset, Service
from .forms import ServiceForm, CSVImportForm
from django.contrib import messages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import io
import numpy as np
from scipy import stats
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
import csv
import json


def landing_page(request):
    # Fetch services categorized by each type
    ml_services = Service.objects.filter(category="ML")
    stat_services = Service.objects.filter(category="Stat")
    data_analysis_services = Service.objects.filter(category="Data Analysis")
    # customer_engagement_services = Service.objects.filter(
    #     category="Customer Engagement"
    # )
    # banking_services = Service.objects.filter(category="Banking Sector")
    # llm_services = Service.objects.filter(category="Large Language Models")
    # marketing_analysis_services = Service.objects.filter(category="Marketing Analysis")
    # product_management_services = Service.objects.filter(category="Product Management")

    context = {
        "ml_services": ml_services,
        "stat_services": stat_services,
        "data_analysis_services": data_analysis_services,
        # "customer_engagement_services": customer_engagement_services,
        # "banking_services": banking_services,
        # "llm_services": llm_services,
        # "marketing_analysis_services": marketing_analysis_services,
        # "product_management_services": product_management_services,
    }

    return render(request, "analysis/landing_page.html", context)


def service_page(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    dataset = None
    results = None

    if request.method == "POST":
        dataset_file = request.FILES["dataset"]
        fs = FileSystemStorage()
        filename = fs.save(dataset_file.name, dataset_file)
        dataset_path = fs.url(filename)

        # Read and display dataset
        dataset = pd.read_csv(dataset_path)
        dataset_headers = dataset.columns.tolist()
        dataset_rows = dataset.values.tolist()

        # Process the dataset based on service
        if service.name == "Linear Regression":
            results = "Processing Linear Regression..."
            # Add Linear Regression processing code here

        # Add other service-specific processing code here

        context = {
            "service": service,
            "dataset": {"headers": dataset_headers, "rows": dataset_rows},
            "results": results,
        }
    else:
        context = {"service": service}

    return render(request, "analysis/service_details.html", context)


def process_data(request, service_id):
    if request.method == "POST":
        service = get_object_or_404(Service, id=service_id)
        dataset = request.FILES["dataset"]

        # Here you would process the uploaded dataset
        # For demonstration, let's just read and print the CSV content
        decoded_file = dataset.read().decode("utf-8").splitlines()
        reader = csv.reader(decoded_file)
        for row in reader:
            print(row)

        # Redirect to the service detail page after processing
        return redirect("service_detail", service_id=service_id)
    return redirect("landing_page")


def add_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.use_cases = json.dumps(request.POST.getlist("use_cases"))
            service.save()
            return redirect("landing_page")
    else:
        form = ServiceForm()
    return render(request, "analysis/add_services.html", {"form": form})


def import_services(request):
    if request.method == "POST" and request.FILES["csv_file"]:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith(".csv"):
            messages.error(request, "This is not a CSV file")
            return redirect("import_services")
        # print(csv_file.name)
        file_data = csv_file.read().decode("UTF-8")
        lines = file_data.split("\n")
        reader = csv.reader(lines)

        # Skip header row if present
        next(reader, None)

        for row in reader:
            # print(row[1])
            if row:  # Ensure row is not empty
                _, created = Service.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    description=row[2],
                    dataset_instructions=row[3],
                    use_cases=row[4],
                    category=row[5],  # Ensure this matches the order in your CSV
                )
        messages.success(request, "Services imported successfully")
        return redirect("landing_page")

    return render(request, "analysis/import_services.html")


# not required, replaced with process_dataset
def upload_dataset(request):
    if request.method == "POST":
        file = request.FILES["file"]
        dataset = Dataset.objects.create(file=file)
        return HttpResponse("Dataset uploaded successfully")
    return render(request, "analysis/upload_dataset.html")


def train_linear_regression(request, dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    data = pd.read_csv(dataset.file.path)
    X = data[["feature1", "feature2"]]
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    # Save the model
    model_file = io.BytesIO()
    joblib.dump(model, model_file)
    model_file.seek(0)

    return HttpResponse(f"Model trained. Mean Squared Error: {mse:.2f}")


def mean_view(request):
    data = np.array([1, 2, 3, 4, 5])
    mean = np.mean(data)
    return HttpResponse(f"Mean: {mean:.2f}")


def median_view(request):
    data = np.array([1, 2, 3, 4, 5])
    median = np.median(data)
    return HttpResponse(f"Median: {median:.2f}")


def mode_view(request):
    data = np.array([1, 1, 2, 3, 4])
    mode = stats.mode(data)[0][0]
    return HttpResponse(f"Mode: {mode}")


def standard_deviation_view(request):
    data = np.array([1, 2, 3, 4, 5])
    std_dev = np.std(data)
    return HttpResponse(f"Standard Deviation: {std_dev:.2f}")


def correlation_view(request):
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    correlation = np.corrcoef(x, y)[0, 1]
    return HttpResponse(f"Correlation: {correlation:.2f}")

