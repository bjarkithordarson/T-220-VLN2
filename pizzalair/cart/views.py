from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from django.shortcuts import render, redirect
from products.models import Product


# Create your views here.

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")

"""def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")"""

"""def cart_clear(request):
    cart = CartItem(request)
    cart.clear()
    return redirect("cart")"""

def cart_detail(request):

    return render(request, 'cart.html')


def product_details(request, product_id):
    template = loader.get_template("details.html")
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product
    }
    return HttpResponse(template.render(context, request))
