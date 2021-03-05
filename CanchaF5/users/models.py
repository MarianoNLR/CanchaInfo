from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Usuario", unique=True, max_length=50)
    first_name = models.CharField("Nombres", max_length=200)
    surname = models.CharField("Apellidos", max_length=200)
    dni = models.CharField("Dni", unique=True, max_length=8)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' ,'dni', 'first_name' , 'surname']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name}, {self.surname}'

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('username', 'first_name','surname','email','dni',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'first_name','surname', 'email','dni',)
