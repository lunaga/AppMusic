from django.urls import path
from AppMusic.views import album, banda_formulario, biografia, busqueda_integrantes, inicio, integrantes, banda, album_formulario, integrantes_formulario, buscar

urlpatterns = [
    path('inicio', inicio, name = 'inicio'),
    path('bandas', banda, name = 'bandas'),
    path('integrantes', integrantes, name = 'integrantes_n'),
    path('album', album, name = 'albumes'),
    path('biografia', biografia, name = 'biografia'),
    path('bandaformulario', banda_formulario, name = 'banda_formulario'),
    path('albumformulario', album_formulario, name= 'album_formulario'),
    path('integrantesformulario', integrantes_formulario, name= 'integrantes_formulario'),
    path('busquedaintegrantes', busqueda_integrantes, name= 'busqueda_integrantes'),
    path('busca', buscar, name= 'buscar'),
]
