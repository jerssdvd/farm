from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import usuario
from .models import Producto
from .models import Proveedor
from .models import Farmaceutico
from .models import Factura
from .models import Compra
from .models import Venta

class FormR(UserCreationForm):
	TipoU =(
		('U','usuario'),
		('A','administrador'),
	)
	Codigo = forms.IntegerField()
	Nombre = forms.CharField(max_length=40)
	Apellido = forms.CharField(max_length=50)
	Telefono = forms.CharField(max_length=10)
	Direccion = forms.CharField(max_length=30)
	Tipo = forms.ChoiceField(
		required=True,
        choices=TipoU,
    ) 

class FProducto(forms.ModelForm):
	class Meta:
		model=Producto
		fields=["Cod","Nombre","Cantidad","Descripcion","PrecioU"]

class FormEmpleado(forms.ModelForm):
	class Meta:
		model=Farmaceutico
		fields=["CodigoF","Nombre","Apellido","Telefono","Direccion","Fecha_entrada"]
		
class FProveedor(forms.ModelForm):
	class Meta:
		model=Proveedor
		fields=['Codigo','Nombre','Telefono','Direccion']	
		
class FCompra(forms.ModelForm):
	class Meta:
		model= Compra
		fields = ['CodCompra','Descripcion','Fecha','codProd','Cantidad','Total']
		
class FormFact(forms.ModelForm):
	class Meta:
		model=Factura
		fields= ['NumF','CodP','Cantidad','Subtotal']
		
class FVenta(forms.ModelForm):
	class Meta:
		model = Venta
		fields = ['Code','CodFa','Descripcion','CodFact','Total']