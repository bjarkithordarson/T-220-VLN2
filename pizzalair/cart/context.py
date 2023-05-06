from .models import Cart, CartItem

def cart(request):
    return {
        'cart_num_items': Cart
    }
