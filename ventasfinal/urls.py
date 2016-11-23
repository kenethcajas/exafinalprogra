from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth.views import login

#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [

	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

   
    url(r'^$', views.venta_lista),
    #url(r'^$', views.inicio),
    url(r'^venta/(?P<pk>[0-9]+)/$', views.venta_detalle),
    url(r'^venta/nuevo/$', views.venta_nuevo, name='venta_nuevo'),
    url(r'^venta/(?P<pk>[0-9]+)/edit/$', views.venta_editar, name='venta_editar'),
    url(r'^venta/(?P<pk>\d+)/remove/$', views.venta_eliminar, name='venta_eliminar'),
    url(r'^usuario/$', views.usuario_lista, name='usuario_lista'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.usuario_detalle),
    url(r'^usuario/nueva/$', views.usuario_nueva, name='usuario_nueva'),
    url(r'^usuario/(?P<pk>[0-9]+)/edit/$', views.usuario_editar, name='usuario_editar'),
    url(r'^usuario/(?P<pk>\d+)/remove/$', views.usuario_eliminar, name='usuario_eliminar'),
    url(r'^articulo/$', views.articulo_lista, name='articulo_lista'),
    url(r'^articulo/(?P<pk>[0-9]+)/$', views.articulo_detalle),
    url(r'^articulo/nuevo/$', views.articulo_nuevo, name='articulo_nuevo'),
    url(r'^articulo/(?P<pk>[0-9]+)/edit/$', views.articulo_editar, name='articulo_editar'),
    url(r'^articulo/(?P<pk>\d+)/remove/$', views.articulo_eliminar, name='articulo_eliminar'),





    ]

   