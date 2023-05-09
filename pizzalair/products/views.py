
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from products.models import Product
from products.models import ProductCategory
from products.models import Pizza

# Create your views here.
def index(request):
    template = loader.get_template("category.html")
    products = Product.objects.all().order_by('name')
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
    pizzas = Pizza.objects.all().order_by('name')

    context = {
        "pizzas" : pizzas,
        "product": product
    }
    return HttpResponse(template.render(context, request))

def category(request, slug):

    categories = get_object_or_404(ProductCategory, slug=slug)
    productcategory = ProductCategory.objects.filter(filter=True)
    products = Product.objects.filter(category = categories).order_by('name')
    template = loader.get_template("category.html")
    products, context = apply_filters(request, products)
    pizzas = Pizza.objects.all().order_by('name')


    context = dict({
        "pizzas": pizzas,
        "productcategory": productcategory,
        "page_title": "Menu",
        "products": products
    }, **context)

    return HttpResponse(template.render(context, request))

def apply_filters(request, product_list, context = {}):
    product_list = product_list.order_by('name')

    category = request.GET.get('category', "")
    if category:
        product_list = ProductCategory.objects.get(slug = category).products.all()

    search_filter = request.GET.get('search_filter', "")
    if search_filter:
        product_list = product_list.filter(name__icontains=search_filter)

    order_by = request.GET.get('order_by', "")
    if order_by:
        if order_by == 'price':
              product_list = product_list.order_by('price')


    direction = request.GET.get('direction', "")
    if direction:
        if direction == 'desc':
            product_list = product_list.reverse()

    if context is None:
        context = {}
    context["filter"] = {
        "category": category,
        "search_filter": search_filter,
        "order_by": order_by,
        "direction": direction
    }

    return (product_list, context)




def search(request):

    template = loader.get_template("search.html")

    products = Product.objects.all().order_by('name')
    ajax = request.GET.get('ajax', False)
    products = apply_filters(request, products)

    if ajax:
        template = loader.get_template("search_ajax.html")

    context = {
        "page_title": "Menu",
        "products": products
    }
    return HttpResponse(template.render(context, request))
