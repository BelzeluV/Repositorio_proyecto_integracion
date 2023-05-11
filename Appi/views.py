from django.shortcuts import render
from .models import *
from .api import services
# Create your views here.

#CRUD 
def menuCategorias(request):
    return render(request,"CRUD_categorias/menu.html")


def menuTipoProducto(request):
    return render(request,"CRUD_tipoproducto/menu.html")


def menuSubcategorias(request):
    return render(request,"CRUD_subcategorias/menu.html")
def test(request):
    variable = services.generate_request
      
    
    ctx = {"variable": variable}
    return render(request,"test/test.html",ctx)