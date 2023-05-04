from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.product_details, name="product_details"),
    path("<int:product_id>/popup", views.product_details, name="product_details_popup")
]
