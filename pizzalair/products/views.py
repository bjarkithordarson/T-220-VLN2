
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from products.models import Product
from products.models import ProductCategory
from products.models import OfferTemplate

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
    offer_template = get_object_or_404(OfferTemplate, offer_id=product_id)
    qnt = range(offer_template.quantity)
    all_pizza = Product.objects.filter(category=offer_template.category)


    context = {
        "product": product,
        "offer_qnt": qnt,
        "all_pizza": all_pizza
    }
    return HttpResponse(template.render(context, request))

def category(request, slug):

    template = loader.get_template("category.html")
    print("hello")
    categories = get_object_or_404(ProductCategory, slug=slug)
    #categories = ProductCategory.objects.get(id = category_id)
    productcategory = ProductCategory.objects.filter(filter=True)
    products = Product.objects.filter(category = categories)

    if 'search_filter' in request.GET:
        search_filter = request.GET["search_filter"]
        assert isinstance(Product.objects.filter(name__icontains=search_filter).values, object)
        pizzas = list(Product.objects.filter(name__icontains=search_filter).values())
        return JsonResponse({'data': pizzas})

    context = {
        "productcategory": productcategory,
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