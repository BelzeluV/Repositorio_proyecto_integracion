from django.db import models
from django.contrib.auth.models import AbstractUser

opcionEstado = [
    [0,"Reservado"],
    [1,"En espera de revisión"],
    [2,"En revision"],
    [3,"en espera de repuestos"],
    [4,"En espera de Atencion del técnico"],
    [5,"En Atención de técnico"],
    [6,"Completado"],
    [7,"Cancelado"]
]
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
    RUT                 = models.CharField(default = '', max_length = 13,  unique = True, error_messages = {"unique": "El rut ya está registrado."}, blank=True)
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
    nombreproveedor     = models.CharField(max_length = 50)

    def __str__(self):
        return  self.nombreproveedor

class TipoProducto(models.Model):
    id_tipo             = models.AutoField(primary_key = True)
    nombretipo          = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta tipo de producto ya está registrado"})

    def __str__(self):
        return self.nombretipo

class Categoria(models.Model):
    id_categoria        = models.AutoField(primary_key = True)
    nombrecategoria     = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta categoria ya está registrada"})
    tipo_producto       = models.ForeignKey(TipoProducto,on_delete = models.PROTECT)
    def __str__(self):
        return self.nombrecategoria
    
class Subcategoria(models.Model):
    id_subcategoria     = models.AutoField(primary_key = True)
    nombre_subcategoria = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta subcategoria ya está registrada"})
    categoria           = models.ForeignKey(Categoria, on_delete = models.PROTECT)
    def __str__(self):
        return self.nombre_subcategoria

class Marca(models.Model):
    id_marca            = models.AutoField(primary_key = True)
    nombre_marca        = models.CharField(max_length = 40)
    def __str__(self):
        return self.nombre_marca

class Producto(models.Model):
    id_producto         = models.AutoField(primary_key = True)
    SKU                 = models.CharField(max_length = 10, unique = True, error_messages = {"unique" : "Este SKU ya está registrado"})
    nombre_producto     = models.CharField(max_length = 60)
    descripcion         = models.TextField(max_length = 1000)
    Precio_compra       = models.IntegerField()
    precio_venta        = models.IntegerField()
    precio_oferta       = models.IntegerField(blank = True)
    stock               = models.IntegerField()
    marca               = models.ForeignKey(Marca, on_delete = models.PROTECT)
    subcat_producto     = models.ForeignKey(Subcategoria, on_delete = models.PROTECT)
    imagen_producto     = models.ImageField(upload_to = "productos", blank = True)
    activo              = models.BooleanField(default = True)

    def __str__(self): 
        return self.nombre_producto

##modelos de las ordenes de servicio
class Orden(models.Model):
    id_orden            = models.AutoField(primary_key = True)
    descripcion         = models.CharField(max_length = 500)
    nombre_dueño        = models.CharField(max_length = 50, null=True)
    estado              = models.IntegerField(default = 0, choices = opcionEstado)
    fecha_creacion      = models.DateField(null = True)
    
    def __str__(self):
        return f'{self.id_orden}'

class Ordenxproducto(models.Model):
    id_ordenxproducto   = models.AutoField(primary_key=True)
    id_orden_relacion   = models.ForeignKey(Orden, on_delete = models.CASCADE)
    id_producto         = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad            = models.IntegerField()

    class Meta:
        ordering = ['-id_ordenxproducto']

    def __str__(self):
        return (f'Orden: {self.id_orden_relacion}, Producto relacionado: {self.id_producto}').format(**self.__dict__)