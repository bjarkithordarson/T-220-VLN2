from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class Cart(models.Model):
    users = models.ManyToManyField(User)
    products = models.ManyToManyField(Product)
    amount = models.IntegerField(default=0)

