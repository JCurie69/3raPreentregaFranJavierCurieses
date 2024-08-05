from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    comision=models.IntegerField()

    def __str__(self):
        return f"Nombre Curso: {self.nombre} - Nro. Comision: {self.comision}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - email: {self.email}"
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)
    domicilio=models.CharField(max_length=30,null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - email: {self.email} - profesion: {self.profesion} - Domiciolio: {self.domicilio}"

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_de_entrega=models.DateField()
    entregado=models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha: {self.fecha_de_entrega} - Entregado: {self.entregado}"
