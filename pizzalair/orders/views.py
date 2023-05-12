from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from cart.helpers import *
from cart.models import CartItem, Cart
from .models import Order, OrderPaymentMethod, OrderStatus
from .forms import BillingForm, CardPaymentForm
from django.http import Http404

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
    """Checkout view"""
    # Redirect to index if no items in cart
    items = get_cart_items_if_any(request)
    if not len(items):
        return redirect('index')

    # Redirect to cart if not enough loyalty points
    cart = get_or_create_cart(request)
    balance = calculate_loyalty_points_balance(request.user, cart)

    if balance['new_balance'] < 0:
        return redirect(reverse('cart') + '?error=loyalty_points')

    if cart.items.filter(pay_with_loyalty_points=False).count() <= 0:
        return redirect(reverse('cart') + '?error=only_merch')

    # Check if there's an order with this cart
    cart_id = request.session.get('cart')

    order, _ = Order.objects.get_or_create(
        cart=Cart.objects.get(id=cart_id),
        user=request.user
    )

    if not order.is_user_editable():
        raise Http404("Order not found or already completed")

    return redirect('billing', order_id=order.id)

@login_required
def order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    context = {
        'order': order
    }
    return render(request, 'order.html', context)

@login_required
def payment_method(request, order_id):
    """Payment method view"""
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    if not order.is_user_editable():
        raise Http404("Order not found or already completed")

    template = 'payment_method.html'

    payment_methods = OrderPaymentMethod.objects.all()

    payment_method_id = request.GET.get('method', None)

    if payment_method_id:
        try:
            payment_method = OrderPaymentMethod.objects.get(id=payment_method_id)
            order.payment_method = payment_method
            order.save()
            if order.payment_method.method == 'card':
                return redirect('payment_card', order_id=order_id)
            else:
                return redirect('review', order_id=order_id)
        except:
            return redirect('payment_method', order_id=order_id)


    context = {
        'payment_methods': payment_methods,
        'order_id': order_id,
        'step': 2,
        'loyalty_points': calculate_loyalty_points_balance(request.user, order.cart)
    }

    return render(request, template, context)



@login_required
def payment_card(request, order_id):
    """Payment card view"""
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    if not order.is_user_editable():
        raise Http404("Order not found or already completed")

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
        'order_id': order_id,
        'step': 2
    }
    return render(request, 'payment_card.html', context)

@login_required
def billing(request, order_id):
    """Billing view"""
    # Redirect to /orders if order doesn't exist
    try:
        order = Order.objects.get(id=order_id)
    except:
        return redirect('checkout')

    if not order.is_user_editable():
        raise Http404("Order not found or already completed")

    return_url = request.GET.get('return', None)

    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(id=order_id)
            order.billing_name = form.cleaned_data['billing_name']
            order.billing_phone_number = form.cleaned_data['billing_phone_number']
            order.billing_address = form.cleaned_data['billing_address']
            order.billing_city = form.cleaned_data['billing_city']
            order.billing_postal_code = form.cleaned_data['billing_postal_code']
            order.billing_country = form.cleaned_data['billing_country']
            order.save()

            if return_url:
                return redirect(return_url)
            else:
                return redirect('payment_method', order_id=order_id)
    else:
        form = BillingForm(instance=order)

    context = {
        'form': form,
        'order_id': order_id,
        'step': 1
    }
    return render(request, 'billing.html', context)

@login_required
def review(request, order_id):
    """Review view"""
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    if not order.is_user_editable():
        raise Http404("Order not found or already completed.")

    errors = {
        'payment': order.validate_payment_info() == False,
        'billing': order.validate_billing_info() == False
    }

    is_complete = not errors['payment'] and not errors['billing']

    context = {
        'order_id': order_id,
        'order': order,
        'errors': errors,
        'is_complete': is_complete,
        'step': 3,
        'loyalty_points': calculate_loyalty_points_balance(request.user, order.cart)
    }

    return render(request, 'review.html', context)

@login_required
def confirmation(request, order_id):
    """Confirmation view"""

    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except:
        return redirect('checkout')

    if not order.validate_payment_info() or not order.validate_billing_info():
        return redirect('review', order_id=order_id)

    if order.status.type == OrderStatus.INITIAL:
        order.status = OrderStatus.objects.filter(type=OrderStatus.RECEIVED).first()

        user = order.user
        user.loyalty_points = calculate_loyalty_points_balance(order.user, order.cart)['new_balance']
        user.save()

        order.save()
        request.session['cart'] = None

    context = {
        'order_id': order_id,
        'order': order,
        'step': 4
    }

    return render(request, 'confirmation.html', context)
