import email
from django.forms import Form, IntegerField, CharField, DateField, EmailField, ImageField

from AppMusic.models import Integrantes

class BandaForm(Form):
    Nombre_banda = CharField()
    nacimiento_banda = DateField()
    ubicacion = CharField()
    email = EmailField()

class AlbumForm(Form):
    fecha_lanzamiento = DateField()
    nombre_album = CharField()
    canciones = IntegerField()

class IntegrantesForm(Form):
    integrantes = CharField ()
    especializacion = CharField()
    
class BiografiaForm(Form):
    inicios = CharField()
    genero = CharField()
    links_banda = CharField()
    
class AvatarFormulario(Form):
    image = ImageField(required=True)
    