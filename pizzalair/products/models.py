from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify

class ProductCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, null=True)
    filter = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    pass
    #product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='Offer')
    #template = models.CharField(max_length=120)

class OfferTemplate(models.Model):
    offer = models.ForeignKey(Offer, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=120)
