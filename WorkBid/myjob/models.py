from django.db import models

# Create your models here.

#job_title,job_description,budget,type,experience_level,bid_value,author

class Work(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    budget = models.IntegerField()
    work_type = models.CharField(max_length=25)
    experience_level = models.CharField(max_length=25)
    author = models.CharField(max_length=125)

#one job can be associated with many bids by different users
class Bid(models.Model):
    user = models.CharField(max_length=100)
    work = models.ForeignKey(Work,on_delete=models.CASCADE)  
    bid_value = models.IntegerField(null=False,default=0)

