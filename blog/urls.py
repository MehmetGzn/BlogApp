from django.urls import path
from blog.views import home, register, login
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
]