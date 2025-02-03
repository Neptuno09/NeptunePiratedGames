from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, RegisterForm, JuegoForm, UserEditForm
from django.contrib.auth.decorators import login_required
import django.contrib.messages as messages

# views.py
def inicio(request):
    # Verificar si el usuario está autenticado y obtener su color
    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        # Color predeterminado para usuarios no autenticados
        user_color = '#6E1F1B'  # Color predeterminado (rojo)
    
    darker_color = darken_color(user_color, 0.3)

    return render(request, 'inicio.html', {'color': user_color, 'darker_color': darker_color})


def juegos(request):
    juegos = Juego.objects.all()
    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'juegos.html', {'juegos': juegos, 'color': user_color, 'darker_color': darker_color})

def adminselector(request):
    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'adminselector.html', {'color': user_color, 'darker_color': darker_color})

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

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'register.html', {'form': form, 'color': user_color, 'darker_color': darker_color})

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('adminselector')
            else:
                return redirect('inicio')
    else:
        form = CustomLoginForm()

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'login.html', {'form': form, 'color': user_color, 'darker_color': darker_color})

def logout_view(request):
    logout(request)
    return redirect('login')

def addgames(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()

            if 'agregar_otro' in request.POST:
                return redirect('addgames')
            return redirect('inicio')
    else:
        form = JuegoForm()

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'addgames.html', {'form': form, 'color': user_color, 'darker_color': darker_color})

def gamepage(request, slug):
    juego = get_object_or_404(Juego, slug=slug)

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'gamepage.html', {'juego': juego, 'color': user_color, 'darker_color': darker_color})

def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account')  # Redirige tras guardar los cambios
    else:
        form = UserEditForm(instance=request.user)

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'account.html', {'form': form, 'color': user_color, 'darker_color': darker_color})

def users(request):
    users = CustomUser.objects.all()
    for user in users:
        user.darker_color = darken_color(user.color)

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'users.html', {'users': users, 'color': user_color, 'darker_color': darker_color})

def see_user(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.5)

    return render(request, 'user.html', {'user': user, 'color': user_color, 'darker_color': darker_color})

def gamelist(request):
    juegos = Juego.objects.all()

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'gamelist.html', {'juegos': juegos, 'color': user_color, 'darker_color': darker_color})

def editgame(request, slug):
    juego = get_object_or_404(Juego, slug=slug)

    if request.method == 'POST':
        if 'delete' in request.POST:
            juego.delete()
            messages.success(request, f"El juego '{juego.titulo}' ha sido eliminado exitosamente.")
            return redirect('gamelist')

        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, "El juego se ha actualizado correctamente.")
            return redirect('gamelist')
        else:
            messages.error(request, "Hubo un error al actualizar el juego.")
    else:
        form = JuegoForm(instance=juego)

    if request.user.is_authenticated:
        user_color = request.user.color
    else:
        user_color = '#FF0000'  # Color predeterminado

    darker_color = darken_color(user_color, 0.3)

    return render(request, 'editgame.html', {'form': form, 'juego': juego, 'color': user_color, 'darker_color': darker_color})

# Funciones para convertir colores y oscurecerlos

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def darken_color(hex_color, factor=0.2):
    r, g, b = hex_to_rgb(hex_color)
    r = max(int(r * (1 - factor)), 0)
    g = max(int(g * (1 - factor)), 0)
    b = max(int(b * (1 - factor)), 0)
    return rgb_to_hex(r, g, b)
