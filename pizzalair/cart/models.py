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
    def __str__(self):
        return f"Anonymous cart created at {self.created_at}"

class CartItem(models.Model):
    name = models.CharField()
    quantity = models.IntegerField(default=1)
    item_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.quantity}x {self.name} at {self.total_price} ISK"

class CartProductItem(CartItem):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class CartOfferItem(CartItem):
    offer = models.ForeignKey(OfferInstance, on_delete=models.SET_NULL, null=True)


@receiver(pre_save, sender=CartProductItem)
def signal_pre_save_cart_product_item(sender, instance, using, **kwargs):
    instance.total_price = instance.item_price * instance.quantity

    try:
        item = CartProductItem.objects.exclude(id=instance.id).get(cart=instance.cart, product=instance.product)
        item.quantity += instance.quantity
        item.save()
        raise IntegrityError('Save operation cancelled')
    except ObjectDoesNotExist:
        pass


@receiver(pre_save, sender=CartOfferItem)
def signal_pre_save_cart_offer_item(sender, instance, using, **kwargs):
    instance.total_price = instance.item_price * instance.quantity

    try:
        item = CartItem.objects.exclude(id=instance.id).get(cart=instance.cart, product=instance.offer)
        item.quantity += instance.quantity
        item.save()
        raise IntegrityError('Save operation cancelled')
    except ObjectDoesNotExist:
        pass


@receiver(post_delete, sender=CartItem)
def signal_post_delete_cart_item(sender, instance, using, **kwargs):
    # Delete the cart if it's empty
    items = CartItem.objects.filter(cart=instance.cart)
    if len(items) == 0:
        instance.cart.delete()
