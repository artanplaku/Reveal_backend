from django.db import models
from django.conf import settings
# Create your models here.
class Product(models.Model):
    


    image = models.TextField()
    name = models.CharField(max_length=100, default='no product name')
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default='no product name')
    
   

    def __str__(self):
        return self.name