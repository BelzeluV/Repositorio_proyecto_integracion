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
            if response != None:
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

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de subcategorias exitosa!" +Style.RESET_ALL+"\n" )
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

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de categorias exitosa!" +Style.RESET_ALL+"\n" )
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

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de productos exitosa!" +Style.RESET_ALL+"\n" )
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

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de tipos de producto exitosa!" +Style.RESET_ALL+"\n" )
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

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de marcas exitosa!" +Style.RESET_ALL+"\n" )
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

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de proveedores exitosa!" +Style.RESET_ALL+"\n" )
                    return arreglo
                
                elif Url == "ordenes/":
                    for orden in response:
                        id_orden = orden["id_orden"]
                        descripcion = orden["descripcion"]
                        nombre_dueño = orden["nombre_dueño"]
                        estado = orden["estado"]
                        fecha_creacion = orden["fecha_creacion"]
                        usuario_rel = orden["usuario_rel"]

                        diccionario = {
                            "id_orden": id_orden,
                            "descripcion": descripcion,
                            "nombre_dueño": nombre_dueño,
                            "estado": estado,
                            "fecha_creacion": fecha_creacion,
                            "usuario_rel": usuario_rel,
                        }
                        arreglo.append(diccionario)
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de orden exitosa!" + Style.RESET_ALL + "\n")
                    return arreglo

                elif Url == "ordenxproductos/":
                    for ordenxproducto in response:
                        id_ordenxproducto = ordenxproducto["id_ordenxproducto"]
                        id_orden_relacion = ordenxproducto["id_orden_relacion"]
                        id_producto = ordenxproducto["id_producto"]
                        cantidad = ordenxproducto["cantidad"]

                        diccionario = {
                            "id_ordenxproducto": id_ordenxproducto,
                            "id_orden_relacion": id_orden_relacion,
                            "id_producto": id_producto,
                            "cantidad": cantidad,
                        }
                        arreglo.append(diccionario)
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de orden por producto exitosa!" + Style.RESET_ALL + "\n")
                    return arreglo
            
            else:
                print(Fore.RED + "no hubo respuesta del servidor, verifica la conexión a internet," +Style.RESET_ALL+"\n")
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            print(Fore.RED + "la Url "+Url+" ingresada no tiene coincidencias en la API del servidor\n     código de error: "+ error_msg + Style.RESET_ALL+"\n")
            return error
    
    def search(url, id):
        error = {"error 404": "no obtuvimos una respuesta del servidor"}
        try:
            response = requests.get(base + url + str(id) + "/").json()
            if response is not None:

                if url == "productos/":
                    producto = response
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
                        "id_producto": id_producto,
                        "sku": sku,
                        "nombre_producto": nombre_producto,
                        "descripcion": descripcion,
                        "Precio_compra": Precio_compra,
                        "precio_venta": precio_venta,
                        "precio_oferta": precio_oferta,
                        "stock": stock,
                        "marca": marca,
                        "subcat_producto": subcat_producto,
                        "imagen_producto": imagen_producto,
                        "activo": activo,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de producto exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario
                
                elif url == "tipoProd/":
                    tipo = response
                    id_tipo = tipo["id_tipo"]
                    id_nombre = tipo["nombretipo"]

                    diccionario = {
                        "id_tipo" : id_tipo,
                        "id_nombre" : id_nombre
                    }

                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de tipos de producto exitosa!" +Style.RESET_ALL+"\n" )
                    return diccionario
                
                elif url == "proveedores/":
                    proveedor = response
                    id_proveedor = proveedor["id_proveedor"]
                    nombre_proveedor = proveedor["nombreproveedor"]
                    direccion = proveedor["direccion"]
                    telefono = proveedor["telefono"]
                    email = proveedor["email"]
                    fecha_registro = proveedor["fecha_registro"]

                    diccionario = {
                        "id_proveedor": id_proveedor,
                        "nombre_proveedor": nombre_proveedor,
                        "direccion": direccion,
                        "telefono": telefono,
                        "email": email,
                        "fecha_registro": fecha_registro,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de proveedor exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario

                elif url == "categorias/":
                    categoria = response
                    id_categoria = categoria["id_categoria"]
                    nombre_categoria = categoria["nombrecategoria"]
                    tipo_producto = categoria["tipo_producto"]

                    diccionario = {
                        "id_categoria": id_categoria,
                        "nombre_categoria": nombre_categoria,
                        "tipo_producto": tipo_producto,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de categoría exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario

                elif url == "subcategorias/":
                    subcategoria = response
                    id_subcategoria = subcategoria["id_subcategoria"]
                    nombre_subcategoria = subcategoria["nombre_subcategoria"]
                    categoria = subcategoria["categoria"]

                    diccionario = {
                        "id_subcategoria": id_subcategoria,
                        "nombre_subcategoria": nombre_subcategoria,
                        "categoria": categoria,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de subcategoria exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario

                elif url == "marcas/":
                    marca = response
                    id_marca = marca["id_marca"]
                    nombre_marca = marca["nombre_marca"]

                    diccionario = {
                        "id_marca": id_marca,
                        "nombre_marca": nombre_marca,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de marca exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario

                elif url == "ordenes/":
                    orden = response
                    id_orden = orden["id_orden"]
                    descripcion = orden["descripcion"]
                    nombre_dueño = orden["nombre_dueño"]
                    estado = orden["estado"]
                    fecha_creacion = orden["fecha_creacion"]
                    usuario_rel = orden["usuario_rel"]

                    diccionario = {
                        "id_orden": id_orden,
                        "descripcion": descripcion,
                        "nombre_dueño": nombre_dueño,
                        "estado": estado,
                        "fecha_creacion": fecha_creacion,
                        "usuario_rel": usuario_rel,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de orden exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario

                elif url == "ordenxproductos/":
                    ordenxproducto = response
                    id_ordenxproducto = ordenxproducto["id_ordenxproducto"]
                    id_orden_relacion = ordenxproducto["id_orden_relacion"]
                    id_producto = ordenxproducto["id_producto"]
                    cantidad = ordenxproducto["cantidad"]

                    diccionario = {
                        "id_ordenxproducto": id_ordenxproducto,
                        "id_orden_relacion": id_orden_relacion,
                        "id_producto": id_producto,
                        "cantidad": cantidad,
                    }
                    print(Fore.GREEN + "\n"+'\u2713'+ " Petición de orden por producto exitosa!" + Style.RESET_ALL + "\n")
                    return diccionario

            else:
                print(Fore.RED + "No hubo respuesta del servidor, verifica la conexión a internet." + Style.RESET_ALL + "\n")

        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            print(Fore.RED + "La URL " + url + " ingresada no tiene coincidencias en la API del servidor.\nCódigo de error: " + error_msg + Style.RESET_ALL + "\n")
        
        return error
#     no listo todavía
    def post(Url, data):
        response = requests.post(base+Url+"post/", params=data).json()

    def delete(Url,id):
        response = requests.delete(base+Url+id) 