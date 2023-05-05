from django.db import models
from django.utils.html import mark_safe

class ProductCategory(models.Model):
    name = models.CharField(max_length=120)
    filter = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ManyToManyField(ProductCategory)
    picture = models.ImageField()
    loyalty_points = models.IntegerField(default=0)
    loyalty_points_only = models.BooleanField(default=False)
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
             url=self.picture.url
         ))


    def __str__(self):
        return self.name


class Pizza(Product):
    #product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='Pizza')
    toppings = models.CharField(max_length=120)

class Offer(Product):
    #product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='Offer')
    template = models.CharField(max_length=120)
