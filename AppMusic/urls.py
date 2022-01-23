from django.urls import path
from AppMusic.views import album, biografia, inicio, integrantes, banda

urlpatterns = [
    path('inicio', inicio, name = 'inicio'),
    path('bandas', banda, name = 'bandas'),
    path('integrantes', integrantes, name = 'integrantes'),
    path('album', album, name = 'album'),
    path('biografia', biografia, name = 'biografia'),
]
