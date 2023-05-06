from .models import Cart, CartItem

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
        return CartItem.objects.filter(cart=cart)
    except:
        return None

def get_cart_total(request):
    items = get_cart_items_if_any(request)
    if items != None:
        print(items)
        return items.aggregate(s=Sum("total_price"))['s']
    else:
        return 0
