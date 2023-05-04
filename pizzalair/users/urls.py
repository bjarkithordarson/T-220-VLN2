from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.register, name='signup'),
    path('signin', LoginView.as_view(template_name='login.html'), name='signin'),
    path('signout', LogoutView.as_view(next_page='signin'), name='signout')
]
