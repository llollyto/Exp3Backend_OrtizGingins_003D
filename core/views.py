from django.shortcuts import render, redirect
from .models import Producto
from .models import Mona
from .forms import ProductoForm
from django.http import HttpResponse
from pprint import pprint
# Create your views here.

def Monas(request):
    mona = Mona.objects.all()
    return render(request, 'core/Monas.html', context={'Mona': mona})

def productos(request):
    producto = Producto.objects.all()
    pprint(globals())
    return render(request, 'core/productos.html',  context={'Producto': producto})

def info(request):
    return render(request, 'core/info.html')

def home(request):
    return render(request, 'core/home.html')


def ingresarProducto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('home')
    else:
        producto_form = ProductoForm()
    return render(request, 'core/forms.html'  , {'producto_form': producto_form})
