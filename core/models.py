from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to="img2")


def __str__(self):
    return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    password1 = models.CharField(max_length=20)

def __str__(self):
    return self.nombre

class Mona(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, blank=True)

def __str__(self):
    return self.Mona




