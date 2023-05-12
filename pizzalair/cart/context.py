from .helpers import get_cart_items_if_any

def cart(request):
    return {
        'cart_num_items': len(get_cart_items_if_any(request))
    }
