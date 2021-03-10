from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from turnos import urls
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import CustomUserChangeForm
from django.contrib import messages

# Create your views here.


class UsuariosViews(HttpRequest):
    
    def home(request):
        return render(request, 'accounts/home.html') 


    def homeUser(request):
        return render(request, 'accounts/registrados/user_home.html')

    @login_required
    def reservar(request):
        return render(request, 'accounts/registrados/reservas.html')


    def perfil(request):
        return render(request, 'accounts/registrados/perfil.html', {"mensaje": 'OK'})


    def registerPage(request):
        form =  CustomUserCreationForm()

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' Creaste la cuenta con exito')
                return redirect('Login')
            else:
                for msg in form.error_messages:
                    messages.error(request, f"form.error_messages[msg]")
        context = {'form':form}
        return render(request, 'accounts/register.html', context)


    def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_home')
            else:
                messages.info(request, "Username or password is incorrect")
        context = {}
        return render(request, 'accounts/login.html', context)

    def logoutUser(request):
        logout(request)
        return redirect('Login')

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
