from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('signin/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='signin'),
    path('signout/', LogoutView.as_view(next_page='signin'), name='signout'),
    path('profile/', views.profile, name='profile')
]
