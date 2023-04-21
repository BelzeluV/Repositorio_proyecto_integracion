from django.db import models


# Create your models here.


class Proveedor(models.Model):
    id_proveedor        = models.AutoField(primary_key = True)
    nombreproveedor     = models.CharField(max_length = 40)
    
    
    def __str__(self):
        return  self.nombreproveedor


class Categoria(models.Model):
    id_categoria        = models.AutoField(primary_key = True)
    nombrecategoria     = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombrecategoria

class Producto(models.Model):
    id_producto         = models.AutoField(primary_key = True)
    SKU                 = models.CharField(max_length = 10, unique = True, error_messages={"unique": "Este SKU ya está registrado"})
    nombre_producto     = models.CharField(max_length = 60)
    descripcion         = models.TextField(max_length = 1000)
    Precio_compra       = models.IntegerField()
    precio_venta        = models.IntegerField()
    precio_oferta       = models.IntegerField()
    stock               = models.IntegerField()
    proveedor           = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    categoria_producto  = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    imagen_producto     = models.ImageField(upload_to = "productos", blank = True)
    activo              = models.BooleanField(default = True)


    def __str__(self): 
        return self.nombre_producto

class Orden(models.Model): 
    id_orden            = models.AutoField(primary_key = True)

    def __str__(self):
        return self.id_orden
