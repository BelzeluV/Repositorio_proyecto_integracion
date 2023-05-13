from django.shortcuts import render
from Appi.api.services import request_api

# Create your views here.
def inicio(request):
    subcat = "subcategorias/"
    cat = "categorias/"
    prod = "productos/"

    productos = request_api.get(prod)
    subcategorias = request_api.get(subcat)
    categorias = request_api.get(cat)
    
    data = {"subcategorias" : subcategorias, "categorias" : categorias,"productos": productos}
    return render(request, "inicio/inicio.html", data)