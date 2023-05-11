from django.contrib import admin

# Register your models here.
from .models import Order, OrderStatus, OrderPaymentMethod, Country

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'billing_name', 'billing_address', 'billing_city', 'billing_postal_code', 'billing_country', 'payment_method')

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'type')

class OrderPaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'method', 'description')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(OrderPaymentMethod, OrderPaymentMethodAdmin)
admin.site.register(Country)
