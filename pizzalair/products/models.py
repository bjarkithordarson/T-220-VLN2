from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    description = models.TextField()
    picture = models.ImageField()
