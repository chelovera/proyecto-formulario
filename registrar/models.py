from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Registrado(models.Model):
    cedula_de_identidad = models.IntegerField(blank=True, null=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, )
    fecha_nac = models.DateField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    # para python 3 __str__
    def __unicode__(self):
        return str(self.cedula_de_identidad)
