from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ingresarProducto, home, Monas, productos, subirImagen, IngresoUsuario, UsuarioList, UsuarioEdit
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
    path('', views.home, name='home'),
    path('Monas', views.Monas, name='Monas'),
    path('productos', views.productos, name='productos'),
    path('info', views.info, name='info'),
    path('ingresarProducto', views.ingresarProducto, name="ingresarProducto"),
    path('subirImagen', views.subirImagen, name="subirImagen"),
    path('IngresoUsuario', views.IngresoUsuario, name="IngresoUsuario"),
    path('listar', views.UsuarioList, name="UsuarioList"),
    path('editar/<int:id>/', views.UsuarioEdit, name="UsuarioEdit"),
 
    #path('test/', views.test, name='test'),
]

