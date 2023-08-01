from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200,null=False)
    isbn = models.CharField(max_length=150)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Userquery(models.Model):
    query = models.CharField(max_length=200)
    llmodel = models.CharField(max_length=150,null=True)
    maxlength = models.IntegerField(null=True)
    topk = models.IntegerField(null=True)
    prompt_template = models.CharField(max_length=250,null=True)
    reply = models.CharField(max_length=500)

    def __str__(self):
        return self.query

