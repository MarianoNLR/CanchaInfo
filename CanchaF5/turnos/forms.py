from django.forms import ModelForm
from .models import Turno
from .models import Cancha
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaForm(ModelForm):
    class Meta:
        model = Turno
        fields = ('cancha', 'dia', 'hora', 'dni')
        widgets = {'dia':DateInput}




