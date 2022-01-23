from pipes import Template
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader

from .models import Banda

# def inicio(request):
#     return HttpResponse('Pagina de inicio')

# lista_temas = ('Aventurero', 'Sola', 'Juegos Prohinibidos', 'Sincerar', 'No Le Da', 'Solitario', 'Otro Dia', 'Soltar', 'Mas Que Maldad', 'Corchazo')


# def t_inicio(request):
#     diccionario = {'nombre' : 'ROMPIENDO HABITOS',
#                    'genero' : 'Rock Alternativo',
#                    'album' : 'Dos Caras',
#                    'temas' : lista_temas,
#     }
    # template_html = open('ProjectMusic\\templates\\template.html')
    # template = Template(template_html.read())
    # template_html.close()
    # # contexto = Context(diccionario)
    
#     template = loader.get_template('template.html')
#     documento = template.render(diccionario)
#     return HttpResponse(documento)

# def banda(request):
#     banda = Banda(Nombre_banda= 'Rompiendo Habitos',  ubicacion='Argentina', email='rhabitos@gmail.com')
#     banda.save()
#     return HttpResponse (f'banda ingresada: {Nombre_banda}, {ubicacion}, {email}')

def inicio(request):
    return render(request, 'AppMusic/inicio.html')

def banda(request):
    return render(request, 'AppMusic/bandas.html')

def integrantes(request):
    return render(request, 'AppMusic/integrantes.html')

def album(request):
    return render(request, 'AppMusic/album.html')

def biografia(request):
    return render(request, 'AppMusic/biografia.html')