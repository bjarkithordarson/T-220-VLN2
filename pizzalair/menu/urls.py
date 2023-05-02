from django.urls import path
from . import views
urlpatterns = [
    path('registere', views.registere, name='registere')
]