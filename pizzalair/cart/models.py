import datetime
from _decimal import Decimal

from django.db import models, IntegrityError
from django.db.models.signals import post_delete, pre_save
from django.conf import settings
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from users.models import User
from products.models import Product, OfferInstance


class Cart(models.Model):
    created_at = models.DateField(auto_now=True)
    def total_price(self):
        return sum([item.total_price() for item in self.items.filter(pay_with_loyalty_points=False)])
    def total_loyalty_points_bonus(self):
        return sum([item.total_loyalty_points_bonus() for item in self.items.all()])

    def total_loyalty_points_price(self):
        return sum([item.total_price() for item in self.items.filter(pay_with_loyalty_points=True)])

    def __str__(self):
        return f"Anonymous cart created at {self.created_at}"

class CartItem(models.Model):
    name = models.CharField()
    quantity = models.IntegerField(default=1)
    item_price = models.IntegerField(default=0)
    item_loyalty_points_bonus = models.IntegerField(default=0)
    pay_with_loyalty_points = models.BooleanField(default=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.quantity}x {self.name} at {self.total_price()} " + ("ISK" if not self.pay_with_loyalty_points else "LP")

    def total_price(self):
        return self.quantity * self.item_price

    def total_loyalty_points_bonus(self):
        return self.quantity * self.item_loyalty_points_bonus

class CartProductItem(CartItem):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class CartOfferItem(CartItem):
    offer = models.ForeignKey(OfferInstance, on_delete=models.SET_NULL, null=True)

@receiver(post_delete, sender=CartItem)
def signal_post_delete_cart_item(sender, instance, using, **kwargs):
    # Delete the cart if it's empty
    items = CartItem.objects.filter(cart=instance.cart)
    if len(items) == 0:
        instance.cart.delete()
