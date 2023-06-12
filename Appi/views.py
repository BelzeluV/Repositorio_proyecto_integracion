from django.shortcuts import redirect, render
from .models import *
from .api.services import *
from .migrar import *

# Create your views here.
def synchronization(request):
    doall()
    return redirect(to = "inicioBackoffice")

def ValidarUsuario(request):
    if request.user.is_authenticated:
        if request.user.is_superuser :
            return redirect(to = "inicioBackoffice")
        if request.user.is_staff:
            return redirect(to = "inicioBackoffice")
        else:
            return redirect(to = "inicio")
    return redirect('login')
#CRUD 
def inicioBackoffice(request):
    return render(request, "Inicio/InicioBackoffice.html")





def menuCategorias(request):
    return render(request,"CRUD_categorias/menu.html")


def menuTipoProducto(request):
    return render(request,"CRUD_tipoproducto/menu.html")


def menuSubcategorias(request):
    return render(request,"CRUD_subcategorias/menu.html")




def test(request):
    productos = "subcategorias/"
    variable = "categorias/"
    

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
    
    data = {"variable": variable}
    data = {"subcategorias" : subcategorias, "categorias" : categorias,"productos": productos,"tipoproducto": tipoproducto, "marcas" : marcas}

    return render(request,"test/test.html", data)