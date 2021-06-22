from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import Widget
from .models import Producto, Mona, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


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
        model= Usuario
        fields = [
            'nombre',
            'sexo',
            'edad',
            'correo',
            'direccion',
            'password1'
        ]

        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad':'Edad',
            'correo': 'Email',
            'direccion': 'Direccion',
            'password1':'Clave',
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca nombre'
                }
            ),
            'sexo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca sexo'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca edad'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca correo'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca direccion'
                }
            ),
            'password1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduzca clave',
                    'type': 'password'
                }
            ),
        }

