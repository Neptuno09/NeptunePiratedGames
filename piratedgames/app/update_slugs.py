import django
import os
import sys
from django.utils.text import slugify

# Agrega la ruta del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configura Django antes de importar modelos
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piratedgames.settings")  # Reemplaza con el nombre de tu proyecto
django.setup()

# Ahora importa los modelos correctamente
from app.models import Juego  # Asegúrate de que esta ruta sea correcta según tu estructura de archivos

# Actualiza los slugs de los juegos sin slug
def actualizar_slugs():
    juegos_sin_slug = Juego.objects.filter(slug__isnull=True) | Juego.objects.filter(slug="")
    total = juegos_sin_slug.count()
    
    if total == 0:
        print("Todos los juegos ya tienen slug. No se hicieron cambios.")
        return

    for juego in juegos_sin_slug:
        juego.slug = slugify(juego.titulo)
        juego.save()
        print(f"Slug generado para: {juego.titulo} -> {juego.slug}")

    print(f"Actualización completada: {total} juegos actualizados.")

if __name__ == "__main__":
    actualizar_slugs()