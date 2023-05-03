from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem

# Create your views here.
class DetailCart(DetailView):
    model = Cart
    template_name='detail_cart.html'