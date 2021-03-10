from django.contrib import admin
from django.urls import path,include
from .views import FormularioTurnosView

urlpatterns = [
    path('reservas/', FormularioTurnosView.reservar, name='reservas_turno'),
    path('Perfil/', FormularioTurnosView.lista_turnos, name='lista_turnos'),
    #path('MisTurnos/', FormularioTurnosView.eliminar, name="eliminar"),
    path('EliminarTurno/<int:turno_id>/', FormularioTurnosView.eliminar_turno, name="eliminar"),
    path('Editar_turno/<int:turno_id>/', FormularioTurnosView.edit_turno, name="editar_turno"),
    path('Actualizar_turno/<int:turno_id>/', FormularioTurnosView.actualizar_turno, name="actualizar_turno"),
]