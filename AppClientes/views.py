import random
from django.shortcuts import render,redirect
from Appi.api.services import request_api
from  .cart import Carrito  
from Appi import models
from django.contrib import messages



# Create your views here.
def inicio(request):
    productos = request_api.get("productos/")
    data = {"productos": productos}
    return render(request, "inicio/inicio.html", data)


def detalle(request,id):
    #despliegue 
    lista_productos   = request_api.get("productos/")
    producto          = request_api.search("productos/",int(id))
    marca             = request_api.search("marcas/",int(producto["marca"]))
    subcategoria      = request_api.search("subcategorias/", int(producto["subcat_producto"]))
    categoria         = request_api.search("categorias/",int(subcategoria["categoria"]))
    tipoprod          = request_api.search("tipoProd/",int(categoria["tipo_producto"]))
    lista_random      = random.sample(list(lista_productos),3)

    
    print("producto:"+str(producto)+"\nmarca: "+str(marca)+"\nsubcategoria: "+str(subcategoria)+"\ncategoria: "+str(categoria)+"\ntipoprod"+str(tipoprod))
    #manejo de la pagina





    data = {"producto" : producto, "recomendaciones" : lista_random, "marca" : marca, "subcategoria" : subcategoria,"categoria" : categoria, "tipo": tipoprod}
    return render(request, "detalles/detalle.html", data)







def carro(request):
    return render(request, "carro/carro.html")

def agregar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.agregar(Producto = producto) 
    messages.success(request,"Producto agregado con éxito")
    return redirect(to="carro")

def eliminar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.eliminar(Producto = producto)
    messages.success(request,"Producto eliminado con éxito")
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