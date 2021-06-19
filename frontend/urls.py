from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
]
