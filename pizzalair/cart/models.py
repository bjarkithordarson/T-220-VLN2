from django.db import models

# Create your models here.
class Cart(models.Model):
    #user = models.ForeignKey(User)
    #products = models.ForeignKey(Product)
    amount = models.IntegerField(default=0)

