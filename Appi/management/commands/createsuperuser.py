from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from Appi.models import Usuario

class Command(BaseCommand):
    help = 'Crea un superusuario con campos adicionales personalizados'

    def handle(self, *args, **options):
        # create base user using the main class
        super().handle(*args, **options)

        # get the new object 
        username = options.get('username')
        user = Usuario.objects.get(username=username) 

        # Agregar los campos adicionales personalizados al usuario
        user.RUT = options.get('rut')
        user.nombre_real = options.get('nombre_real')
        user.nacimiento = options.get('nacimiento')
        user.genero = options.get('genero')
        user.telefono = options.get('telefono')
        user.Direccion = options.get('Direccion')
        user.comuna = options.get('comuna')
        user.foto_de_Usuario = options.get('foto_de_Usuario')

        # Guardar los cambios en la base de datos
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Se ha creado el superusuario {username}'))