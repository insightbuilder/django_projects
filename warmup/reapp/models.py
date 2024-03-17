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


class Query(models.Model):
    query = models.CharField(max_length=1024,
                             null=True)
    response_text = models.CharField(max_length=5000,
                                     null=True)
    model_used = models.CharField(max_length=25,
                                  null=False,
                                  blank=True)