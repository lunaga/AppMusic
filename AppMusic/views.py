from pipes import Template
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppMusic.forms import BandaForm, AlbumForm, IntegrantesForm

from AppMusic.models import Banda, Album, Integrantes, Biografia

def inicio(request):
    return render(request, 'AppMusic/inicio.html')

def banda(request):
    return render(request, 'AppMusic/bandas.html', 
    {'bandas': Banda.objects.all()})

def integrantes(request):
    return render(request, 'AppMusic/integrantes.html',
    {'integrantes': Integrantes.objects.all()})

def album(request):
    return render(request, 'AppMusic/album.html',
    {'albumes': Album.objects.all()})

def biografia(request):
    return render(request, 'AppMusic/biografia.html',
    {'biografia': Biografia.objects.all()})

def banda_formulario(request):
    if request.method == 'POST':
        formulario = BandaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Banda.objects.create(Nombre_banda=data ['Nombre_banda'], nacimiento_banda=data ['nacimiento_banda'], ubicacion=data['ubicacion'], email=data['email'])
            return redirect('bandas')
    else:
        formulario = BandaForm()
    return render(request, 'AppMusic/bandaformulario.html', {'formulario' : formulario})

def album_formulario(request):
    if request.method == 'POST':
        formulario = AlbumForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Album.objects.create(fecha_lanzamiento=data ['fecha_lanzamiento'], nombre_album=data ['nombre_album'], canciones=data['canciones'])
            return redirect('album')
    else:
        formulario = AlbumForm()
    return render(request, 'AppMusic/albumformulario.html', {'formulario' : formulario})

def integrantes_formulario(request):
    if request.method == 'POST':
        formulario = IntegrantesForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Integrantes.objects.create(integrantes=data ['integrantes'], especializacion=data ['especializacion'])
            return redirect('integrantes_n')
    else:
        formulario = IntegrantesForm()
    return render(request, 'AppMusic/integrantesformulario.html', {'formulario' : formulario})


def busqueda_integrantes(request):
    return render(request, 'AppMusic/busquedaintegrantes.html')

def buscar(request):
    especializacion = request.GET["especializacion"]
    
    if especializacion:
        integrantes = Integrantes.objects.filter(especializacion = especializacion)
         
        return render(request, 'AppMusic/buscar.html', 
            {'integrantes' : integrantes, 'especializacion' : especializacion})
    else:
        return HttpResponse ('No hay sierta especializacion en esta banda')
 