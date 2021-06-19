from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=225, required=True)
    password = forms.CharField(
        max_length=225, widget=forms.PasswordInput, required=True
    )
