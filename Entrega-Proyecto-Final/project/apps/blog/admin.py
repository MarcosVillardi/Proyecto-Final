from django.contrib import admin
from . import models
@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni','fecha_llegada','fecha_salida','numero_habitacion','comentarios')
    search_fields = ('nombre','apellido','dni')
    list_filter = ('fecha_llegada','fecha_salida')
    ordering = ("numero_habitacion",)

@admin.register(models.Garaje)
class GarajeAdmin(admin.ModelAdmin):
    list_display = ('nombre','titular','direccion','capacidad','patente','modelo','comentarios')
    search_fields = ('titular','modelo')
    ordering = ("patente",)