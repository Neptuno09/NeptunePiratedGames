from django.db import models
from .validators import validate_image_url  # Importar la función de validación personalizada
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
    descripcion = models.TextField()
    imagen = models.URLField(validators=[validate_image_url], blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(
        max_length=4,
        choices=GENERO_CHOICES,
        default='NULL',  # Género por defecto
    )
    def __str__(self):
        return self.titulo  