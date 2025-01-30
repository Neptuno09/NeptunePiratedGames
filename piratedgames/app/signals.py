from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        try:
            default_group = Group.objects.get(name='Usuario')  # Asegúrate de que este nombre sea correcto
            instance.groups.add(default_group)
        except Group.DoesNotExist:
            print("El grupo no existe.")

@receiver(post_save, sender=CustomUser)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        # Lista de codenames de permisos que deseas asignar
        permissions_codenames = ['add_customuser', 'change_customuser', 'delete_customuser', 'view_customuser', 'view_juego']
        
        # Obtener los permisos y asignarlos al usuario
        permissions = Permission.objects.filter(codename__in=permissions_codenames)
        instance.user_permissions.add(*permissions)