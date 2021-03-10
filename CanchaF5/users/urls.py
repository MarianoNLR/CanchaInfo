from django.contrib import admin
from django.urls import path,include
from .views import UsuariosViews

urlpatterns = [
    path('register/', UsuariosViews.registerPage, name="Registro"),
    path('Home/', UsuariosViews.home, name="home"),
    path('Login/', UsuariosViews.loginPage, name="Login"),
    path('Logout/',UsuariosViews.logoutUser, name="Logout"),
    path('Home_user/', UsuariosViews.homeUser, name="user_home"),
    path('Reservas/', UsuariosViews.reservar, name="reservar"),
    #path('Perfil/', views.perfil, name="perfil_user"),
    path('editar_user/<int:user_id>', UsuariosViews.edit_user, name="editar_user"),
    path('actualizar_user/<int:user_id>', UsuariosViews.actualizar_user, name="actualizar_user"),
]