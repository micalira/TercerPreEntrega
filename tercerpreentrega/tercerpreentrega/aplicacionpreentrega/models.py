from django.db import models

# Modelo de negocio de la aplicacion para la tercer pre entrega para mi emprendimiento de venta de termos TiendaPipi

class tiendaMinorista(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    provincia = models.CharField(max_length=60)
    
class tiendaMayoristas(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()    
    provincia = models.CharField(max_length=60)
    
class ProveedorMercaderia(models.Model) :
    nombre = models. CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    pagina = models.URLField()
    email = models.EmailField()
    producto = models.CharField(max_length=50)
    
class EmpresaEnvio(models.Model) :
    nombre = models. CharField(max_length=60)
    pagina = models.URLField()
    email = models.EmailField() 

class EntregableProducto(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=60)
    empresaenvio = models.CharField(max_length=60)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()