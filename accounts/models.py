"""
Custom user model.

We use AbstractUser and manage roles via Django Groups + Permissions.
"""

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

iran_phone_validator = RegexValidator(
    regex=r"^09\d{9}$",
    message="شماره موبایل باید با 09 شروع شده و 11 رقم باشد."
)

class User(AbstractUser):
    """Custom User with optional phone field."""
    phone = models.CharField(max_length=20, blank=True, unique=True, validators=[iran_phone_validator],)