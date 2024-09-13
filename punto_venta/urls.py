"""punto_venta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from caja.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='inicio'),
    path('', sigin, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', signout, name='logout'),
    path('negocios/', negocio, name='negocio'),
    path('negocios/crear/', negocio_crear, name='negocio_crear'),
    re_path(r'negocios/editar/(?P<pk>\d+)/$', negocio_editar, name='negocio_editar'),
    re_path(r'negocios/eliminar/(?P<pk>\d+)/$', negocio_eliminar, name='negocio_eliminar'),
    path('marcas/', marca, name='marca'),
    path('marcas/crear/', marca_crear, name='marca_crear'),
    re_path(r'marcas/editar/(?P<pk>\d+)/$', marca_editar, name='marca_editar'),
    re_path(r'marcas/eliminar/(?P<pk>\d+)/$', marca_eliminar, name='marca_eliminar'),
    path('clientes/', cliente, name='cliente'),
    path('clientes/crear/', cliente_crear, name='cliente_crear'),
    re_path(r'clientes/editar/(?P<pk>\d)/$', cliente_editar, name='cliente_editar'),
    re_path(r'clientes/eliminar/(?P<pk>\d)/$', cliente_eliminar, name='cliente_eliminar'),
    path('cajas/', caja, name='caja'),
    path('cajas/crear/', caja_agregar, name='caja_crear'),
    re_path(r'cajas/editar/(?P<pk>\d)/$', caja_editar, name='caja_editar'),
    re_path(r'cajas/eliminar/(?P<pk>\d)/$', caja_eliminar, name='caja_eliminar'),
    path('departamentos/', departamento, name='departamento'),
    path('departamentos/crear/', departamento_crear, name='departamento_crear'),
    re_path(r'departamentos/editar/(?P<pk>\d)/$', departamento_editar, name='departamento_editar'),
    re_path(r'departamentos/eliminar/(?P<pk>\d)/$', departamento_eliminar, name='departamento_eliminar'),
    path('medidas/', medida, name='medida'),
    path('medidas/crear/', medida_crear, name='medida_crear'),
    re_path(r'medidas/editar/(?P<pk>\d)/$', medida_editar, name='medida_editar'),
    re_path(r'medidas/eliminar/(?P<pk>\d)/$', medida_eliminar, name='medida_eliminar'),
    path('productos/', producto, name='producto'),
    path('productos/crear/', producto_crear, name='producto_crear'),
    re_path(r'productos/editar/(?P<pk>\d)/$', producto_editar, name='producto_editar'),
    re_path(r'productos/eliminar/(?P<pk>\d)/$', producto_eliminar, name='producto_eliminar'),
    path('empleados/', empleado, name='empleado'),
    path('empleados/crear/', empleado_crear, name='empleado_crear'),
    re_path(r'empleados/editar/(?P<pk>\d)/$', empleado_editar, name='empleado_editar'),
    re_path(r'empleados/eliminar/(?P<pk>\d)/$', empleado_eliminar, name='empleado_eliminar'),
    re_path(r'cajas/abrir/(?P<pk>\d)/$', abrir_caja, name='caja_abrir'),
    re_path(r'cajas/cerrar/(?P<pk>\d)/$', cerrar_caja, name='caja_cerrar'),
    path('ventas/', venta, name='venta'),
    path('productos/copletar/', autocomplete_producto, name='autocomplete_producto'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)