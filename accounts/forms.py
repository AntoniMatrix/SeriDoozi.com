"""
Account-related forms.
"""
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    """Register form extending UserCreationForm."""
    email = forms.EmailField(required=True, label="ایمیل", widget=forms.TextInput(attrs={ "placeholder": "example@email.com" }))
    phone = forms.CharField(required=True, label="شماره موبایل", widget=forms.TextInput(attrs={ "placeholder": "09xx xxx xxxx" }))
    first_name = forms.CharField(required=True , label="نام", widget=forms.TextInput(attrs={ "placeholder": "مثلا: علی" }))
    last_name = forms.CharField(required=True , label="نام خانوادگی", widget=forms.TextInput(attrs={ "placeholder": "مثلا: هاشمی" }))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",  "phone", "password1", "password2")

        def clean_phone(self):
            phone = self.cleaned_data["phone"]

            if not re.fullmatch(r"09\d{9}", phone):
                raise forms.ValidationError(
                    "شماره موبایل باید با 09 شروع شده و 11 رقم باشد."
                )

            return phone