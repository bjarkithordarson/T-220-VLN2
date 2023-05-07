from django.contrib import admin

# Register your models here.
from .models import Order, OrderStatus, OrderPaymentMethod

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderPaymentMethod)
