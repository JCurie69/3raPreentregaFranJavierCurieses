from django.urls import path

from app03.views import inicio,cursos,estudiantes,profesores,entregables,buscar
#,form_cursos_api
#o from app03.views import *


urlpatterns = [
    #path('inicio/',inicio),
    path('',inicio, name="inicio"),
    path('pagina-cursos/',cursos,name="cursos"),
    path('pagina-estudiantes/',estudiantes,name="estudiantes"),
    path('pagina-profesores/',profesores,name="profesores"),
    path('pagina-entregables/',entregables,name="entregables"),
    path('busqueda/',buscar,name="busqueda"),
    path('buscar/',buscar,name="buscar")
]

#urlsadicionales = [
#    path('form_cursos_api/',form_cursos_api,name="Form_cursos"),
#]
#urlpatterns += urlsadicionales
