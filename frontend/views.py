from django.shortcuts import render
from django.urls import reverse_lazy, reverse
import requests
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import View
from .forms import *

# Create your views here.


class Home(View):
    def get(self, request):
        context = {}
        return render(request, "home.html", context)


class LoginView(FormView):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            response = requests.post(
                f"/api/user/login", params=form.cleaned_data
            ).json()
            print(response)

        else:
            print(form.errors)

        return render(request, "login.html", {"form": form})


# class RegisterView(FormView):
