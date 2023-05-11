import requests

base = "http://localhost:8000/api/"

class consultasSubcategorias():
    productos = "subcategorias/"

    def generate_request(Url):
        response = requests.get(base+Url).json()
        subcategorias = []
        if response:
            for subcategoria in response:
                id_subcategoria = subcategoria["id_subcategoria"]
                nombre_subcategoria = subcategoria["nombre_subcategoria"]
                categoria = subcategoria["categoria"]
                subcategoria_dict = {
                    "id_subcategoria": id_subcategoria,
                    "nombre_subcategoria": nombre_subcategoria,
                    "categoria": categoria
                }
                subcategorias.append(subcategoria_dict)
            return subcategorias
        else:
            return response