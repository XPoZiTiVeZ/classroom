from django.urls import path
from account.views import register, login, profile, set_password

urlpatterns = [
    path("", profile, name="profile"),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("set_password", set_password, name="set_password"),
]