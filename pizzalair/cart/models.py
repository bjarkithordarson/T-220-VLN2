from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL)
    products = models.ManyToManyField(Product)
    amount = models.IntegerField(default=0)

