from .models import Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.db.models import Sum
from django.http import Http404
from django.db import IntegrityError
from .helpers import *

# Create your views here.
def index(request):
    items = get_cart_items_if_any(request)
    print(items)
    context = {
        "test": "Session is not set!",
        "items": items,
        "cart_total": get_cart_total(request)
    }
    if request.session.get("cart"):
        context["test"] = "Session is set! The value is: " + str(request.session.get("cart"))

    return render(request, 'cart.html', context)

def add(request, product_id, quantity=1):
    cart = get_or_create_cart(request)
    product = Product.objects.get(id=product_id)
    print(product)
    cart_item = CartItem(
        product=product,
        name=product.name,
        quantity=quantity,
        item_price = product.price,
        total_price = product.price * quantity,
        cart=cart
    )
    try:
        cart_item.save()
    except IntegrityError:
        pass
    return redirect('cart')

def remove(request, cart_item_id):
    try:
        cart = get_or_create_cart(request)
        item = CartItem.objects.get(id=cart_item_id, cart=cart)
        item.delete()
    except:
        pass
    return redirect('cart')

def update(request, cart_item_id, quantity):
    item = get_object_or_404(CartItem, pk=cart_item_id)
    if item.cart.id == request.session['cart']:
        if quantity <= 0:
            remove(request, cart_item_id)
        else:
            item.quantity = quantity
            item.save()
        return redirect('cart')
    else:
        raise Http404("Cart item not found.")
