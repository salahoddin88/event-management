from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(
        max_length=20, blank=True, null=True,
        default=None, unique=True
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """ Return user's full name """
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        """ Return string representation of our user"""
        return f'{self.get_full_name()}'
