from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import Widget
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


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

