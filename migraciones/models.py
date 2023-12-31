from django.db import models

# Create your models here.

class PrecioHistoricoVehiculos(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True,verbose_name='Fecha')
    modelo = models.TextField(verbose_name='Modelo')
    color = models.CharField(max_length=50,default='Desconocido')
    precio = models.DecimalField(
        null=False,blank=False,decimal_places=2,max_digits=10,verbose_name='Precio')
    # Buena práctica:
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de actualización')