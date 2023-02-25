from django.urls import path
from App1.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path("",inicio, name="Inicio"),
    path("login/",InicioSesion, name="Login"),
    path("logout/",LogoutView.as_view(template_name="App1/logout.html"), name="Logout"),
    path("registro/",registro, name="SignIn"),
    path("nvo_cliente/", nuevo_cliente, name="NuevoCliente"),
    path("cliente_formulario/",cliente_formulario, name="FormularioCliente"),
    path("reparacion_formulario/", reparacion, name="FormularioReparacion"),
    path("resultados_stock/", mostrar_resultados ,name="Resultados"),
    path("agregarAvatar/", agregarAvatar, name="Avatar"),
    
    #CRUD StockPropio
    
    path("leer_stockpropio/", leer_stockpropio, name="StockPropio"),
    path("crear_stockpropio/", crear_stockpropio, name="Crear_stockpropio"),
    path("eliminar_stockpropio/<modelopropio>", eliminar_stockpropio, name="Eliminar_stockpropio"),
    path("editar_stockpropio/<modelopropio>", editar_stockpropio, name="Editar_stockpropio"),

    #CRUD Reparaciones usando Class
    path("reparacion/list/", listaReparacion.as_view(), name="ReparacionLeer"),
    path("reparacion/<int:pk>", DetalleReparacion.as_view(), name="ReparacionDetalle"),
    path("reparacion/crear/", CrearReparacion.as_view(), name="ReparacionCrear"),
    path("reparacion/editar/<int:pk>", ActualizarReparacion.as_view(), name="ReparacionActualizar"),
    path("reparacion/borrar/<int:pk>", BorrarReparacion.as_view(), name="ReparacionEliminar"),
]

#Imagen Soyus

urlpatterns += staticfiles_urlpatterns()