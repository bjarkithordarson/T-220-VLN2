from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    description = models.TextField()
    picture = models.ImageField()
    loyalty_points = models.IntegerField(default=0)
    loyalty_points_only = models.BooleanField(default=False)
    #category = model.ForeignKey(ProductCategory)

class ProductCategory(models.Model):
    name = models.CharField(max_length=120)
    #product = model.ForeignKey(Product)

class Pizza(models.Model):
    toppings = models.CharField(max_length=120)

class Offer(models.Model):
    #products=models.ForeignKey(Product)
    template = models.CharField(max_length=120)

