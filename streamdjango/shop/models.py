from django.db import models
from datetime import date


class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    card = models.CharField(max_length=20)


class Purchase(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_purchase = models.CharField(max_length=75)
    price = models.FloatField()
    quantity = models.IntegerField()
    total_spend = models.FloatField()
    purchase_ts = models.DateTimeField(blank=True,
                                       default=date.today)


class questions(models.Model):
    question = models.TextField()
    prompt = models.TextField(blank=True)
    answer = models.TextField()
    asked_ts = models.DateTimeField(blank=True, default=date.today)