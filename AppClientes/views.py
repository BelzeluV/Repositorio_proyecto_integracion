from django.shortcuts import render
from Appi.api.services import request_api

# Create your views here.
def inicio(request):


    productos = request_api.get("productos/")

    data = {"productos": productos}
    return render(request, "inicio/inicio.html", data)