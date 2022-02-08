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
from AppMusic.forms import AvatarFormulario, BandaForm, AlbumForm, IntegrantesForm, BiografiaForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppMusic.models import Avatar, Banda, Album, Integrantes, Biografia

def about(request):
    return render(request, 'AppMusic/about.html')

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else: 
        avatar_url=''
    return render(request, 'AppMusic/inicio.html', {'avatar_url': avatar_url})

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
    {'album': Album.objects.all()})

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
            return redirect('integrantes')
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

#Vistas de Bandas
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
    #template_name = 'AppMusic/ver_bandas.html'
    #template name toma como defaul bandas_confirm_delete.html  
    

#Vistas de Biografia

class BiografiaListView(LoginRequiredMixin, ListView):
    model= Biografia
    template_name = 'AppMusic/biografia.html'
    context_object_name = 'biografia'
    

class BiografiaDetailView(DetailView):
    model= Biografia
    template_name = 'AppMusic/ver_biografia.html'
    
class BiografiaCreateView(CreateView):
    model= Biografia
    success_url = reverse_lazy('biografia')
    fields = ['inicios', 'genero', 'links_banda'] 
    template_name = 'AppMusic/biografiaform.html'
    
class BiografiaUpdateView(UpdateView):
    model= Biografia
    success_url = reverse_lazy('biografia')
    fields = ['inicios', 'genero', 'links_banda']
    template_name = 'AppMusic/biografiaform.html'
    
class BiografiaDeleteView(DeleteView):
    model = Biografia
    success_url = reverse_lazy('biografia')
   


#Bloque de vistas de integrantes

class IntegrantesListView(LoginRequiredMixin, ListView):
    model= Integrantes
    template_name = 'AppMusic/integrantes.html'
    context_object_name = 'integrantes'
    

class IntegrantesDetailView(DetailView):
    model= Integrantes
    template_name = 'AppMusic/ver_integrantes.html'
    
class IntegrantesCreateView(CreateView):
    model= Integrantes
    success_url = reverse_lazy('integrantes')
    fields = ['integrantes', 'especializacion'] 
    template_name = 'AppMusic/integrantesform.html'
    
class IntegrantesUpdateView(UpdateView):
    model= Integrantes
    success_url = reverse_lazy('integrantes')
    fields = ['integrantes', 'especializacion']
    template_name = 'AppMusic/integrantesform.html'
    
class IntegrantesDeleteView(DeleteView):
    model = Integrantes
    success_url = reverse_lazy('integrantes')
    
#Bloque de vistas para Album

class AlbumListView(LoginRequiredMixin, ListView):
    model= Album
    template_name = 'AppMusic/album.html'
    context_object_name = 'album'
    

class AlbumDetailView(DetailView):
    model= Album
    template_name = 'AppMusic/ver_album.html'
    
class AlbumCreateView(CreateView):
    model= Album
    success_url = reverse_lazy('album')
    fields = ['fecha_lanzamiento', 'nombre_album','canciones'] 
    template_name = 'AppMusic/albumform.html'
    
class AlbumUpdateView(UpdateView):
    model= Album
    success_url = reverse_lazy('album')
    fields = ['fecha_lanzamiento', 'nombre_album','canciones']
    template_name = 'AppMusic/albumform.html'
    
class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('album')

#Bloque de Avatar


@login_required    
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('inicio')
            
    else:
        formulario = AvatarFormulario()
    return render(request, 'AppMusic/crear_avatar.html', {'form': formulario})