from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    numero_habitacion = models.PositiveSmallIntegerField()
    comentarios = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    def __str__(self):
        return f"nombre: {self.nombre},apellido: {self.apellido},DNI: {self.dni},fecha_llegada: {self.fecha_llegada},fecha_salida: {self.fecha_salida},numero_habitacion: {self.numero_habitacion}"
     
class Garaje(models.Model):
    nombre = models.CharField(max_length=50)
    titular = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    capacidad = models.PositiveSmallIntegerField()
    patente = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    comentarios = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name = 'Garaje'
        verbose_name_plural = 'Garajes'
    def __str__(self):
        return self.nombre, self.titular, self.direccion, self.capacidad, self.patente, self.modelo