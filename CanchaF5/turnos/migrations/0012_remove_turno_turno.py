# Generated by Django 3.1.7 on 2021-03-03 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0011_auto_20210303_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='turno',
        ),
    ]