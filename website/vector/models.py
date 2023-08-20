from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    vid_id = models.CharField(max_length=50,default='')
    body = models.TextField()
    createdon = models.DateTimeField(auto_now=True)
    modifiedon = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True,null=True)
    category = models.ManyToManyField(Category, related_name="post")

    def __str__(self):
        return self.title
