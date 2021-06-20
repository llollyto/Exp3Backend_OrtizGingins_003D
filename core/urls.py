from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ingresarProducto, home, Monas, ingresarUsuario, productos, info, subirImagen


urlpatterns=[
    path('', views.home, name='home'),
    path('Monas', views.Monas, name='Monas'),
    path('productos', views.productos, name='productos'),
    path('info', views.info, name='info'),
    path('ingresarProducto', views.ingresarProducto, name="ingresarProducto"),
    path('subirImagen', views.subirImagen, name="subirImagen"),
    path('ingresarUsuario', ingresarUsuario, name="ingresarUsuario"),
 
    #path('test/', views.test, name='test'),
]

