from django.db import models
from django.db.models.fields import BooleanField, IntegerField

# Create your models here.
class Zona(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)
    direccion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField()
    arrendado = models.BooleanField()
    wifi = models.BooleanField()
    cable = models.BooleanField()
    servicioHabitacion = models.BooleanField()
    parking = models.BooleanField()
    piscina = models.BooleanField()
    restaurante = models.BooleanField()
    amueblado = models.BooleanField()
    calefaccion = models.BooleanField()

    def __str__(self):
        return self.nombre

class Tiposervicio(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Servicio(models.Model):
    tipo =  models.ForeignKey(Tiposervicio, on_delete=models.PROTECT)
    descripcion = models.TextField()
    direccion = models.TextField()
    precio = models.IntegerField()
    horaInicio = models.CharField(max_length=50)
    horaCierre = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length=50)
    imagen = models.ImageField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.tipo)

class Transporte(models.Model):
    patente = models.CharField(max_length=50)
    descripcion = models.TextField()
    rutConductor = models.CharField(max_length=50) 
    nombreConductor = models.CharField(max_length=50)
    tipoVehiculo = models.CharField(max_length=50)
    contacto = models.IntegerField
    capacidad = models.IntegerField
    precio = models.IntegerField()
    horaInicio = models.CharField(max_length=50)
    horaCierre = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length=50)
    imagen = models.ImageField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)
    

    def __str__(self):
        return str(self.patente)

class Contacto(models.Model):
    
