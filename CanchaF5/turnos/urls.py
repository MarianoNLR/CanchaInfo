from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('reservas/', views.ReservaCreateView.as_view(), name='reservas_turno'),
]