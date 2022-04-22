from django.db import models

# Create your models here.
class Fichas(models.Model):
    codigo_ficha = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    
    def __str__(self):
        return self.codigo_ficha


class Book(models.Model):
    codigo_ficha = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.codigo_ficha