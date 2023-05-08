from django.db import models
from cart.models import Cart
from users.models import User

class OrderStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OrderPaymentMethod(models.Model):
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    billing_name = models.CharField(null=True)
    billing_address = models.CharField(null=True)
    billing_city = models.CharField(null=True)
    billing_postal_code = models.CharField(null=True)
    billing_country = models.CharField(null=True)
    payment_method = models.ForeignKey(OrderPaymentMethod, on_delete=models.SET_NULL, null=True)
    payment_card_name = models.CharField(null=True)
    payment_card_number = models.CharField(null=True)
    payment_expiry_month = models.CharField(null=True)
    payment_expiry_year = models.CharField(null=True)
    payment_cvc = models.CharField(null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"

