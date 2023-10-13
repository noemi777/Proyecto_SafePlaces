from django.db import models

# Create your models here.
class Lugar(models.Model):
    name = models.CharField(max_length=70, verbose_name= 'Nombre')
    description = models.CharField(max_length=128, verbose_name='Descripcion')
    state = models.CharField(max_length=70, verbose_name= 'Estado')
    city = models.CharField(max_length=70, verbose_name= 'Ciudad')
    colony = models.CharField(max_length=70, verbose_name= 'Colonia')
    street = models.CharField(max_length=70, verbose_name= 'Calle')
    numberstreet = models.IntegerField (verbose_name= 'Numero de Calle')
    postcode = models.IntegerField( verbose_name= 'Codigo Postal')
    status = models.BooleanField(default=True, verbose_name= 'Status')
    
    class Meta:
        db_table = 'lugares'