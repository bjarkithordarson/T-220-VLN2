
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from products.models import Product
from products.models import ProductCategory
from products.models import OfferTemplate, Offer
from products.models import Pizza

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
def product_list(request):
    return base_list(request, Product, "base_list.html", "Our Products")

def pizza_list(request):
    return base_list(request, Pizza, "pizza/list.html", "Pizzas")

def offer_list(request):
    return base_list(request, Offer, "offer/list.html", "Offers")

def merch_list(request):
    return base_list(request, Product, "merch/list.html", "Merch")

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
    is_popup = request.GET.get('popup', False)

    if is_popup:
        template = loader.get_template("product/details_ajax.html")
    else:
        template = loader.get_template("product/details.html")

    product = get_object_or_404(Product, pk=offer_id)
    offer_template = OfferTemplate.objects.filter(offer_id=offer_id)

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
    template = loader.get_template("category.html")
    products, context = apply_filters(request, products)
    pizza = Pizza.objects.all()

    context = dict({
        "pizza": pizza,
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

def offer(request, slug):
    template = loader.get_template("category.html")
    categories = get_object_or_404(ProductCategory, slug=slug)
    products = Product.objects.filter(category=categories)
    offer_template = OfferTemplate.objects.all()

    context = {
        "page_title": "Menu",
        "products": products,
        "offer_template": offer_template
    }
    return HttpResponse(template.render(context, request))
