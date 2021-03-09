from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="Registro"),
    path('Home/', views.home, name="home"),
    path('Login/', views.loginPage, name="Login"),
    path('Logout/',views.logoutUser, name="Logout"),

    path('Home_user/', views.homeUser, name="user_home"),
    path('Reservas/', views.reservar, name="reservar"),
    #path('Perfil/', views.perfil, name="perfil_user"),
]