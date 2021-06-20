from django.shortcuts import render, redirect
from .models import Producto
from .models import Mona
from .forms import ProductoForm, UsuarioForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.

def Monas(request):
    mona = Mona.objects.all()
    return render(request, 'core/Monas.html', context={'Mona': mona})

def productos(request):
    
    producto = Producto.objects.all()
    print(producto)
    for i, c in enumerate(producto):
         print(c.imagen.url)
    return render(request, 'core/productos.html',  context={'Producto': producto})

def info(request):
    return render(request, 'core/info.html')

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')


def ingresarProducto(request) :
    if request.method=='POST' :
        producto_form = ProductoForm(request.POST) 
        if producto_form.is_valid():
            producto_form.save()
            return redirect('home')
    else:
        producto_form = ProductoForm()
    return render(request, 'core/forms.html'  , {'producto_form': producto_form})

def subirImagen(request):
    if request.method == 'POST' and request.FILES['imagenloa']:
        imagenes = request.FILES['imagenloa']
        print(imagenes.name)
        print(imagenes.size)
        if imagenes.is_valid():
            imagenes.save()
        return render(request, 'core/forms.html')

def ingresarUsuario(request):
    if request.method=='POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('home')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'core/usuform.html'  , {'usuario_form': usuario_form})

