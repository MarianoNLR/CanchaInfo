from django.shortcuts import render, redirect
from datetime import date
from django.http import HttpRequest
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .models import Turno, Cancha
from .models import Usuario
from users.forms import CustomUserChangeForm
from .forms import ReservaForm
from users import urls, views
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.
class FormularioTurnosView(HttpRequest):
    def reservar(request):
        form = ReservaForm()
        if request.method == 'POST':
            form = ReservaForm(request.POST)
            if form.is_valid():
                fecha = request.POST.get('dia')
                hora = request.POST.get('hora')
                cancha = request.POST.get('cancha')
                turnos = Turno.objects.all()
                for i in turnos:
                    if (i.get_hora() == hora) and (form.cleaned_data.get('cancha') == i.get_cancha()) and (form.cleaned_data.get('dia') == i.get_dia()):
                        context = {'form': form}
                        messages.info(request, "El turno ya existe")
                        return render(request, 'accounts/registrados/reservas.html', context)
                else:
                    solicitante = form.save(commit=False)
                    solicitante.persona_id = request.user.id 
                    solicitante.save()
                    messages.success(request, 'Reserva creada con exito')
                return redirect('lista_turnos')
        else:
            context = {'form': form}
            return render(request, 'accounts/registrados/reservas.html', context) 

    def lista_turnos(request):
        actual_user = request.user.id
        hoy = date.today()
        data = {
            'turnos': Turno.objects.filter(persona_id=request.user.id, dia__gt=hoy).order_by('-dia'),
        }
        return render(request, 'accounts/registrados/perfil.html', data)
    

    def edit_turno(request, turno_id):
        turno = Turno.objects.filter(id=turno_id).first()
        form = ReservaForm(instance=turno)
        return render(request, "accounts/registrados/editar_turno.html", {"form":form, "turno": turno})

    def actualizar_turno(request, turno_id):
        turno = Turno.objects.get(pk=turno_id)
        form = ReservaForm(request.POST, instance=turno)
        if form.is_valid():
            fecha = request.POST.get('dia')
            hora = request.POST.get('hora')
            cancha = request.POST.get('cancha')
            turnos = Turno.objects.all()
            for i in turnos:
                a = i.get_hora()
                b = i.get_cancha()
                c = i.get_dia()
                if (i.get_hora() == hora) and (form.cleaned_data.get('cancha') == i.get_cancha()) and (form.cleaned_data.get('dia') == i.get_dia()):
                    messages.error(request, "El turno ya existe")
                    return render(request, 'accounts/registrados/editar_turno.html', {"form":form,"turno":turno})
            else:
                form.save()
                messages.success(request, "Turno actualizado con exito!")
            return redirect('lista_turnos')
        return render(request, 'accounts/registrados/editar_turno.html', {"form":form,"turno":turno})
        

    def eliminar_turno(request, turno_id):
        try:
            turno = Turno.objects.filter(pk=turno_id)
        except Turno.DoesNotExist:
            messages.error(request, "Ha ocurrido un error")
            return redirect("lista_turnos")
        turno.delete()
        turnos = Turno.objects.filter(persona_id=request.user.id).order_by('-dia')
        messages.success(request, "El turno ha sido eliminado")
        return redirect("lista_turnos")
    
    def edit_user(request, user_id):
        usuario = Usuario.objects.filter(id=user_id).first()
        form = CustomUserChangeForm(instance=usuario)
        return render(request, "accounts/registrados/editar_user.html", {"form":form, "usuario":usuario})

    def actualizar_user(request, user_id):
        usuario = Usuario.objects.get(pk=user_id)
        form = CustomUserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.info(request, "Datos actualizados con exito!")
            return redirect('lista_turnos')
        else:
            messages.error(request, "Ha ocurrido un error, intente nuevamente")
            return render(request, "accounts/registrados/editar_user.html", {"form":form, "usuario":usuario})
        return render(request, "accounts/registrados/editar_user.html", {"form":form, "usuario":usuario})
        