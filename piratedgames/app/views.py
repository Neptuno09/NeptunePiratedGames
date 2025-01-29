from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from .forms import JuegoForm

def inicio(request):
     return render(request, 'inicio.html')

def juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos.html', {'juegos': juegos})

def adminselector(request):
    return render(request, 'adminselector.html')

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('adminselector')  # Cambia esto a la URL donde quieres redirigir tras el login
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

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