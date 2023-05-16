
class Carro:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro
    


    def agregar(self,Producto):
        id_producto = (Producto.id_producto)
        print(id_producto)
        
        if id_producto not in self.carro.keys():
            self.carro[id_producto] = {
                "id_producto"   : Producto.id_producto,
                "nombre"        : Producto.nombre_producto,
                "precio"        : Producto.precio,
                "cantidad"      : 1,
                "imagen"        : Producto.FotoProducto.url
            }
        else:
            for key,value in self.carro.items():
                if key == id_producto:
                    value["cantidad"] += 1
                    
        self.guardar_carro()



    def agregar(self,Producto):
        id_producto = str(Producto.id_producto)
        print(id_producto)
        if id_producto not in self.carro.keys():
            self.carro[id_producto] = {
                "id_producto"   : Producto.id_producto,
                "nombre"        : Producto.nombre_producto,
                "precio"        : Producto.precio,
                "imagen"        : Producto.FotoProducto.url,
                "cantidad"      : 1
            }
    
        else:
            for key, value in self.carro.items():
                if key == id_producto:
                    value["cantidad"] = value["cantidad"]+1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
    
    def eliminar(self,Producto):
        id_producto = str(Producto.id_producto)

        Producto.id_producto = id_producto
        if Producto.id_producto in self.carro:
            del self.carro[Producto.id_producto]
        self.guardar_carro()
    
    def restar_producto(self,Producto):
        id_producto = str(Producto.id_producto)
        for key, value in self.carro.items():
            if key == id_producto:
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.eliminar(Producto)
                break          
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
