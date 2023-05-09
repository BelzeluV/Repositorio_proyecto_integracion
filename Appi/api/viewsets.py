from ..models import *
from .serializers import *
from rest_framework import viewsets

class ProveedorViewset(viewsets.ModelViewSet):
    queryset            = Proveedor.objects.all()
    serializer_class    = proveedorSerializer

class TipoProductoViewset(viewsets.ModelViewSet):
    queryset            = TipoProducto.objects.all()
    serializer_class    = TipoProductoSerializer

class SubcategoriaViewset(viewsets.ModelViewSet):
    queryset            = Subcategoria.objects.all()
    serializer_class    = SubcategoriaSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset            = Categoria.objects.all()
    serializer_class    = categoriaSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset            = Producto.objects.all()
    serializer_class    = productoSerializer

class OrdenViewset(viewsets.ModelViewSet):
    queryset            = Orden.objects.all()
    serializer_class    = OrdenSerializer

class OrdenxproductoViewset(viewsets.ModelViewSet):
    queryset            = Ordenxproducto.objects.all()
    serializer_class    = OrdenxproductoSerializer