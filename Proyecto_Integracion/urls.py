from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers  
from Appi import views as Appi
from Appi.api.viewsets import *
from AppClientes import views as Clientes


router = routers.DefaultRouter()

router.register(r'proveedores', ProveedorViewset)
router.register(r'tipoProd', TipoProductoViewset)
router.register(r'categorias', CategoriaViewset)
router.register(r'subcategorias', SubcategoriaViewset)
router.register(r'productos', ProductoViewset)
router.register(r'Ordenes', OrdenViewset)
router.register(r'OrdenxProductos', OrdenxproductoViewset)
router.register(r'marcas', MarcaViewset)



urlpatterns = [
    #partes vitales del proyecto
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('test/', Appi.test, name="testeo"),

    #vistas de la pagina de los CRUD de los modelos
    path('manager/categorias/',                     Appi.menuCategorias,                            name="categorias"),


    path('manager/tipo_de_producto/',               Appi.menuTipoProducto,                          name="tipoproducto"),


    path('manager/subcategorias/',                  Appi.menuSubcategorias,                         name="subcategorias"),


#Vistas para los clientes
    path('',                                 Clientes.inicio,                                name="clientesinicio")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







 



















"""
URL configuration for Proyecto_Integracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""