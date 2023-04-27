from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
opcionesSexo = [
    [0,"Hombre"],
    [1,"Mujer"],
    [2,"No especificado"]
]
opcionescomuna = [
    [0,"Peñaflor"],
    [1,"Cerrillos"],
    [2,"Cerro Navia"],
    [3,"Conchalí"],
    [4,"El Bosque"],
    [5,"Estación Central"],
    [6,"Huechuraba"],
    [7,"Independencia"],
    [8,"La Cisterna"],
    [9,"La Florida"],
    [10,"La Granja"],
    [11,"La Pintana"],
    [12,"La Reina"],
    [13,"Las Condes"],
    [14,"Lo Barnechea"],
    [15,"Lo Espejo"],
    [16,"Lo Prado"],
    [17,"Macul"],
    [18,"Maipú"],
    [19,"Ñuñoa"],
    [20,"Pedro Aguirre Cerda"],
    [21,"Peñalolén"],
    [22,"Providencia"],
    [23,"Pudahuel"],
    [24,"Quilicura"],
    [25,"Quinta Normal"],
    [26,"Recoleta"],
    [27,"Renca"],
    [28,"San Joaquín"],
    [29,"San Miguel"],
    [30,"San Ramón"],
    [31,"Vitacura"],
    [32,"Puente Alto"],
    [33,"Pirque"],
    [34,"San José de Maipo"],
    [35,"Colina"],
    [36,"Lampa"],
    [37,"Tiltil"],
    [38,"San Bernardo"],
    [39,"Buin"],
    [40,"Calera de Tango"],
    [41,"Paine"],
    [42,"Melipilla"],
    [43,"Alhué"],
    [44,"Curacaví"],
    [45,"María Pinto"],
    [46,"San Pedro"],
    [47,"Talagante"],
    [48,"El Monte"],
    [49,"Isla de Maipo"],
    [50,"Padre Hurtado"]
]

class Usuario(AbstractUser):
    RUT                 = models.CharField(default = '', max_length = 13,  unique = True, error_messages = {"unique": "El rut ya está registrado."},blank=True)
    nombre_real         = models.CharField(default = '', max_length = 50)
    nacimiento          = models.DateField(null = True)
    genero              = models.IntegerField(default = 2, choices = opcionesSexo)
    telefono            = models.CharField(default = '', max_length = 15)
    Direccion           = models.CharField(default = '', max_length = 300)
    comuna              = models.IntegerField(null = True, blank = True, choices = opcionescomuna)  
    foto_de_Usuario     = models.ImageField(upload_to = "usuarios",null = True)

    class Meta:
        ordering = ['nombre_real']

    def __str__(self):
        return self.username
    
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
