from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import Widget
from .models import Producto, Mona, Usuario


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
            'imagen': 'Imagen'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre producto'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion de producto'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            
        }

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombreUsu', 'rutUsu', 'direccionUsu', 'correoUsu', 'fechaNa' , 'password']
        labels = {
            'nombreUsu' : 'Nombre', 
            'rutUsu': 'Rut', 
            'direccionUsu' : 'Direccion', 
            'correoUsu' : 'Correo', 
            'fechaNa' : 'Fecha de nacimiento', 
            'password': 'Clave'

        }
        widgets={
            'nombreUsu': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'rutUsu': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Rut'
                }
            ),
            'direccionUsu': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion'
                }
            ),
            'correoUsu': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo'
                }
            ),
            'fechaNa': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de nacimiento',
                    'type': 'Date'
                }
                
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Clave'
                }
            )
        }