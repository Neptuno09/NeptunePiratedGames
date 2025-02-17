"""
URL configuration for piratedgames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('juegos/', views.juegos, name='juegos'),
    path('adminselector/', views.adminselector, name='adminselector'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('addgames', views.addgames, name='addgames'),
    path('juego/<slug:slug>/', views.gamepage, name='gamepage'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.users, name='users'),
    path('user/<str:username>/', views.see_user, name='user'),
    path('account', views.edit_profile, name='account'),
    path('editgame/<slug:slug>/', views.editgame, name='editgame'),
    path('gamelist/', views.gamelist, name='gamelist'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)