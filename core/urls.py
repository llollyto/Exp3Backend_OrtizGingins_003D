from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
from .views import home, Monas, productos, IngresoUsuario, UsuarioList, UsuarioEdit, UsuarioDelete, login





urlpatterns=[
    path('', views.home, name='home'),
    path('Monas', views.Monas, name='Monas'),
    path('productos', views.productos, name='productos'),
    path('info', views.info, name='info'),
    path('IngresoUsuario', views.IngresoUsuario, name="IngresoUsuario"),
    path('listar', views.UsuarioList, name="UsuarioList"),
    path('editar/<int:id_usuario>/', views.UsuarioEdit, name="Edit"),
    path('eliminar/<int:id_usuario>/', views.UsuarioDelete, name="Delete"),
    path('', login, {'template_name': 'registration/login.html'}, name='login'),
    
]

