from django.shortcuts import render, redirect
from .models import Producto
from .models import Mona
from .models import Usuario
from .forms import  UsuarioForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView




# Create your views here.

def Monas(request):
    mona = Mona.objects.all()
    return render(request, 'core/Monas.html', context={'Mona': mona})

def productos(request):
    producto = Producto.objects.all()
    return render(request, 'core/productos.html',  context={'Producto': producto})

def info(request):
    return render(request, 'core/info.html')

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')


def IngresoUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UsuarioForm()
    return render(request, 'core/usuform.html'  , {'form': form})

def UsuarioList(request):
    usuario = Usuario.objects.all().order_by('id')
    contexto = {'usu': usuario}
    return render(request, 'core/infoUsuario.html'  , contexto)


def UsuarioEdit(request, id_usuario):
    usu = Usuario.objects.get(id=id_usuario)
    if request.method == 'GET':
        form = UsuarioForm(instance=usu)
    else:
        form = UsuarioForm(request.POST, instance=usu)
        if form.is_valid():
            form.save()
        return redirect('UsuarioList')
    return render(request, 'core/usuform.html', {'form':form})


def UsuarioDelete(request, id_usuario):
    usu = Usuario.objects.get(id=id_usuario)
    if request.method == 'POST':
        usu.delete()
        return redirect('UsuarioList')
    return render(request, 'core/usuarioDelete.html', {'usu':usu})

