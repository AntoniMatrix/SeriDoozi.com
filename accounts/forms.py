"""
Account-related forms.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    """Register form extending UserCreationForm."""
    email = forms.EmailField(required=True, label="ایمیل")
    phone = forms.CharField(required=True, label="شماره موبایل")
    first_name = forms.CharField(required=True , label="نام")
    last_name = forms.CharField(required=True , label="نام خانوادگی")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",  "phone", "password1", "password2")