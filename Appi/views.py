from django.shortcuts import render
from .models import *
from .api.services import *
# Create your views here.
def generar_arreglo(tamano):
    arreglo = []
    variable = 0.1
    for _ in range(tamano):
        arreglo.append(variable)
        variable += 0.5
    return arreglo
#CRUD 
def menuCategorias(request):
    return render(request,"CRUD_categorias/menu.html")


def menuTipoProducto(request):
    return render(request,"CRUD_tipoproducto/menu.html")


def menuSubcategorias(request):
    return render(request,"CRUD_subcategorias/menu.html")


def test(request):
    lista_productos = request_api.get("productos/")  # Obtener la lista de productos de la API
    tamaño = len(lista_productos)
    retraso_animacion = generar_arreglo(tamaño)  # Generar el arreglo de retrasos
    print(retraso_animacion)
    for i in lista_productos:
        for j in retraso_animacion:
            if i.key == j.key:
                print(i.key, j.key)
    data = {'lista_productos': lista_productos, 'retraso_animacion': retraso_animacion}
    
    return render(request,"test/test.html", data)