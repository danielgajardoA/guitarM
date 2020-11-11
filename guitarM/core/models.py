from django.db import models

# Create your models here.

class Mantencion(models.Model):
    #id -> numero autoincrementable
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self .nombre

class Tipo_Instrumento(models.Model):
    tipo = models.CharField(max_length=30)
    
    def __str__(self):
        return self .tipo

class Instrumento(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    mantencion = models.ForeignKey(Mantencion, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_Instrumento, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()

    def __str__(self):
        return self .marca
   