from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mail_id = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=512)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.desc

