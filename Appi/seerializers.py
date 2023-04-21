from rest_framework import serializers
from .models import *


class productoSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Producto
        fields  = '__all__'

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Categoria
        fields  = '__all__'


class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        
        model   = Proveedor
        fields  = '__all__'