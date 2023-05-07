from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
def order(request):
    return render(request, 'order.html')

@login_required
def payment(request):
    return render(request, 'payment.html')

@login_required
def billing(request):
    return render(request, 'billing.html')

@login_required
def review(request):
    return render(request, 'review.html')

@login_required
def confirmation(request):
    return render(request, 'confirmation.html')
