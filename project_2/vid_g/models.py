from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

class Video(models.Model):
    video_id = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    category_id = models.ForeignKey(on_delete=models.CASCADE)
    thumbnail_link = models.CharField(max_length=150)
    description = models.CharField(max_length=2000)
    slug = models.SlugField(default='',max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title
