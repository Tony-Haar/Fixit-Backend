from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    class UserType(models.TextChoices):
        USER = 'User', _('User')
        PROFESSIONAL = 'Professional', _('Professional')
        COMPANY = 'Company', _('Company')
        ADMIN = 'Admin', _('Admin')

    email = models.EmailField(_('email address'), unique=True)
    usertype = models.CharField(max_length = 12, choices = UserType.choices, default = UserType.USER)
    location = models.CharField(max_length = 100, blank = True)

    USERNAME_FIELD = 'email' # this field tells django which field should be used as the unique identifier for the user.
    REQUIRED_FIELDS = ['username'] # is a list of field names that will be required when creating a superuser with the createsuperuser command

    objects = CustomUserManager()

    def __str__(self):
        return self.email
        