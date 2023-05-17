import random
from django.shortcuts import render
from Appi.api.services import request_api

# Create your views here.
def inicio(request):
    productos = request_api.get("productos/")
    data = {"productos": productos}
    return render(request, "inicio/inicio.html", data)

def detalle(request,id):
    #despliegue
    lista_productos = request_api.get("productos/")
    lista_random = random.sample(list(lista_productos),3)
    producto = request_api.search("productos/",int(id))
    marcas = request_api.get("marcas/")


    #manejo de la pagina


    
    data = {"producto" : producto, "recomendaciones" : lista_random, "marcas" : marcas}

    return render(request, "detalles/detalle.html", data)