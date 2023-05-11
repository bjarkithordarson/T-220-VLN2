
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .forms import OfferInstanceForm
from .models import Product
from .models import ProductCategory
from .models import OfferTemplate, Offer
from .models import Pizza


def base_list(request, model, template, title):
    products = model.objects.all().order_by('name')
    category = get_object_or_404(ProductCategory, name=title)
    products = products.filter(category=category)
    products, context = apply_filters(request, products)
    categories = ProductCategory.objects.all()
    categories = categories.filter(filter=True)

    #check if the title is "Our Products" and make the title based on the product category

    context = dict({
        "categories": categories,
        "page_title": title,
        "products": products,
    }, **context)
    return render(request, template, context)

def base_no_nav(request, model, template, title):
    products = model.objects.all().order_by('name')
    category = get_object_or_404(ProductCategory, name=title)
    products = products.filter(category=category)
    products, context = apply_filters(request, products)

    context = dict({
        "page_title": title,
        "products": products,
    }, **context)

    return render(request, template, context)

def product_list(request, slug):
# I want to imitate base_list but I want to use the slug instead of the title
    products = Product.objects.all().order_by('name')
    category = get_object_or_404(ProductCategory, slug=slug)
    products = products.filter(category=category)
    products, context = apply_filters(request, products)
    categories = ProductCategory.objects.all()
    categories = categories.filter(filter=True)

    context = dict({
        "categories": categories,
        "page_title": category.name,
            "products": products,
        }, **context)
    return render(request, "product/list.html", context)

def pizza_list(request):
    print("YOU ARE IN PIZZA LIST")
    return base_list(request, Pizza, "pizza/list.html", "Pizza")

def offer_list(request):
    print("YOU ARE IN OFFER LIST")
    return base_list(request, Offer, "offer/list.html", "Offers")

def merch_list(request):
    print("YOU ARE IN MERCH LIST")
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
    template = "pizza/details.html" if not ajax else "pizza/details_ajax.html"
    return base_details(request, Pizza, template, pizza_id)

def offer_details(request, offer_id):
    if request.method == "POST":
        form = OfferInstanceForm(offer_id, request.POST)
        ajax= request.POST.get('ajax', False) != False
        if form.is_valid():
            instance = form.save()
            return redirect('cart_add_offer', offer_instance_id=instance.id, quantity=1)

    ajax = request.GET.get('ajax', False)

    form = OfferInstanceForm(offer_id)

    if ajax:
        template = loader.get_template("offer/details_ajax.html")
    else:
        template = loader.get_template("offer/details.html")

    product = get_object_or_404(Product, pk=offer_id)
    offer_template = OfferTemplate.objects.filter(offer_id=offer_id)

    for x in offer_template:
        print(x.products())

    context = {
        "form": form,
        "product": product,
        "offer_template": offer_template
    }
    return HttpResponse(template.render(context, request))

def merch_details(request, merch_id):
    ajax = request.GET.get("ajax", False) != False
    template = "merch/details.html" if not ajax else "merch/details_ajax.html"
    return base_details(request, Product, template, merch_id)

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

def offer_create(request):
    if request.method == "POST":
        # Print all post data to the server console
        print(request.POST)

        offer_instance_id = 1
        quantity = request.POST.get("quantity", 1)

        # Return json response
        return JsonResponse({
            "success": True,
            "message": "Offer created successfully"
        })

        # Add offer to cart
        return redirect("/cart/add_offer/" + str(offer_instance_id) + "/" + str(quantity))

    else:
        return redirect("/")

