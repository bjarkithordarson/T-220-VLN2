from django.db import models
from cart.models import Cart
from users.models import User
from . import validators

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OrderStatus(models.Model):
    INITIAL = 1
    RECEIVED = 2
    PROCESSING = 3
    FINISHED = 4
    CANCELLED = 5

    ORDER_STATUS_TYPE_CHOICES = [
        (INITIAL, 'Initial'),
        (RECEIVED, 'Received'),
        (PROCESSING, 'Processing'),
        (FINISHED, 'Finished'),
        (CANCELLED, 'Cancelled')
    ]

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.IntegerField(choices=ORDER_STATUS_TYPE_CHOICES, default=INITIAL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Order statuses"

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
    billing_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey(OrderPaymentMethod, on_delete=models.SET_NULL, null=True)
    payment_card_name = models.CharField(null=True, )
    payment_card_number = models.CharField(null=True, validators=[validators.credit_card_number_validator])
    payment_expiry_month = models.CharField(null=True, validators=[validators.expiry_month_validator])
    payment_expiry_year = models.CharField(null=True, validators=[validators.expiry_year_validator])
    payment_cvc = models.CharField(null=True, validators=[validators.cvc_validator])

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = OrderStatus.objects.filter(type=OrderStatus.INITIAL).first()

        super().save(*args, **kwargs)

    def validate_billing_info(self):
        if not self.billing_name:
            return False
        if not self.billing_address:
            return False
        if not self.billing_city:
            return False
        if not self.billing_postal_code:
            return False
        if not self.billing_country:
            return False
        return True

    def validate_payment_info(self):
        if not self.payment_method:
            return False
        if self.payment_method.method == 'pickup':
            return True
        if not self.payment_card_name:
            return False
        if not self.payment_card_number:
            return False
        if not self.payment_expiry_month:
            return False
        if not self.payment_expiry_year:
            return False
        if not self.payment_cvc:
            return False
        return True

    def is_user_editable(self):
        print("=====================================")
        print(self.status.type)
        print(self.status)
        return self.status.type in [
            OrderStatus.INITIAL,
        ]

    def is_closed(self):
        return self.status.type in [
            OrderStatus.FINISHED,
            OrderStatus.CANCELLED
        ]

    def __str__(self):
        return f"Order #{self.id} by {self.user}"
