import random
from django.shortcuts import render,redirect
from Appi.api.services import request_api
from .cart.cart import Cart as Carrito
from Appi import models
from django.contrib import messages



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

def carro(request):
    return render(request, "carro/carro.html")
def agregar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.agregar(Producto = producto)
    messages.success(request,"Producto agregado con exito")
    return redirect(to="carro")

def eliminar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.eliminar(Producto = producto)
    messages.success(request,"Producto eliminado con exito")
    return redirect(to="carro")

def restar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.restar_producto(Producto = producto)
    return redirect(to="carro")

def vaciar_carro(request):
    carro = Carrito.Carro(request)
    carro.limpiar_carro()
    messages.success(request,"El carro fue Vaciado")
    return redirect("")

