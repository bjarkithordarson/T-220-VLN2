
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from products.models import Product
from products.models import ProductCategory

# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET["search_filter"]

        assert isinstance(Product.objects.filter(name__icontains=search_filter).values, object)
        pizzas = list(Product.objects.filter(name__icontains=search_filter).values())
        return JsonResponse({'data': pizzas})
    template = loader.get_template("category.html")
    products = Product.objects.all().order_by('name')
    productcategory = ProductCategory.objects.filter(filter=True)
    context = {
        "productcategory": productcategory,
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
    categories = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category = categories)

    context = {
        "page_title": "Menu",
        "products": products
    }
    return HttpResponse(template.render(context, request))

