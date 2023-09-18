from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    quantity = models.IntegerField()
    published_on = models.DateField(auto_now=True)
    
    @property
    def have_stock(self):
        return self.quantity > 0