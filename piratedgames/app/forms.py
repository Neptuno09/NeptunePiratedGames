from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Juego
from django.contrib.auth.models import User, Group, Permission
from .models import CustomUser
from colorfield.forms import ColorField

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Usuario", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Correo Electrónico", 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'descripcion', 'imagen', 'url', 'genero']  # No incluimos el campo 'slug'
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Escribe una descripción... (puedes usar Markdown)',
                'class': 'form-control',
                'rows': 5
            }),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class UserEditForm(forms.ModelForm):
    descripcion = forms.CharField(
        label="Descripción",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    color = ColorField(
        label="Color de perfil",
        required=False,
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['descripcion', 'color']
