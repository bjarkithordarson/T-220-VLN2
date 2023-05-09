from django.db import models
from cart.models import Cart
from users.models import User

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

    order_status_type = models.IntegerField(
        choices=ORDER_STATUS_TYPE_CHOICES,
        default=INITIAL
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.IntegerField(choices=ORDER_STATUS_TYPE_CHOICES, default=INITIAL)

    def is_closed(self):
        return self.order_status_type in [
            self.FINISHED,
            self.CANCELLED
        ]

    def is_user_editable(self):
        return self.order_status_type in [
            self.INITIAL
        ]
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
    billing_country = models.CharField(null=True)
    payment_method = models.ForeignKey(OrderPaymentMethod, on_delete=models.SET_NULL, null=True)
    payment_card_name = models.CharField(null=True)
    payment_card_number = models.CharField(null=True)
    payment_expiry_month = models.CharField(null=True)
    payment_expiry_year = models.CharField(null=True)
    payment_cvc = models.CharField(null=True)

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = OrderStatus.objects.filter(type=OrderStatus.OrderStatusType.INITIAL).first()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"
