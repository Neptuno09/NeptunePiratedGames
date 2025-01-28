from django.db import models

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_juegos/', blank=True, null=True)

    def __str__(self):
        return self.titulo