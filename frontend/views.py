from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
import requests
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import View
from .forms import *
from django.contrib import messages


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
                f"http://localhost:8000/api/user/login", data=form.cleaned_data
            ).json()
            if response["detail"] == "Login Successfull":
                messages.success(request, "Login Successfull")
                request.session["token"] = response["token"]
                return redirect("home")
        else:
            print(form.errors)

        return render(request, "login.html", {"form": form})


class RegisterView(FormView):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            response = requests.post(
                "http://localhost:8000/api/user/register", data=form.cleaned_data
            ).json()
            if response["detail"] == "Registration successfull":
                messages.success(request, "Registration Successfull")
                request.session["token"] = response["token"]
                return redirect("home")
        else:
            print(form.errors)
        return render(request, "register.html", {"form": form})
