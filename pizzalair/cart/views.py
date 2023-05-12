import json
from .models import Cart, CartItem, CartProductItem, CartOfferItem
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Offer, OfferInstance
from django.http import Http404, HttpResponse
from django.db import IntegrityError
from .helpers import *
from itertools import chain


# Create your views here.
def index(request):
    cart = get_or_create_cart(request)
    items = get_cart_items_if_any(request)

    context = {
        "test": "Session is not set!",
        "items": items,
        "cart_total": get_cart_total(request),
        "cart": cart,
        "error": request.GET.get('error', None)
    }
    if request.user.is_authenticated:
        context["loyalty_points"] = calculate_loyalty_points_balance(request.user, cart)
        
    if request.session.get("cart"):
        context["test"] = "Session is set! The value is: " + str(request.session.get("cart"))

    return render(request, 'cart.html', context)

def add(request, product_id, quantity=1):
    is_ajax = request.GET.get('ajax', False) != False

    cart = get_or_create_cart(request)
    product = Product.objects.get(id=product_id)
    cart_item = CartProductItem(
        product=product,
        name=product.name,
        quantity=quantity,
        item_price = product.price,
        item_loyalty_points_bonus=product.loyalty_points_bonus,
        pay_with_loyalty_points=product.pay_with_loyalty_points,
        cart=cart
    )
    try:
        cart_item.save()
    except IntegrityError:
        pass

    if is_ajax:
        data = {
            'id': cart_item.id,
            'quantity': cart_item.quantity,
            'item_price': cart_item.item_price,
            'item_total_price': cart_item.total_price(),
            'pay_with_loyalty_points': cart_item.pay_with_loyalty_points,
            'total_price': get_cart_total(request),
            'cart_count': len(get_cart_items_if_any(request))
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return redirect('cart')

def add_offer(request, offer_instance_id, quantity=1):
    is_ajax = request.GET.get('ajax', False) != False

    cart = get_or_create_cart(request)
    instance = OfferInstance.objects.get(id=offer_instance_id)
    cart_offer_item = CartOfferItem(
        offer=instance,
        name=str(instance),
        quantity=quantity,
        item_price=instance.offer.price,
        item_loyalty_points_bonus=instance.offer.loyalty_points_bonus,
        pay_with_loyalty_points=instance.offer.pay_with_loyalty_points,
        cart=cart
    )

    cart_offer_item.save()


    if True:
        data = {
            'id': cart_offer_item.id,
            'quantity': cart_offer_item.quantity,
            'item_price': cart_offer_item.item_price,
            'item_total_price': cart_offer_item.total_price(),
            'pay_with_loyalty_points': cart_offer_item.pay_with_loyalty_points,
            'total_price': get_cart_total(request),
            'cart_count': len(get_cart_items_if_any(request))
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return redirect('cart')

def remove(request, cart_item_id):

    if cart_item_id == 0:
        cart = get_or_create_cart(request)
        items = CartItem.objects.filter(cart_id=cart.id)
        for item in items:
            item.delete()
        return redirect('cart')
    try:
        cart = get_or_create_cart(request)
        item = CartItem.objects.get(id=cart_item_id, cart=cart)
        item.delete()
    except:
        pass
    return redirect('cart')

def update(request, cart_item_id, quantity):
    is_ajax = request.GET.get('ajax', False) != False
    item = get_object_or_404(CartItem, pk=cart_item_id)
    if item.cart.id == request.session['cart']:
        if quantity <= 0:
            remove(request, cart_item_id)
        else:
            item.quantity = quantity
            item.save()

        if is_ajax:
            data = {
                'id': item.id,
                'deleted': quantity <= 0,
                'quantity': item.quantity,
                'item_price': item.item_price,
                'item_total_price': item.total_price(),
                'total_price': item.cart.total_price(),
                'total_loyalty_points_bonus': item.cart.total_loyalty_points_bonus(),
                'total_loyalty_points_price': item.cart.total_loyalty_points_price(),
                'loyalty_points': calculate_loyalty_points_balance(request.user, item.cart),
                'cart_count': len(get_cart_items_if_any(request))
            }

            return HttpResponse(json.dumps(data), content_type='application/json')

        else:
            return redirect('cart')
    else:
        raise Http404("Cart item not found.")
