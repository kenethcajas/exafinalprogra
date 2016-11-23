from django.db import models
from django.contrib import admin
from django.utils import timezone




class Marca(models.Model):
    marca1  =   models.CharField(max_length=30)
    def __str__(self):
        return self.marca1

class Articulo(models.Model):
    articulo1  =   models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.articulo1
        


class Venta(models.Model):
    fecha_ingreso = models.DateField(default=timezone.now)
    DPIcliente  =   models.CharField(max_length=30)
    cantidad  =   models.CharField(max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
            

class VentaInLine(admin.TabularInline):
    model = Venta
    extra = 3

class MarcaAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class ArticuloAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)