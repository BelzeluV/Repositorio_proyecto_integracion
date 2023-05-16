def importe_total_carro(request):
    total = 0
    if 'carro' in request.session.keys():
        for key,value in request.session["carro"].items():
            total += int(value["precio"] * value["cantidad"])
    return {"importe_total_carro":total}