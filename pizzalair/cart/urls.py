from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart_detail, name='cart'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:id>/', views.cart_remove, name='cart_remove'),
    #path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    #path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    #path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    #path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    #path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
