from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    qty = models.IntegerField()