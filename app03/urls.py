from django.urls import path
from app03.views import inicio,about
#,cursos,estudiantes,profesores,entregables,buscar
from app03 import views

urlpatterns = [
    path('',inicio, name="inicio"),
    #path('pagina-cursos/',cursos,name="cursos"),
    #path('pagina-estudiantes/',estudiantes,name="estudiantes"),
    #path('pagina-profesores/',profesores,name="profesores"),
    #path('pagina-entregables/',entregables,name="entregables"),
    #path('busqueda/',buscar,name="busqueda"),
    #path('buscar/',buscar,name="buscar")

    path('about/',about,name="About"),

    

    path('listar_curso/', views.CursoListView.as_view(), name="MenuCursos"),
    path('crear_crurso/',views.CursoCreateView.as_view(),name="CrearCursos"),
    path('actualizar_curso/<pk>',views.CursoUpdateView.as_view(),name="ActualizarCursos"),
    path('borrar_curso/<pk>',views.CursoDeleteView.as_view(),name="BorrarCursos"),

    path('listar_estudiantes/', views.EstudListView.as_view(), name="MenuEstudiantes"),
    path('crear_estudiantes/',views.EstudCreateView.as_view(),name="CrearEstudiantes"),
    path('actualizar_estudiantes/<pk>',views.EstudUpdateView.as_view(),name="ActualizarEstudiantes"),
    path('borrar_estudiantes/<pk>',views.EstudDeleteView.as_view(),name="BorrarEstudiantes"),

    path('listar_profesores/', views.ProfListView.as_view(), name="MenuProfesores"),
    path('crear_profesores/',views.ProfCreateView.as_view(),name="CrearProfesores"),
    path('actualizar_profesores/<pk>',views.ProfUpdateView.as_view(),name="ActualizarProfesores"),
    path('borrar_profesores/<pk>',views.ProfDeleteView.as_view(),name="BorrarProfesores"),

    path('listar_entregables/', views.EntListView.as_view(), name="MenuEntregables"),
    path('crear_entregables/',views.EntCreateView.as_view(),name="CrearEntregables"),
    path('actualizar_entregables/<pk>',views.EntUpdateView.as_view(),name="ActualizarEntregables"),
    path('borrar_entregables/<pk>',views.EntDeleteView.as_view(),name="BorrarEntregables"),

]

#urlsadicionales = [
#    path('form_cursos_api/',form_cursos_api,name="Form_cursos"),
#]
#urlpatterns += urlsadicionales
