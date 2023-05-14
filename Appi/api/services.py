import requests
from colorama import init, Fore, Style

init()
base = "http://localhost:8000/api/"

class request_api():

    def get(Url):
        error = [{"error 404": "no obtuvimos una respuesta del servidor"}]
        try:
            response = requests.get(base+Url).json()
            arreglo = []
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
                elif Url == "marcas/":
                    for marcas in response:
                        id_marca = marcas["id_marca"]
                        nombre_marca = marcas["nombre_marca"]
                        diccionario = {
                            "id_marca" : id_marca,
                            "nombre_marca" : nombre_marca
                            }
                        arreglo.append(diccionario)
                    return arreglo
                elif Url == "proveedores/":
                    for pro in response:
                        id_proveedor = pro["id_proveedor"]
                        nombreproveedor = pro["nombreproveedor"]
                        direccion = pro["direccion"]
                        telefono = pro["telefono"]
                        email = pro["email"]
                        fecha_registro = pro["fecha_registro"]
                        diccionario = {
                            "id_proveedor" : id_proveedor,
                            "nombreproveedor" : nombreproveedor,
                            "direccion" : direccion,
                            "telefono" : telefono,
                            "email" : email,
                            "fecha_registro" : fecha_registro
                        }
                        arreglo.append(diccionario)
                    return arreglo
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            print(Fore.RED + "hubo un problema con la peticion: "+ error_msg + Style.RESET_ALL)
            return error
    def delete(url,id):
        wena = 2