from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from products.models import Product

# Create your views here.
def index(request):
    template = loader.get_template("category.html")
    products = Product.objects.all()

    context = {
        "page_title": "Menu",
        "products": products
    }
    return HttpResponse(template.render(context, request))

def product_details(request, product_id):
    template = loader.get_template("details.html")
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product
    }
    return HttpResponse(template.render(context, request))
