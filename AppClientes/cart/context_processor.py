import random
from Appi.api import services as s

desactivado = True

def importe_total_carro(request):
    total = 0
    if 'carro' in request.session.keys():
        for key,value in request.session["carro"].items():
            total += int(value["precio"] * value["cantidad"])
    return {"importe_total_carro":total}

def categorias_productos(request):
    lista_random = random.sample(list(s.request_api.get("categorias/")),6)
    return {"cate" : lista_random}

def subcategorias_productos(request):
    lista_random = random.sample(list(s.request_api.get("subcategorias/")),6)
    return {"subcate" : lista_random}