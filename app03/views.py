from django.shortcuts import render
from django.http import HttpResponse
from app03.models import Curso
from app03.forms import CursoFormulario

from .models import Curso


# Create your views here.

def inicio(request):

    return render(request, "app03/inicio.html")

#def cursos(request):
#    cursos01= Curso.objects.all()
#    return render(request, "app03/cursos.html",{"cursoscontex":cursos01})

def estudiantes(request):
    return render(request, "app03/estudiantes.html")

def profesores(request):
    return render(request, "app03/profesores.html")

def entregables(request):
    return render(request, "app03/entregables.html")  

def cursos(request):
    if request.method == "POST":
        mi_formulario=CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            curso=Curso(nombre=informacion["curso"],comision=informacion["comision"])
            curso.save()
            
            return render(request,"app03/inicio.html")
    else:
       
        mi_formulario=CursoFormulario()
    return render(request,"app03/cursos.html", {"mi_formulario":mi_formulario})

def buscar (request):
    if request.GET["comision"]:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision__icontains=comision)

        return render(request,"app03/busqueda.html",{"cursos":cursos,"comision":comision})
    
    else:

        respuesta="No enviaste datos"

    return HttpResponse(respuesta)

def busquedacomision(request):
    return render(request, "app03/busqueda.html")

    


