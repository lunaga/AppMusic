from django.urls import path
from AppMusic.views import  BandaDetailView, album, album_update, banda_delete, banda_formulario, banda_update, biografia, biografia_delete, biografia_update, busqueda_integrantes, inicio, integrantes, banda, album_formulario, integrantes_formulario, buscar, biografia_add, integrante_delete, album_delete, integrantes_update, BandaCreateView, BandaDeleteView, BandaListView, BandaUpdateView

urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    #path('bandas/', banda, name = 'bandas'),
    path('integrantes/', integrantes, name = 'integrantes_n'),
    path('album/', album, name = 'albumes'),
    path('biografia/', biografia, name = 'biografia'),
    path('biografia/add', biografia_add, name = 'biografia_add'),
    path('bandaformulario/', banda_formulario, name = 'banda_formulario'),
    path('albumformulario/', album_formulario, name= 'album_formulario'),
    path('integrantesformulario/', integrantes_formulario, name= 'integrantes_formulario'),
    path('busquedaintegrantes/', busqueda_integrantes, name= 'busqueda_integrantes'),
    path('busca/', buscar, name= 'buscar'),
    #path('bandas/delete/<id_banda>', banda_delete, name= 'banda_delete'),
    path('integrante/delete/<id_integrante>', integrante_delete, name= 'integrante_delete'),
    path('album/delete/<id_album>', album_delete, name= 'album_delete'),
    path('biografia/delete/<id_biografia>', biografia_delete, name= 'biografia_delete'),
    #path('banda/update/<id_banda>', banda_update, name= 'banda_update'),
    path('album/update/<id_album>', album_update, name= 'album_update'),
    path('integrantes/update/<id_integrantes>', integrantes_update, name= 'integrantes_update'),
    path('biografia/update/<id_biografia>', biografia_update, name= 'biografia_update'),
    path('bandas/', BandaListView.as_view(), name = 'bandas'),
    path('bandas/add', BandaCreateView.as_view(), name = 'banda_add'),
    path('bandas/update/<pk>', BandaUpdateView.as_view(), name= 'banda_update'),
    path('bandas/delete/<pk>', BandaDeleteView.as_view(), name= 'banda_delete'),
    path('bandas/view/<pk>', BandaDetailView.as_view(), name= 'banda_view')
    ]
