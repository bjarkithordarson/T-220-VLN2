
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Product
from .models import ProductCategory
from .models import OfferTemplate, Offer
from .models import Pizza


# Create your views here.

def base_list(request, model, template, title):

    products = model.objects.all().order_by('name')
    products, context = apply_filters(request, products)
    context = dict({
        "page_title": title,
        "products": products,
        "categories": ProductCategory.objects.filter(filter=True).order_by('name')
    }, **context)
    return render(request, template, context)

def base_no_nav(request, model, template, title):

    products = model.objecst.all().order_by('name')
    products, context = apply_filters(request, products)
    context = {
        "page_title": title,
        "products": products
    }
    return render(request, template, context)

def product_list(request):
    return base_list(request, Product, "base_list.html", "Our Products")

def pizza_list(request):
    print("YOU ARE IN PIZZA LIST")
    return base_list(request, Pizza, "pizza/list.html", "Pizzas")

def offer_list(request):
    return base_list(request, Offer, "offer/list.html", "Offers")

def merch_list(request):
    return base_no_nav(request, Product, "merch/list.html", "Merch")

def base_details(request, model, template, id):
    product = get_object_or_404(model, pk=id)

    context = {
        "product": product
    }
    return render(request, template, context)

def product_details(request, product_id):
    ajax = request.GET.get("ajax", False) != False
    template = "product/details.html" if not ajax else "product/details_ajax.html"
    return base_details(request, Product, template, product_id)

def pizza_details(request, pizza_id):
    ajax = request.GET.get("ajax", False) != False
    template = "product/details.html" if not ajax else "product/details_ajax.html"
    return base_details(request, Product, template, pizza_id)

def offer_details(request, offer_id):

    ajax = request.GET.get('ajax', False)

    if ajax:
        template = loader.get_template("offer/details_ajax.html")
    else:
        template = loader.get_template("offer/details.html")

    product = get_object_or_404(Product, pk=offer_id)
    offer_template = OfferTemplate.objects.filter(offer_id=offer_id)

    for x in offer_template:
        print(x.products())
    print("AAAAAAAAAAAA")

    context = {

        "product": product,
        "offer_template": offer_template
    }
    return HttpResponse(template.render(context, request))

def merch_details(request, merch_id):
    pass

def category(request, slug):

    categories = get_object_or_404(ProductCategory, slug=slug)
    productcategory = ProductCategory.objects.filter(filter=True)
    products = Product.objects.filter(category = categories).order_by('name')
    template = loader.get_template("product/list.html")
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
        product_list = product_list.filter(category__slug=category)

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

def offer(request, slug):
    template = loader.get_template("base_list.html")
    categories = get_object_or_404(ProductCategory, slug=slug)
    products = Product.objects.filter(category=categories)
    offer_template = OfferTemplate.objects.all()

    context = {
        "page_title": "Menu",
        "products": products,
        "offer_template": offer_template
    }
    return HttpResponse(template.render(context, request))
