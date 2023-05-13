import requests

base = "http://localhost:8000/api/"





class request_api():

    def get(Url):
        response = requests.get(base+Url).json()
        arreglo = []
        error = [{"error 404": "no obtuvimos una respuesta"}]
        if response:
            if Url == "subcategorias/":
                for subcategoria in response:
                    id_subcategoria = subcategoria["id_subcategoria"]               #el elemento de  la subcategoria
                    nombre_subcategoria = subcategoria["nombre_subcategoria"]
                    categoria = subcategoria["categoria"]
                    diccionario = {
                        "id_subcategoria": id_subcategoria,
                        "nombre_subcategoria": nombre_subcategoria,
                        "categoria": categoria
                    }
                    arreglo.append(diccionario)
                return arreglo
            elif Url == "categorias/":
                for categoria in response :
                    id_categoria = categoria["id_categoria"]
                    nombrecategoria = categoria["nombrecategoria"]
                    tipo_producto = categoria["tipo_producto"]
                    diccionario = {
                        "id_categoria":id_categoria,
                        "nombrecategoria": nombrecategoria,
                        "tipo_producto": tipo_producto
                    }
                    arreglo.append(diccionario)
                return arreglo
            elif Url == "productos/":
                for producto in response:
                    id_producto = producto["id_producto"]
                    sku = producto["SKU"]
                    nombre_producto = producto["nombre_producto"]
                    descripcion = producto["descripcion"]
                    Precio_compra = producto["Precio_compra"]
                    precio_venta = producto["precio_venta"]
                    precio_oferta = producto["precio_oferta"]
                    stock = producto["stock"]
                    marca = producto["marca"]
                    subcat_producto = producto["subcat_producto"]
                    imagen_producto = producto["imagen_producto"]
                    activo = producto["activo"]
                    diccionario = {
                        "id_producto" : id_producto,
                        "sku" : sku,
                        "nombre_producto" : nombre_producto,
                        "descripcion" : descripcion,
                        "Precio_compra" : Precio_compra,
                        "precio_venta" : precio_venta,
                        "precio_oferta" : precio_oferta,
                        "stock" : stock,
                        "marca" : marca,
                        "subcat_producto" : subcat_producto,
                        "imagen_producto" : imagen_producto,
                        "activo" : activo,
                    }
                    arreglo.append(diccionario)
                return arreglo
            elif Url == "tipoProd/":
                for tipo in response:
                    id_tipo = tipo["id_tipo"]
                    id_nombre = tipo["nombretipo"]
                    diccionario = {
                        "id_tipo" : id_tipo,
                        "id_nombre" : id_nombre
                    }
                    arreglo.append(diccionario)
                return arreglo
            else:
                error = [{"error":"no existen mas objetos en la base de datos"}]
                return error
        else:
            return error 

