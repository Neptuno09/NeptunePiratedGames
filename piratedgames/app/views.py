from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, RegisterForm, JuegoForm, UserEditForm
from django.contrib.auth.decorators import login_required

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

def logout_view(request):
    logout(request)
    return redirect('inicio')
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

@login_required

def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account')  # Redirige tras guardar los cambios
    else:
        form = UserEditForm(instance=request.user)

    # Obtener el color del usuario (por ejemplo, '#FF0000' para rojo)
    user_color = request.user.color if hasattr(request.user, 'color') else '#FF0000'  # Valor por defecto

    # Oscurecer el color
    darker_color = darken_color(user_color, 0.3)

    # Pasar tanto el formulario como el color oscuro a la plantilla
    return render(request, 'account.html', {'form': form, 'color': request.user.color, 'darker_color': darker_color})

def users(request):
    users = CustomUser.objects.all()
    for user in users:
        user.darker_color = darken_color(user.color)
    return render(request, 'users.html', {'users': users})

def see_user(request, username):
    # Obtiene el perfil basado en el nombre de usuario
    user = get_object_or_404(CustomUser, usuario__username=username)
    return render(request, 'user.html', {'user': user})