from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'nacimiento', 'genero', 'telefono', 'Direccion', 'comuna')
    list_filter = ('genero', 'comuna')
    search_fields = ('username', 'email', 'telefono')
    
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombreproveedor', 'direccion', 'telefono', 'email', 'fecha_registro')
    list_filter = ('fecha_registro',)
    search_fields = ('nombreproveedor', 'direccion', 'email')

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('id_tipo', 'nombretipo')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombrecategoria', 'tipo_producto')

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_subcategoria', 'nombre_subcategoria', 'categoria')

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id_marca', 'nombre_marca')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'SKU', 'nombre_producto', 'precio_venta', 'stock', 'marca', 'tipo_producto', 'categoria_producto', 'subcat_producto', 'proveedor', 'activo')
    list_filter = ('marca', 'tipo_producto', 'categoria_producto', 'subcat_producto', 'proveedor', 'activo')
    search_fields = ('nombre_producto', 'SKU')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'descripcion', 'nombre_dueño', 'estado', 'fecha_creacion', 'usuario_rel')
    list_filter = ('estado', 'fecha_creacion', 'usuario_rel')
    search_fields = ('descripcion', 'nombre_dueño')

class OrdenxproductoAdmin(admin.ModelAdmin):
    list_display = ('id_ordenxproducto', 'id_orden_relacion', 'id_producto', 'cantidad')
    list_filter = ('id_orden_relacion',)
    search_fields = ('id_orden_relacion__id', 'id_producto__nombre_producto')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Ordenxproducto, OrdenxproductoAdmin)
