from django.db import models

# Create your models here.

class Autos(models.Model): # AUTOS A REPARAR
    marca= models.CharField(max_length=30, help_text="marca del auto")
    modelo= models.CharField(max_length=30, help_text="modelo del auto")
    reparacion= models.CharField(max_length=600, default='',help_text="reparacion")
    precio= models.IntegerField(default=1, help_text="precio de reparacion o presupuesto") 

class Mecanicos(models.Model): # MECANICOS DISPONIBLES
    nombre= models.CharField(max_length=30, help_text="nombre del mecanico")
    apellido= models.CharField(max_length=30, help_text="apellido del mecanico")
    especializacion= models.CharField(max_length=150, help_text="especializacion del mecanico")
    
class Piezas(models.Model): # PIEZAS EN STOCK PARA REPARACIONES
    nombre= models.CharField(max_length=30, help_text="nombre de la pieza")
    precio= models.IntegerField(default=1, help_text="precio de la pieza")
    cantidad= models.IntegerField(default=1, help_text="cantidad de piezas")