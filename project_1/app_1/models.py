from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200,null=False)
    isbn = models.CharField(max_length=150)
    qty = models.IntegerField(default=0)
