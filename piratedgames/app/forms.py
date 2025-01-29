from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Juego

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'descripcion', 'imagen', 'url', 'genero']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }