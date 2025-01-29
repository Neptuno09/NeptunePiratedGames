from django.core.exceptions import ValidationError

# Validar si la URL tiene una extensión de imagen válida
def validate_image_url(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    if not any(value.endswith(ext) for ext in valid_extensions):
        raise ValidationError(f"La URL no es válida para una imagen. Asegúrate de que termine con una extensión de imagen como: {', '.join(valid_extensions)}")