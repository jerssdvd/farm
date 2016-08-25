from django.db import models
from django.contrib.auth.models import User

class usuario (models.Model):
	TipoU =(
		('U','usuario'),
		('A','administrador'),
	)
	user = models.OneToOneField(User)
	Codigo = models.CharField(max_length=30)
	Nombre = models.CharField(max_length=40)
	Apellido = models.CharField(max_length=50)
	Telefono = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=30)
	Tipo = models.CharField(max_length=15,choices=TipoU)
	
	def __str__(self):
		return self.Codigo

class Farmaceutico (models.Model):
	CodigoF = models.CharField(max_length=30)
	Nombre = models.CharField(max_length=40)
	Apellido = models.CharField(max_length=50)
	Telefono = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=30)
	Fecha_entrada = models.DateField(blank=True,null=True)
	
	def __str__(self):
		return self.CodigoF
		
class Producto (models.Model):
	Cod = models.CharField(max_length=30)
	Nombre = models.CharField(max_length=50)
	Cantidad = models.IntegerField()
	Descripcion = models.CharField(max_length=30)
	PrecioU = models.DecimalField(max_digits=8,decimal_places=2)
	
	def __str__(self):
		return self.Cod

class Factura (models.Model):
	NumF = models.CharField(max_length=30)
	Fecha = models.DateTimeField(auto_now=True,auto_now_add=False)
	CodP = models.ForeignKey(Producto,on_delete=models.CASCADE,default="")
	Cantidad = models.IntegerField()
	Subtotal = models.DecimalField(max_digits=8,decimal_places=2)
	
	def __str__(self):
		return self.NumF
	
class Venta (models.Model):
	Code = models.CharField(max_length=30)
	CodFa = models.ForeignKey(Farmaceutico,on_delete=models.CASCADE,default="")
	Descripcion = models.CharField(max_length=30)
	CodFact = models.ForeignKey(Factura,on_delete=models.CASCADE,default="")
	Total = models.DecimalField(max_digits=8,decimal_places=2)
	
	def __str__(self):
		return self.Code
		
class Proveedor (models.Model):
	Codigo = models.CharField(max_length=30)
	Nombre = models.CharField(max_length=40)
	Telefono = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=40)
	
	def __str__(self):
		return self.Codigo
		
class Compra (models.Model):
	CodCompra = models.CharField(max_length=30)
	Descripcion = models.CharField(max_length=30)
	Fecha = models.DateField(blank=True,null=True)
	codProd = models.ForeignKey(Producto,on_delete=models.CASCADE,default="")
	Cantidad = models.IntegerField()
	Total = models.DecimalField(max_digits=8,decimal_places=2)
	
	def __str__(self):
		return self.CodCompra