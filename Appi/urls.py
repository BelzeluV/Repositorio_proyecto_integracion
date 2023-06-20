from django.urls import path
from .views import *

urlpatterns = [
    #Vistas de los administradores de la pagina de MusicPro
    path('',                                        inicioBackoffice,                          name="inicioBackoffice"),
    path('categorias/',                             menuCategorias,                            name="categorias"),
    path('tipo_de_producto/',                       menuTipoProducto,                          name="tipoproducto"),
    path('subcategorias/',                          menuSubcategorias,                         name="subcategorias"),
]