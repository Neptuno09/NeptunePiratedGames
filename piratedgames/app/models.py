from django.db import models
from .validators import validate_image_url  # Importar la función de validación personalizada
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, Group, Permission
from colorfield.fields import ColorField
import markdown

GENERO_CHOICES = [
    ('NULL', 'Género no especificado'),
    ('ACC', 'Acción'),
    ('HOR', 'Horror'),
    ('ADV', 'Aventura'),
    ('RPG', 'RPG'),
    ('SIM', 'Simulador'),
    ('DEP', 'Deportes'),
    ('EST', 'Estrategia'),
    ('PLT', 'Plataformas'),
    ('PZL', 'Puzle'),
    ('CRG', 'Carreras'),
    ('LCH', 'Lucha'),
    ('MSO', 'Musical'),
    ('TIR', 'Tiro'),
    ('OTR', 'Otros'),
    ('FIC', 'Ficción interactiva'),
    ('MMO', 'Multijugador masivo en línea'),
    ('RTS', 'Estrategia en tiempo real'),
    ('TAB', 'Juegos de mesa'),
    ('TRV', 'Trivia'),
    ('VR', 'Realidad virtual'),
]
class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(validators=[validate_image_url], blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(
        max_length=4,
        choices=GENERO_CHOICES,
        default='NULL',  # Género por defecto
    )
    slug = models.SlugField(unique=True, blank=True, null=True)  # Campo slug

    def save(self, *args, **kwargs):
        if not self.slug:  # Si no tiene slug, lo genera automáticamente
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def descripcion_html(self):
        """Convierte la descripción en Markdown a HTML"""
        return markdown.markdown(self.descripcion)
    
    def __str__(self):
        return self.titulo  
    
class CustomUser(AbstractUser):
    descripcion = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')
    color = ColorField(default='#313131', format='hex')
    def __str__(self):
        return self.username