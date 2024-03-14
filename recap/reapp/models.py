from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mail_id = models.EmailField()


class Task(models.Model):
    owner = models.ForeignKey(Owner,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    category = models.IntegerField()