from dataclasses import field
from msilib.schema import Class
from multiprocessing import context
from pipes import Template
from re import template
from sre_constants import SUCCESS
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.urls import reverse_lazy
from AppMusic.forms import BandaForm, AlbumForm, IntegrantesForm, BiografiaForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppMusic.models import Banda, Album, Integrantes, Biografia

@login_required
def inicio(request):
    return render(request, 'AppMusic/inicio.html')

@login_required
def banda(request):
    return render(request, 'AppMusic/bandas.html', 
    {'bandas': Banda.objects.all()})

@login_required
def integrantes(request):
    return render(request, 'AppMusic/integrantes.html',
    {'integrantes': Integrantes.objects.all()})

@login_required
def album(request):
    return render(request, 'AppMusic/album.html',
    {'albumes': Album.objects.all()})

@login_required
def biografia(request):
    return render(request, 'AppMusic/biografia.html',
    {'biografia': Biografia.objects.all()})

#Bloque de formularios y altas!

def biografia_add(request):
    if request.method == 'POST':
        formulario = BiografiaForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Biografia.objects.create(inicios=data['inicios'], genero=data['genero'], links_banda=data['links_banda'])
            return redirect('biografia')
    else:
        formulario = BiografiaForm()
    return render(request, 'AppMusic/bandaformulario.html', {'formulario' : formulario})

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
            return redirect('albumes')
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

#Bloque de busqueda!

def busqueda_integrantes(request):
    return render(request, 'AppMusic/busquedaintegrantes.html')

def buscar(request):
    especializacion = request.GET["especializacion"]
    
    if especializacion:
        integrantes = Integrantes.objects.filter(especializacion = especializacion)
         
        return render(request, 'AppMusic/buscar.html', 
            {'integrantes' : integrantes, 'especializacion' : especializacion})
    else:
        return HttpResponse ('No hay dicha especializacion en esta banda')


#Bloque de delete!
 
def banda_delete(request, id_banda):
    banda = Banda.objects.get(id=id_banda)
    banda.delete()
    
    return redirect ('bandas')

def integrante_delete(request, id_integrante):
    integrantes = Integrantes.objects.get(id=id_integrante)
    integrantes.delete()
    
    return redirect ('integrantes_n')

def album_delete(request, id_album):
    album = Album.objects.get(id=id_album)
    album.delete()
    
    return redirect ('albumes')

def biografia_delete(request, id_biografia):
    biografia = Biografia.objects.get(id=id_biografia)
    biografia.delete()
    
    return redirect ('biografia')

#Bloque de Modificar!

def banda_update(request, id_banda):
    banda = Banda.objects.get(id=id_banda)
    
    if request.method == 'POST':
        formulario = BandaForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            banda.Nombre_banda=data ['Nombre_banda'] 
            banda.nacimiento_banda=data ['nacimiento_banda'] 
            banda.ubicacion=data['ubicacion'] 
            banda.email=data['email']
            banda.save()
            return redirect('bandas')
    else:
        formulario = BandaForm(model_to_dict(banda))
    return render(request, 'AppMusic/bandaformulario.html', {'formulario' : formulario})
    
    
def album_update(request, id_album):
    album = Album.objects.get(id=id_album)
    
    if request.method == 'POST':
        formulario = AlbumForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            album.fecha_lanzamiento=data ['fecha_lanzamiento']
            album.nombre_album=data ['nombre_album']
            album.canciones=data['canciones']
            album.save()
            return redirect('albumes')
    else:
        formulario = AlbumForm(model_to_dict(album))
    return render(request, 'AppMusic/albumformulario.html', {'formulario' : formulario})

def integrantes_update(request, id_integrantes):
    integrantes = Integrantes.objects.get(id=id_integrantes)
    
    if request.method == 'POST':
        formulario = IntegrantesForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            integrantes.integrantes=data ['integrantes'] 
            integrantes.especializacion=data ['especializacion']
            integrantes.save()
            return redirect('integrantes_n')
    else:
        formulario = IntegrantesForm(model_to_dict(integrantes))
    return render(request, 'AppMusic/integrantesformulario.html', {'formulario' : formulario})

def biografia_update(request, id_biografia):
    biografia = Biografia.objects.get(id=id_biografia)
    
    if request.method == 'POST':
        formulario = BiografiaForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            biografia.inicios=data['inicios']
            biografia.genero=data['genero']
            biografia.links_banda=data['links_banda']
            biografia.save()
            return redirect('biografia')
    else:
        formulario = BiografiaForm(model_to_dict(biografia))
    return render(request, 'AppMusic/bandaformulario.html', {'formulario' : formulario})

#bloque de clases basadas en vistas


class BandaListView(LoginRequiredMixin, ListView):
    model= Banda
    template_name = 'AppMusic/bandas.html'
    context_object_name = 'bandas'
    

class BandaDetailView(DetailView):
    model= Banda
    template_name = 'AppMusic/ver_bandas.html'
    
class BandaCreateView(CreateView):
    model= Banda
    success_url = reverse_lazy('bandas')
    fields = ['Nombre_banda','nacimiento_banda','ubicacion','email'] 
    template_name = 'AppMusic/bandasform.html'
    
class BandaUpdateView(UpdateView):
    model= Banda
    success_url = reverse_lazy('bandas')
    fields = ['Nombre_banda','nacimiento_banda','ubicacion','email']
    template_name = 'AppMusic/bandasform.html'
    
class BandaDeleteView(DeleteView):
    model = Banda
    success_url = reverse_lazy('bandas')
    template_name = 'AppMusic/ver_bandas.html'
    # template name toma como defaul bandas_confirm_delete.html  
    