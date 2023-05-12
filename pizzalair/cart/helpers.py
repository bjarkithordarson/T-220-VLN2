from .models import Cart, CartItem, CartProductItem, CartOfferItem
from django.db.models import Sum
from itertools import chain

def get_or_create_cart(request):
    try:
        cart_id = request.session.get('cart')
        cart = Cart.objects.get(id=cart_id)
    except:
        cart = Cart()
        cart.save()
        request.session['cart'] = cart.id
    return cart

def get_cart_items_if_any(request):
    try:
        cart_id = request.session.get('cart')
        cart = Cart.objects.get(id=cart_id)
        products = CartProductItem.objects.filter(cart=cart)
        offers = CartOfferItem.objects.filter(cart=cart)
        return list(chain(products, offers))
    except:
        return []

def get_cart_total(request):
    items = get_cart_items_if_any(request)
    if len(items):
        print(items)
        return sum([item.total_price() for item in items])
    else:
        return 0

def calculate_loyalty_points_balance(user, cart):
    return {
        "old_balance": user.loyalty_points,
        "earned": cart.total_loyalty_points_bonus(),
        "spent": cart.total_loyalty_points_price(),
        "new_balance": user.loyalty_points + cart.total_loyalty_points_bonus() - cart.total_loyalty_points_price()
    }
