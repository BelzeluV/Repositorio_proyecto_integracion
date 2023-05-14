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

    subcat = "subcategorias/"
    cat = "categorias/"
    prod = "productos/"
    tipo = "tipoProd/"
    mar = "marcas/"
    productos = request_api.get(prod)
    subcategorias = request_api.get(subcat)
    categorias = request_api.get(cat)
    tipoproducto = request_api.get(tipo)
    marcas = request_api.get("marcas/")
    
    data = {"subcategorias" : subcategorias, "categorias" : categorias,"productos": productos,"tipoproducto": tipoproducto, "marcas" : marcas}

    return render(request,"test/test.html", data)