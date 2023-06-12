from django.db import connections
from django.shortcuts import get_object_or_404
from .models import *
import json
from tabulate import tabulate



def sync_marca():
    with connections['default'].cursor() as oracle_cursor:                      # Obtener los datos de la tabla Marca en la base de datos Oracle
        oracle_cursor.execute("SELECT * FROM Appi_marca")
        oracle_marcas = oracle_cursor.fetchall()
        print(tabulate(oracle_marcas))
    with connections['sqlite'].cursor() as sqlite_cursor:                       # Sincronizar los datos de la tabla Marca
        for row in oracle_marcas:
            """ marca = Marca(
                id_marca=row[0],
                nombre_marca=row[1]
            )
            marca.save()"""
        print("marcas sincronizadas")
    return {"status": "correcto"}

def sync_tipo():
    with connections['default'].cursor() as oracle_cursor:
        # Obtener los datos de la tabla TipoProducto en la base de datos Oracle
        oracle_cursor.execute("SELECT * FROM Appi_tipoproducto")
        oracle_tiposproducto = oracle_cursor.fetchall()
        print(tabulate(oracle_tiposproducto))
    with connections['sqlite'].cursor() as sqlite_cursor:
        # Sincronizar los datos de la tabla TipoProducto
        for row in oracle_tiposproducto:
            tipo_producto = TipoProducto(
                nombretipo=row[1]
            )
            tipo_producto.save()
        print("tipos de productos sincronizados")
    return {"status": "correcto"}

def sync_cat():
    with connections['default'].cursor() as oracle_cursor:                      # Obtener los datos de la tabla Categoria en la base de datos Oracle
        oracle_cursor.execute("SELECT * FROM Appi_categoria")
        oracle_categorias = oracle_cursor.fetchall()
        print(tabulate(oracle_categorias))
    with connections['sqlite'].cursor() as sqlite_cursor: 
                            # Sincronizar los datos de la tabla Categoria
        for row in oracle_categorias:
            """ categoria = Categoria(
                nombrecategoria=row[1],
                tipo_producto_id=row[2]
            )
            categoria.save()"""
        print("categorias sincronizadas")
    return {"status": "correcto"}

def sync_subcat():
    with connections['default'].cursor() as oracle_cursor:                      # Obtener los datos de la tabla Subcategoria en la base de datos Oracle
        oracle_cursor.execute("SELECT * FROM Appi_subcategoria")
        oracle_subcategorias = oracle_cursor.fetchall()
        print(tabulate(oracle_subcategorias))
    with connections['sqlite'].cursor() as sqlite_cursor:                       # Sincronizar los datos de la tabla Subcategoria
        for row in oracle_subcategorias:
            """ subcategoria = Subcategoria(
                nombre_subcategoria=row[1],
                categoria_id=row[2]
            )
            subcategoria.save()"""
        print("subcategorias sincronizadas")
    return {"status": "correcto"}

def sync_proveedores():
    with connections['default'].cursor() as oracle_cursor:
        # Obtener los datos de la tabla Proveedor en la base de datos Oracle
        oracle_cursor.execute("SELECT * FROM Appi_proveedor")
        oracle_proveedores = oracle_cursor.fetchall()
        print(tabulate(oracle_proveedores))
    with connections['sqlite'].cursor() as sqlite_cursor:               # Sincronizar los datos de la tabla Proveedor
        for row in oracle_proveedores:
            """ proveedor = Proveedor(
                nombreproveedor=row[1],
                direccion=row[2],
                telefono=row[3],
                email=row[4],
                fecha_registro=row[5]
            )
            proveedor.save()"""
    return {"status": "correcto"}

def sync_products():
    with connections['default'].cursor() as oracle_cursor:
        # Obtener los datos de la tabla Producto en la base de datos Oracle
        oracle_cursor.execute("SELECT * FROM Appi_producto")
        oracle_productos = oracle_cursor.fetchall()
        print(tabulate(oracle_productos))
    with connections['sqlite'].cursor() as sqlite_cursor:
        # Sincronizar los datos de la tabla Producto
        for row in oracle_productos:
            """
            producto = Producto(
                SKU=row[1],
                nombre_producto=row[2],
                descripcion=row[3],
                Precio_compra=row[4],
                precio_venta=row[5],
                precio_oferta=row[6],
                stock=row[7],
                imagen_producto=row[8],
                activo = row[9],
                subcat_producto_id =    get_object_or_404(Subcategoria,id_subcategoria = row[10]),
                marca =                 get_object_or_404(Marca,id_marca = row[11]),
                categoria_producto =    get_object_or_404(Categoria,id_categoria =row[12]),
                proveedor =             get_object_or_404(Proveedor,id_proveedor = row[13]),
                tipo_producto =         get_object_or_404(TipoProducto,id_tipo = row[14]) 
            )
            producto.save()"""
        print("productos sincronizados")
    return {"status": "correcto"}

def doall():
    sync_cat()
    sync_marca()
    sync_products()
    sync_proveedores()
    sync_tipo()