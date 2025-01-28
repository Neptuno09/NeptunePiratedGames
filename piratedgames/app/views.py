from django.http import HttpResponse
from django.shortcuts import render
from .models import Juego

def inicio(request):
    juegos = Juego.objects.all()
    return render(request, 'inicio.html', {'juegos': juegos})