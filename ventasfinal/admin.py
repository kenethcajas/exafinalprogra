from django.contrib import admin
from ventasfinal.models import Marca, Articulo, MarcaAdmin, ArticuloAdmin, Venta

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Venta)