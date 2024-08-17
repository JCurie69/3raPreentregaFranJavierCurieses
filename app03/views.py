from django.shortcuts import render
from .models import Curso,Estudiante,Profesor,Entregable

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):

    return render(request, "app03/inicio.html")

@login_required
def about(request):
        return render(request, "app03/about.html")

class CursoListView(LoginRequiredMixin,ListView):
    model=Curso
    context_object_name="cursos"
    template_name="app03/menu_cursos.html"

class CursoCreateView(CreateView):
    model=Curso
    template_name="app03/cur_crear.html"
    success_url=reverse_lazy("MenuCursos")
    fields=['nombre','comision']

class CursoUpdateView(UpdateView):
    model=Curso
    template_name="app03/cur_actualizar.html"
    fields=['nombre','comision']
    success_url=reverse_lazy("MenuCursos")
    
class CursoDeleteView(DeleteView):
    model=Curso
    template_name="app03/cur_borrar.html"
    success_url=reverse_lazy("MenuCursos")


class EstudListView(LoginRequiredMixin,ListView):
    model=Estudiante
    context_object_name="estudiantes"
    template_name="app03/menu_estudiantes.html"

class EstudCreateView(CreateView):
    model=Estudiante
    template_name="app03/estud_crear.html"
    success_url=reverse_lazy("MenuEstudiantes")
    fields=['nombre','apellido']

class EstudUpdateView(UpdateView):
    model=Estudiante
    template_name="app03/cur_actualizar.html"
    fields=['nombre','apellido']
    success_url=reverse_lazy("MenuEstudiantes")
    
class EstudDeleteView(DeleteView):
    model=Estudiante
    template_name="app03/estud_borrar.html"
    success_url=reverse_lazy("MenuEstudiantes")


class ProfListView(LoginRequiredMixin,ListView):
    model=Profesor
    context_object_name="profesores"
    template_name="app03/menu_profesores.html"

class ProfCreateView(CreateView):
    model=Profesor
    template_name="app03/prof_crear.html"
    success_url=reverse_lazy("MenuProfesores")
    fields=['nombre','apellido']

class ProfUpdateView(UpdateView):
    model=Profesor
    template_name="app03/prof_actualizar.html"
    fields=['nombre','apellido']
    success_url=reverse_lazy("MenuProfesores")

class ProfDeleteView(DeleteView):
    model=Profesor
    template_name="app03/prof_borrar.html"
    success_url=reverse_lazy("MenuProfesores")


class EntListView(LoginRequiredMixin,ListView):
    model=Entregable
    context_object_name="entregables"
    template_name="app03/menu_entregables.html"

class EntCreateView(CreateView):
    model=Entregable
    template_name="app03/ent_crear.html"
    success_url=reverse_lazy("MenuEntregables")
    fields=['nombre','fecha_de_entrega','entregado']


class EntUpdateView(UpdateView):
    model=Entregable
    template_name="app03/ent_actualizar.html"
    fields=['nombre','fecha_de_entrega','entregado']
    success_url=reverse_lazy("MenuEntregables")

class EntDeleteView(DeleteView):
    model=Entregable
    template_name="app03/ent_borrar.html"
    success_url=reverse_lazy("MenuEntregables")    
