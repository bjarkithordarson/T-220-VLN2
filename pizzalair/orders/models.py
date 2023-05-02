from django.db import models

# Create your models here.
class Order(models.Model):
    #cart = models.ForeignKey(Cart)
    #user = models.ForeignKey(User)
    is_paid = models.BooleanField(default=False)
    billing_name = models.TextField()
    billing_address = models.TextField()
    billing_city = models.TextField()
    billing_postal_code = models.TextField()
    billing_country = models.TextField()
