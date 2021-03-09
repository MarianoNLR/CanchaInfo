from django.forms import ModelForm
from .models import Turno
from .models import Cancha
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(ModelForm):
    class Meta:
        model = Turno
        fields = ('cancha', 'dia', 'hora')

        labels = {
            'cancha': 'Nro. Cancha',
            'dia': 'Fecha',
            'hora': 'Horario',
            #'persona': 'Persona',
        }
        widgets = {
            'cancha': forms.Select(attrs={'class': 'form-control'}),
            'dia':DateInput(attrs={'class': 'form-control'}),
            'hora':forms.Select(attrs={'class': 'form-control'}),
            #'persona': forms.Select(attrs={'class': 'form-control'}),
            }





