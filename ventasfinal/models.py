from django.db import models
from django.contrib import admin
from django.utils import timezone




class Usuario(models.Model):
    usuario1  =   models.CharField(max_length=30)
    def __str__(self):
        return self.usuario1

class Articulo(models.Model):
    articulo1  =   models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.articulo1
        


class Venta(models.Model):
    fecha_ingreso = models.DateField(default=timezone.now)
    DPIcliente  =   models.CharField(max_length=30)
    cantidad  =   models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
            

class VentaInLine(admin.TabularInline):
    model = Venta
    extra = 3

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class ArticuloAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)