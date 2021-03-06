from django.db import models
from django.db.models.fields import BooleanField, IntegerField
from django.contrib.auth.models import User

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
    capacidad = models.IntegerField()
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
    contacto = models.IntegerField()
    capacidad = models.IntegerField()
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
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT)
    mensaje = models.TextField()

    def __str__(self):
        return str(self.nombre)

class Arriendo(models.Model):
    nombre_cliente = models.CharField(max_length=20)
    apellido_cliente = models.CharField(max_length=20)
    email_cliente = models.EmailField()
    usuario_cliente = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)
    zona = models.CharField(max_length=20)
    cantidad_personas = models.IntegerField()
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    precio = models.IntegerField()
    precio_final = models.IntegerField()

    def __str__(self):
        return str(self.nombre_cliente)

class ActaIn(models.Model):
    first_name = models.ForeignKey(User, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    tipo =  models.ForeignKey(Tiposervicio, on_delete=models.PROTECT)
    pago = models.BooleanField()
    entrega = models.BooleanField()
    transporte = models.BooleanField()
    descripcion = models.TextField()

class ActaOut(models.Model):
    conforme = models.BooleanField()
    multa = models.BooleanField()
    transporte = models.BooleanField()
    condiciones = models.CharField(max_length=50)
    problemas = models.CharField(max_length=50)
    first_name = models.ForeignKey(User, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    tipo =  models.ForeignKey(Tiposervicio, on_delete=models.PROTECT)

class Pasajero(models.Model):
    nombre_cliente = models.CharField(max_length=20)
    rut_pasajero = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_cliente)

class Pago(models.Model):
    orden_compra = models.CharField(max_length=20)
    tipo_tarjeta = models.CharField(max_length=20)
    numero_tarjeta = models.IntegerField()
    titular_tarjeta = models.CharField(max_length=100)
    expira = models.CharField(max_length=20)
    cvc = models.CharField(max_length=8)
    usuario = models.CharField(max_length=20)

    def __str__(self):
        return str(self.orden_compra)

class Transportes_contrato(models.Model):
    orden_compra = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
