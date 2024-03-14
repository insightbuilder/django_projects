from django.db import models


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mail_id = models.EmailField()


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    category = models.IntegerField()
    owner = models.ForeignKey(Owner,
                              on_delete=models.CASCADE,)
