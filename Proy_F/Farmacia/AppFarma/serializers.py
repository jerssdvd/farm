from rest_framework import serializers
from .models import Producto

class MedicinasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('Cod','Nombre','Cantidad','Descripcion','PrecioU')