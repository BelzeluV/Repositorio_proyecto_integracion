from django.shortcuts import render
from .models import *
from .api.services import *
# Create your views here.

#CRUD 
def menuCategorias(request):
    return render(request,"CRUD_categorias/menu.html")


def menuTipoProducto(request):
    return render(request,"CRUD_tipoproducto/menu.html")


def menuSubcategorias(request):
    return render(request,"CRUD_subcategorias/menu.html")


def test(request):
    retraso = "dd"
    productos = request_api.get("productos/")
    data = {"productos" : productos}
    return render(request,"test/test.html", data)