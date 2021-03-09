from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('reservas/', views.reservar, name='reservas_turno'),
]