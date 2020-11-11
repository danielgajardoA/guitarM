from django.urls import path
from .views import home, galeria, listado_instrumento, nuevo_instrumento, modificar_instrumento, eliminar_instrumento,registro_usuario

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-instrumento/', listado_instrumento, name="listado de instrumentos"),
    path('nuevo-instrumento/', nuevo_instrumento, name="nuevo instrumento"),
    path('modificar-instrumento/<id>/', modificar_instrumento, name="modificar instrumento"),
    path('eliminar-instrumento/<id>/',eliminar_instrumento, name="eliminar instrumento"),
    path('registro/', registro_usuario, name='registro de usuario'),
]