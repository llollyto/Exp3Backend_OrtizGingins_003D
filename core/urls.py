from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ingresarProducto, home, Monas, ingresarUsuario, productos, info, login

urlpatterns=[
    path('', views.home, name='home'),
    path('Monas', views.Monas, name='Monas'),
    path('productos', views.productos, name='productos'),
    path('info', views.info, name='info'),
    path('ingresarProducto', ingresarProducto, name="ingresarProducto"),
    path('ingresarUsuario', ingresarUsuario, name="ingresarUsuario"),
    path('login', views.login, name="login")
    #path('test/', views.test, name='test'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)