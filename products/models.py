from django.db import models

# Create your models here.


class Products(models.Model):
    image = models.ImageField(blank=True , null= True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)