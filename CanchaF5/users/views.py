from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
# Create your views here.



def home(request):
    return render(request, 'accounts/home.html') 


def homeUser(request):
    return render(request, 'accounts/registrados/user_home.html')

@login_required
def reservar(request):
    return render(request, 'accounts/registrados/reservas.html')


def perfil(request):
    return render(request, 'accounts/registrados/perfil.html')


def registerPage(request):
    form =  CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' Creaste la cuenta con exito')
            return redirect('Login')
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

