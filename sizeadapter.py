import os
from PIL import Image

def recortar_imagenes_en_carpeta(carpeta):
    archivos = os.listdir(carpeta)

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)

        if os.path.isfile(ruta_archivo) and archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            imagen = Image.open(ruta_archivo)
            imagen_ancho, imagen_alto = imagen.size
            nuevo_ancho = imagen_alto * 21 // 9
            recorte_ancho = (imagen_ancho - nuevo_ancho) // 2
            recorte_alto = 0
            recortado_ancho = imagen_ancho - (recorte_ancho * 2)
            recortado_alto = imagen_alto - (recorte_alto * 2)
            imagen_recortada = imagen.resize((recortado_ancho, recortado_alto))

            nombre_archivo_recortado = "recortado_" + archivo
            ruta_archivo_recortado = os.path.join(carpeta, nombre_archivo_recortado)
            imagen_recortada.save(ruta_archivo_recortado)

            # Eliminar la imagen original
            os.remove(ruta_archivo)

    print("Recorte de todas las imágenes en la carpeta completado.")

recortar_imagenes_en_carpeta(r"C:\Users\Belz-Sama\Documents\GitHub\Proyectos Django\Repositorio_Proyecto_Integracion\static\images\carusel")