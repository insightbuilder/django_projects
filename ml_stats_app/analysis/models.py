# analysis/models.py

from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="datasets/")


class MLModel(models.Model):
    name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="models/")


class Service(models.Model):
    CATEGORY_CHOICES = [
        ("ML", "Machine Learning"),
        ("Stat", "Statistical Analysis"),
        ("Data Analysis", "Data Analysis"),
        ("Customer Engagement", "Customer Engagement"),
        ("Banking Sector", "Banking Sector"),
        ("Large Language Models", "Large Language Models"),
        ("Marketing Analysis", "Marketing Analysis"),
        ("Product Management", "Product Management"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    dataset_instructions = models.TextField()
    use_cases = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
