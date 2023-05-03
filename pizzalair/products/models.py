from django.db import models
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    description = models.TextField()
    picture = models.ImageField()
    loyalty_points = models.IntegerField(default=0)
    loyalty_points_only = models.BooleanField(default=False)
    #category = model.ForeignKey(ProductCategory)
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
             url=self.picture.url
         ))
    def get_absolute_url(self):
        return reverse('')

class ProductCategory(models.Model):
    name = models.CharField(max_length=120)
    #product = model.ForeignKey(Product)

class Pizza(models.Model):
    toppings = models.CharField(max_length=120)

class Offer(models.Model):
    #products=models.ForeignKey(Product)
    template = models.CharField(max_length=120)

