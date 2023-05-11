from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="index"),
    path("<int:product_id>/", views.product_details, name="product_details"),
    path("pizzas/", views.pizza_list, name="pizza_list"),
    path("offers/", views.offer_list, name="offer_list"),
    path("merch/", views.merch_list, name="merch_list"),
    path("<slug:slug>/", views.product_list, name="product_list"),
    path("pizzas/<int:pizza_id>/", views.pizza_details, name="pizza_details"),
    path("offers/<int:offer_id>/", views.offer_details, name="offer_details"),
    path("offers/create", views.offer_create, name="offer_create"),
    path("merch/<int:merch_id>/", views.merch_details, name="merch_details"),
    path("<int:product_id>/popup", views.product_details, name="product_details_popup")
]
