#-*- coding: utf-8 -*-

from django.db import models

class Articulo(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	publicado = models.BooleanField(default=False)
	precio_ma = models.FloatField(null =True, blank = True)#uno es para el campo y otro para formulario
	precio_mi = models.FloatField(null = True, blank = True)
	publicado_ma = models.BooleanField(default=False)
	publicado_mi = models.BooleanField(default=False)


	def __unicode__(self):
		return self.nombre #pongo que quiero que se muestre
   
class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	publicada = models.BooleanField(default=False)
	articulos = models.ManyToManyField(Articulo)

	def __unicode__(self):
		return self.nombre #pongo que quiero que se muestre
