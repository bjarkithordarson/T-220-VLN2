from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:order_id>/', views.order, name='order'),
    path('<int:order_id>/payment/', views.payment, name='payment'),
    path('<int:order_id>/billing/', views.billing, name='billing'),
    path('<int:order_id>/review/', views.review, name='review'),
    path('<int:order_id>/confirmation/', views.confirmation, name='confirmation')
]
