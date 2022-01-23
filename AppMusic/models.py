from django.db.models import Model
from django.db.models.fields import CharField, EmailField, DateField, IntegerField

class Banda(Model):
    Nombre_banda = CharField(max_length=40)
    nacimiento_banda = DateField()
    ubicacion = CharField(max_length=30)
    email = EmailField()


class Integrantes(Model):
    integrantes = CharField(max_length=40)
    especializacion = CharField(max_length=40)
    
    
class Album(Model):
    fecha_lanzamiento = DateField()
    nombre_album = CharField(max_length=40)
    canciones = IntegerField()
    

class  Biografia(Model):
    inicios = CharField(max_length=250)
    genero = CharField(max_length=40)
    links_banda = CharField(max_length=50)