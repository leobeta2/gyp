from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=150)
	p_neto = models.IntegerField()
	p_iva = models.IntegerField()
	p_venta = models.IntegerField()
	imagen = models.ImageField(upload_to='imagenes')
	p_web = models.URLField()

"""
class proveedor(models.Model): 
    nombre = models.CharField(max_length=30) 
    domicilio = models.CharField(max_length=50) 
    ciudad = models.CharField(max_length=60) 
    rut = models.CharField(max_length=30) 
    website = models.URLField() 

class cliente(models.Model): 
    nombre = models.CharField(max_length=30) 
    apellidos = models.CharField(max_length=40) 
    email = models.EmailField() 
"""