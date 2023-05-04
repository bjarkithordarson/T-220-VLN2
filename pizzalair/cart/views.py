from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.template import loader

# Create your views here.




def index(request):
    template = loader.get_template("cart.html")
    cart = Cart.objects.all()

    context = {
        "page_title": "Menu",
        "products": cart
    }

    return HttpResponse(template.render(context, request))



def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart':cart})

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




