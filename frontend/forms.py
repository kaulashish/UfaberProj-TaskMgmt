from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=225, required=True)
    password = forms.CharField(
        max_length=225, widget=forms.PasswordInput, required=True
    )


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name"]
