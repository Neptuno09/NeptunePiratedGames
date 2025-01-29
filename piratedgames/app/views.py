from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, RegisterForm
from .forms import JuegoForm

def inicio(request):
     return render(request, 'inicio.html')

def juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos.html', {'juegos': juegos})

def adminselector(request):
    return render(request, 'adminselector.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio')  # Cambia 'home' por la vista que desees
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:  
                return redirect('adminselector')  # Redirige al panel de administración
            else:
                return redirect('inicio')  # Redirige a otra vista para usuarios comunes
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def addgames(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a donde quieras
    else:
        form = JuegoForm()
    return render(request, 'addgames.html', {'form': form})

def gamepage(request, slug):
    juego = get_object_or_404(Juego, slug=slug)  # Obtiene el juego por su slug
    return render(request, 'gamepage.html', {'juego': juego})

def account(request):
    return render(request, 'account.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')