from django.contrib import admin
from .models import Producto,Categoria,Proveedor
# Register your models here.

class adminProducto(admin.ModelAdmin):
    list_display = ['nombre_producto']

class adminProveedor(admin.ModelAdmin):
    list_display = ['nombreproveedor']

class admincategoria(admin.ModelAdmin):
    list_display = ['nombrecategoria']
 


admin.site.register(Producto,adminProducto)
admin.site.register(Proveedor,adminProveedor)
admin.site.register(Categoria,admincategoria)