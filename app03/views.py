from django.shortcuts import render
from django.http import HttpResponse
from app03.models import Curso,Estudiante,Profesor,Entregable
from app03.forms import CursoFormulario,EstudFromulario,ProfeFromulario,EntregableFormulario

from .models import Curso


# Create your views here.

def inicio(request):

    return render(request, "app03/inicio.html")

#def cursos(request):
#    cursos01= Curso.objects.all()
#    return render(request, "app03/cursos.html",{"cursoscontex":cursos01})

def estudiantes(request):
    if request.method == "POST":
        mi_formulario=EstudFromulario(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            estudiante=Estudiante(nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"],domicilio=informacion["domicilio"])
            estudiante.save()
            
            return render(request,"app03/inicio.html")
    else:
       
        mi_formulario=EstudFromulario()
    return render(request,"app03/estudiantes.html", {"mi_formulario":mi_formulario})


def profesores(request):
    if request.method == "POST":
        mi_formulario=ProfeFromulario(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            profesor=Profesor(nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"],profesion=informacion["profesion"],domicilio=informacion["domicilio"])
            profesor.save()
            
            return render(request,"app03/inicio.html")
    else:
       
        mi_formulario=ProfeFromulario()
    return render(request,"app03/profesores.html", {"mi_formulario":mi_formulario})
    #return render(request, "app03/profesores.html")

def entregables(request):
    if request.method == "POST":
        mi_formulario=EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            entreg=Entregable(nombre=informacion["nombre"],fecha_de_entrega=informacion["fecha_de_entrega"],entregado=informacion["entregado"])
            entreg.save()
            
            return render(request,"app03/inicio.html")
    else:
       
        mi_formulario=EntregableFormulario()
    return render(request,"app03/entregables.html", {"mi_formulario":mi_formulario})
    #return render(request, "app03/entregables.html")  

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

    


