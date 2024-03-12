from django.db import models


# Create your models here.
class Videos(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()
    genre = models.CharField(max_length=10)


class Subscriber(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
