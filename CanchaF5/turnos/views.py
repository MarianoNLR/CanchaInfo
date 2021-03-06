from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Turno, Cancha, CanchaLibre
from .forms import ReservaForm
from users import urls, views
from users.views import homeUser
from django.contrib import messages

# Create your views here.

class ReservaCreateView(CreateView):
    model = Turno
    form_class = ReservaForm
    template_name = 'accounts/registrados/reservas.html'
    if Turno == CanchaLibre:
       return render(request, 'accounts/registrados/reservas.html')
    else:
        success_url = reverse_lazy(homeUser)
    



