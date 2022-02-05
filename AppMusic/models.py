from django.db.models import Model
from django.db.models.fields import CharField, EmailField, DateField, IntegerField

class Banda(Model):
    Nombre_banda = CharField(max_length=40)
    nacimiento_banda = DateField()
    ubicacion = CharField(max_length=30)
    email = EmailField()
    def __str__(self):
        return f'Banda {self.Nombre_banda}, Nacimiento: ({self.nacimiento_banda}), Ubicacion: {self.ubicacion}, Email: {self.email}'

class Integrantes(Model):
    integrantes = CharField(max_length=40)
    especializacion = CharField(max_length=40)
    def __str__(self):
        return f'Integrante: {self.integrantes}, Rol: {self.especializacion}'
    
    
class Album(Model):
    fecha_lanzamiento = DateField()
    nombre_album = CharField(max_length=40)
    canciones = IntegerField()
    def __str__(self):
        return f'Fecha de lanzamiento {self.fecha_lanzamiento}, Nombre del album: {self.nombre_album}, cantidad de canciones : {self.canciones}'

class  Biografia(Model):
    inicios = CharField(max_length=250)
    genero = CharField(max_length=40)
    links_banda = CharField(max_length=50)
    def __str__(self):
        return f'Biografia {self.inicios}, Genero de la banda {self.genero}, Links {self.links_banda}'