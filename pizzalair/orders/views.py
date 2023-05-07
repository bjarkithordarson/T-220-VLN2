from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cart.helpers import *
from cart.models import CartItem, Cart
from .models import Order
from .forms import BillingForm, CardPaymentForm, PaymentMethodForm


# Create your views here.
@login_required
def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders
    }
    return render(request, 'index.html', context)

@login_required
def checkout(request):
    # Redirect to index if no items in cart
    items = get_cart_items_if_any(request)
    if not len(items):
        return redirect('index')

    # Check if there's an order with this cart
    cart_id = request.session.get('cart')

    try:
        order = Order.objects.get(cart=cart_id, user=request.user)
    except:
        order = Order()
        order.cart = Cart.objects.get(id=cart_id)
        order.user = request.user
        order.save()

    return redirect('billing', order_id=order.id)

@login_required
def order(request, order_id):
    return render(request, 'order.html')

@login_required
def payment_method(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    template = 'payment_method.html'

    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(id=order_id)
            order.payment_method = form.cleaned_data['payment_method']
            order.save()
            if order.payment_method.method == 'card':
                return redirect('payment_card', order_id=order_id)
            else:
                return redirect('review', order_id=order_id)
    else:
        form = PaymentMethodForm(instance=order)

    context = {
        'order_id': order_id,
        'form': form
    }

    return render(request, template, context)



@login_required
def payment_card(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    if request.method == 'POST':
        form = CardPaymentForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(id=order_id)
            order.payment_card_name = form.cleaned_data['payment_card_name']
            order.payment_card_number = form.cleaned_data['payment_card_number']
            order.payment_expiry_month = form.cleaned_data['payment_expiry_month']
            order.payment_expiry_year = form.cleaned_data['payment_expiry_year']
            order.payment_cvc = form.cleaned_data['payment_cvc']
            order.save()
            return redirect('review', order_id=order_id)
    else:
        form = CardPaymentForm(instance=order)

    context = {
        'form': form,
        'order_id': order_id
    }
    return render(request, 'payment_card.html', context)

@login_required
def billing(request, order_id):
    # Redirect to /orders if order doesn't exist
    try:
        order = Order.objects.get(id=order_id)
    except:
        return redirect('checkout')

    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(id=order_id)
            order.billing_name = form.cleaned_data['billing_name']
            order.billing_address = form.cleaned_data['billing_address']
            order.billing_city = form.cleaned_data['billing_city']
            order.billing_postal_code = form.cleaned_data['billing_postal_code']
            order.billing_country = form.cleaned_data['billing_country']
            order.save()
            return redirect('payment_method', order_id=order_id)
    else:
        form = BillingForm(instance=order)

    context = {
        'form': form,
        'order_id': order_id
    }
    return render(request, 'billing.html', context)

@login_required
def review(request, order_id):
    # Redirect to checkout if order doesn't exist
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    return render(request, 'review.html')

@login_required
def confirmation(request, order_id):
    return render(request, 'confirmation.html')
