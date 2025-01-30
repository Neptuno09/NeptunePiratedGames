from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Juego
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "descripcion")
    fieldsets = UserAdmin.fieldsets + (
        ("Información adicional", {"fields": ("descripcion", "color")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Información adicional", {"fields": ("descripcion", "color")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Juego)