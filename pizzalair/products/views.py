from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from products.models import Product, ProductCategory


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
    is_popup = request.GET.get('popup', False)

    if is_popup:
        template = loader.get_template("details_popup.html")
    else:
        template = loader.get_template("details.html")

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product
    }
    return HttpResponse(template.render(context, request))


def category(request, category_id):
    template = loader.get_template("category.html")
    print("hello")
    categories = ProductCategory.objects.get(id = category_id)
    products = Product.objects.filter(category = categories)

    context = {
        "page_title": "Menu",
        "products": products
    }
    return HttpResponse(template.render(context, request))