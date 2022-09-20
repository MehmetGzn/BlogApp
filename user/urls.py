from django.urls import path
from user.views import home, register, profile
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", profile, name="profile"),
]