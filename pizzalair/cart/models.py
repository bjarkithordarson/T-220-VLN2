import datetime

from django.db import models
from products.models import Product
from user.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateField(defult = datetime)

class CartItem(models.Model):
    products = models.ManyToManyField(Product)
    amount = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

