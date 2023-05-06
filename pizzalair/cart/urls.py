from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:product_id>/<int:quantity>', views.add, name='cart_add'),
    path('remove/<int:cart_item_id>', views.remove, name='cart_remove'),
    path('update/<int:cart_item_id>/<int:quantity>', views.update, name='cart_update')
]
