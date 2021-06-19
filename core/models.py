from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreUsu = models.CharField(max_length=60)
    rutUsu = models.CharField(max_length=12)
    direccionUsu = models.CharField(max_length=70)
    correoUsu = models.CharField(max_length=70)
    fechaNa = models.DateField()
    password = models.CharField(max_length=20)
    

def __str__(self):
    return self.Usuario

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='img2', max_length=100,null=True)


def __str__(self):
    return self.Producto

class Mona(models.Model):
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, blank=True)

def __str__(self):
    return self.Mona




