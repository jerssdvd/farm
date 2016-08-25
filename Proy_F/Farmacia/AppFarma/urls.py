from django.conf.urls import include,url
from django.contrib import admin
from . import views
from rest_framework import routers
from .viewsets import ProductoViewset

router = routers.DefaultRouter()
router.register(r'producto',ProductoViewset)

urlpatterns = [
	url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio.html'},name='login'),
	url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^listar/$', 'AppFarma.views.listar'),
    url(r'^rest/', include(router.urls)),
    url(r'^listweb/$', 'AppFarma.views.listweb'),
    url(r'^listwebjson/$', 'AppFarma.views.listwebj'),
    url(r'^listaradmin/$', 'AppFarma.views.Adlistar'),
    url(r'^Acerca/$', 'AppFarma.views.About'),
    url(r'^listaradmin/crear/$', 'AppFarma.views.crearp'),
    url(r'^listaradmin/Compras/$', 'AppFarma.views.com'),
    url(r'^listaradmin/Compras/Comprar/$', 'AppFarma.views.comprar'),
    url(r'^listaradmin/Ventas/$', 'AppFarma.views.ven'),
    url(r'^listaradmin/Ventas/venta/$', 'AppFarma.views.reg_ventas'),
    url(r'^listaradmin/Ventas/detalle/$', 'AppFarma.views.detail'),
    url(r'^listaradmin/Ventas/facturas/$', 'AppFarma.views.listfacturas'),
    url(r'^listaradmin/Ventas/facturas/ing/$', 'AppFarma.views.fact'),
    url(r'^listaradmin/certificado/$', 'AppFarma.views.certificado'),
    url(r'^listaradmin/Ingresar/$', 'AppFarma.views.ingresaremp'),
    url(r'^listaradmin/Proveedor/$', 'AppFarma.views.IngP'),
    url(r'^listaradmin/modificar/$', 'AppFarma.views.modificar'),
    url(r'^listaradmin/modific/$', 'AppFarma.views.modific'),
    url(r'^listaradmin/editar/$', 'AppFarma.views.editar'),
    url(r'^listaradmin/eliminar/$', 'AppFarma.views.eliminar'),
    url(r'^listaradmin/eliminarP/$', 'AppFarma.views.eliminarP'),
    url(r'^listaradmin/eliminarProducto/$', 'AppFarma.views.eliminarProducto'),
    url(r'^listaradmin/remover/$', 'AppFarma.views.remover'),
    url(r'^listaradmin/removerEmpleado/$', 'AppFarma.views.removerEmpleado'),
    url(r'^listaradmin/eliminarProveedor/$', 'AppFarma.views.eliminarProv'),
    url(r'^registrar/$', 'AppFarma.views.registrar'),
    url(r'^Farma/$', 'AppFarma.views.farma',name="logeo"),
]