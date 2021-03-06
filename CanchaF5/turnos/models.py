from django.db import models
from users.models import Usuario

HORARIOS = (
    ('5PM - 6PM', '5PM - 6PM'),
    ('6PM - 7PM', '6PM - 7PM'),
    ('7PM - 8PM', '7PM - 8PM'),
    ('8PM - 9PM', '8PM - 9PM'),
    ('9PM - 10PM', '9PM - 10PM'),
    ('10PM - 11PM', '10PM - 11PM'),
    ('11PM - 00AM', '11PM - 00AM'),
)


class Cancha(models.Model):
    num_cancha = models.IntegerField(blank=False, null=False, unique=True)

    def __str__(self):
        return f'Cancha {self.num_cancha}'

class Turno(models.Model):
    dia = models.DateField()
    hora = models.CharField(blank=False, null=False, max_length=20, choices=HORARIOS)
    dni = models.CharField(blank=False, null=False, max_length=10)
    cancha = models.ForeignKey(Cancha, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.persona.dni}: Turno para {self.dia}, en el horario de {self.hora} en {self.cancha}'


def CanchaLibre(request):
    turnos = Turno.objects.all()
    listaTurno = []
    listaTurno_Turno.append(self.dia)
    listaTurno_Turno.append(self.hora)
    listaTurno_Turno.append(self.cancha)


