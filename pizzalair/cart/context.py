from .helpers import get_cart_items_if_any

def cart(request):
    items = get_cart_items_if_any(request)
    print(items)
    print("World")
    return {
        'cart_num_items': len(items)
    }
