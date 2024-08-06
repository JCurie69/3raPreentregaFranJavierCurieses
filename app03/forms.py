from django import forms

class CursoFormulario(forms.Form):
    curso=forms.CharField()
    comision=forms.IntegerField()

class ProfeFromulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField(required=False)
    profesion=forms.CharField()
    domicilio=forms.CharField()

class EstudFromulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField(required=False)
    domicilio=forms.CharField()

class EntregableFormulario(forms.Form):
    nombre=forms.CharField()
    fecha_de_entrega=forms.DateField()
    entregado=forms.BooleanField()




    