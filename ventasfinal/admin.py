from django.contrib import admin
from ventasfinal.models import Usuario, Articulo, UsuarioAdmin, ArticuloAdmin, Venta

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Venta)