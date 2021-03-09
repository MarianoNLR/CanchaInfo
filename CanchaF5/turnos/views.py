from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Turno, Cancha
from .forms import ReservaForm
from users import urls, views
from users.views import homeUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def reservar(request):
    a = None
    b = None
    c = None
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
                    messages.info(request, "El turno ya existe")
                    context = {'form': form}
                    return render(request, 'accounts/registrados/reservas.html', context)
            else:
                form.save()
                messages.success(request, 'Reserva creada con exito')
            return redirect('user_home')
    else:
        context = {'form': form}
        return render(request, 'accounts/registrados/reservas.html', context) 

    
                
