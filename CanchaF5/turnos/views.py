from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Turno, Cancha
from .models import Usuario
from .forms import ReservaForm
from users import urls, views
from users.views import homeUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

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
            return redirect('user_home')
    else:
        context = {'form': form}
        return render(request, 'accounts/registrados/reservas.html', context) 

def lista_turnos(request):
    actual_user = request.user.id
    data = {
        'title': 'Lista de turnos',
        'turnos': Turno.objects.filter(persona_id=request.user.id).order_by('-dia'),
    }
    return render(request, 'accounts/registrados/perfil.html', data)
                
