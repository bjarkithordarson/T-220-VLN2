import datetime
from _decimal import Decimal

from django.db import models
from users.models import User
from django.conf import settings
from products.models import Product


# Create your models here.
class Cart(models.Model):
    users = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateField(default = datetime)

    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    def add(self, product, quantity=1, overwrite_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quntity':0, 'price':str(product.proce)}

        if overwrite_quantity:
            self.cart[product_id]['quantity']=quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.object.filter(id = product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values()))

   
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

   """
class CartItem(models.Model):
    products = models.ManyToManyField(Product)
    amount = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


