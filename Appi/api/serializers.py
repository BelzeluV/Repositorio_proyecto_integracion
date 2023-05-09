from rest_framework import serializers
from ..models import *


class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Proveedor
        fields  = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = TipoProducto
        fields  = '__all__'

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Categoria
        fields  = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Subcategoria
        fields  = '__all__'

class productoSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Producto
        fields  = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Orden
        fields  = '__all__'

class OrdenxproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Ordenxproducto
        fields  = '__all__'
