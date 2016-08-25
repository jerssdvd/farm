from django.shortcuts import render,redirect
from django.contrib import messages
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json as simplejson
from .models import usuario
from .models import Producto
from .models import Farmaceutico
from .models import Proveedor
from .models import Compra
from .models import Venta
from .models import Factura
from .forms import FProducto
from .forms import FProveedor
from .forms import FormEmpleado
from .forms import FormR
from .forms import FCompra
from .forms import FormFact
from .forms import FVenta

@login_required
def Adlistar(request):
	Medicamento= Producto.objects.all()
	empleadof= Farmaceutico.objects.all()
	proveedorf= Proveedor.objects.all()
	context={
		'Medicamentos':Medicamento,
		'empleados':empleadof,
		'proveedor':proveedorf,
		}
	return render(request,"listar_admin.html",context)

def listar(request):
	Productos=Producto.objects.all()
	Users=usuario.objects.all()
	context={
		'medicinas':Productos,
		'medici':Users,
	}
	return render(request,"listar.html",context)

@login_required
def crearp(request):
	fcrear = FProducto(request.POST or None)
	if(request.method=='POST'):
		if fcrear.is_valid():
			datos = fcrear.cleaned_data
			p = Producto()
			p.Cod=datos.get("Cod")
			p.Nombre=datos.get("Nombre")
			p.Cantidad=datos.get("Cantidad")
			p.Descripcion=datos.get("Descripcion")
			p.PrecioU=datos.get("PrecioU")
			if (p.save()!=True):
				return redirect(Adlistar)
				
	context = {
		'form':fcrear,
	}
	return render(request,"crear.html",context)

@login_required
def com(request):
	Comp=Compra.objects.all()
	contenido = {
		'Compras':Comp,
	}
	return render(request,"Comp.html",contenido)

@login_required
def comprar(request):
	fcompr = FCompra(request.POST or None)
	if(request.method == 'POST'):
		if fcompr.is_valid():
			datos = fcompr.cleaned_data
			c = Compra()
			c.CodCompra=datos.get("CodCompra")
			c.Descripcion=datos.get("Descripcion")
			c.Fecha=datos.get("Fecha")
			c.codProd=datos.get("codProd")
			c.Cantidad=datos.get("Cantidad")
			c.Total = datos.get("Total")
			if c.save()!=True:
				return redirect(com)
	context = {
		'fcom':fcompr,
	}
	return render(request,"Compform.html",context)

@login_required
def IngP(request):
	fcrearp = FProveedor(request.POST or None)
	if(request.method=='POST'):
		if fcrearp.is_valid():
			datos = fcrearp.cleaned_data
			p = Proveedor()
			p.Codigo=datos.get("Codigo")
			p.Nombre=datos.get("Nombre")
			p.Telefono=datos.get("Telefono")
			p.Direccion=datos.get("Direccion")
			if p.save()!=True:
				return redirect(Adlistar)
	context = {
		'formp':fcrearp,
	}
	return render(request,"Proveedor.html",context)

@login_required	
def modificar(request):
	fmod = FProducto(request.POST or None)
	producto = Producto.objects.get(Cod=request.GET['Cod'])
	context={
		'producto':producto,
		'f':fmod,
	}
	fmod.fields["Cod"].initial = producto.Cod
	fmod.fields["Nombre"].initial = producto.Nombre
	fmod.fields["Cantidad"].initial = producto.Cantidad
	fmod.fields["Descripcion"].initial = producto.Descripcion
	fmod.fields["PrecioU"].initial = producto.PrecioU
	
	if request.method == 'POST':
		if fmod.is_valid():
			datos = fmod.cleaned_data
			producto.Cod = datos.get("Cod")
			producto.Nombre = datos.get("Nombre")
			producto.Cantidad = datos.get("Cantidad")
			producto.Descripcion = datos.get("Descripcion")
			producto.PrecioU = datos.get("PrecioU")

			if (producto.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el producto", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el producto", fail_silently=True)
			return redirect(Adlistar)
	return render(request,"modificar.html",context)

@login_required	
def modific(request):
	fmodi = FormEmpleado(request.POST or None)
	farmac = Farmaceutico.objects.get(CodigoF=request.GET['CodigoF'])
	context={
		'farm':farmac,
		'f':fmodi,
	}
	fmodi.fields["CodigoF"].initial = farmac.CodigoF
	fmodi.fields["Nombre"].initial = farmac.Nombre
	fmodi.fields["Apellido"].initial = farmac.Apellido
	fmodi.fields["Telefono"].initial = farmac.Telefono
	fmodi.fields["Direccion"].initial = farmac.Direccion
	fmodi.fields["Fecha_entrada"].initial = farmac.Fecha_entrada
	
	if request.method == 'POST':
		if fmodi.is_valid():
			datos = fmodi.cleaned_data
			farmac.CodigoF = datos.get("CodigoF")
			farmac.Nombre = datos.get("Nombre")
			farmac.Apellido = datos.get("Apellido")
			farmac.Telefono = datos.get("Telefono")
			farmac.Fecha_entrada = datos.get("Fecha_entrada")

			if (farmac.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el empleado", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el empleado", fail_silently=True)
			return redirect(Adlistar)
	return render(request,"modifi.html",context)	
	
def registrar(request):
	f = FormR (request.POST or None)
	context = {
		"Us" : f,
	}
	if f.is_valid():
		user = f.save()
		perfil = usuario()
		perfil.user = user
		datos = f.cleaned_data
		perfil.Codigo= datos.get("Codigo")
		perfil.Nombre = datos.get("Nombre")
		perfil.Apellido = datos.get("Apellido")
		perfil.Telefono = datos.get("Telefono")
		perfil.Direccion = datos.get("Direccion")
		perfil.Tipo = datos.get("Tipo")
		if perfil.save()!=True:
			return redirect(Adlistar)
	return render (request,"registro.html",context)

@login_required
def ingresaremp(request):
	femp= FormEmpleado(request.POST or None)
	if(request.method=='POST'):
		if femp.is_valid():
			datos = femp.cleaned_data
			F = Farmaceutico()
			F.CodigoF=datos.get("CodigoF")
			F.Nombre=datos.get("Nombre")
			F.Apellido=datos.get("Apellido")
			F.Telefono=datos.get("Telefono")
			F.Direccion=datos.get("Direccion")
			F.Fecha_entrada=datos.get("Fecha_entrada")
			if F.save()!=True:
				return redirect(Adlistar)
	context = {
		'formempleado':femp,
	}
	return render(request,"Ingresar.html",context)

@login_required
def eliminar(request):
	clpro = Producto.objects.get(Cod=request.GET['Cod'])
	context = {
		'prod':clpro,
	}

	return render(request,"eliminar.html",context)

@login_required	
def eliminarProducto(request):
	producto = Producto.objects.get(Cod=request.GET['Cod'])
	if producto.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el Producto", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el Producto", fail_silently=True)
	return redirect(Adlistar)

@login_required	
def remover(request):
	elemp = Farmaceutico.objects.get(CodigoF=request.GET['CodigoF'])
	context = {
		'trab':elemp,
	}

	return render(request,"remover_trab.html",context)

@login_required	
def removerEmpleado(request):
	empleado = Farmaceutico.objects.get(CodigoF=request.GET['CodigoF'])
	if empleado.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el farmaceutico", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el farmaceutico", fail_silently=True)
	return redirect(Adlistar)

@login_required	
def certificado(request):
	producto = Producto.objects.get(Cod=request.GET['Cod'])
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Productosetail.pdf"'
	p = canvas.Canvas(response)
	cant=str(producto.Cantidad)
	Nombre="Nombre Del Producto"
	Des="Descripcion Del Producto"
	des1="Cantidad Del Producto"
	p.drawString(100, 650,Nombre)
	p.drawString(190, 650, Des)
	p.drawString(350, 900, des1)
	p.drawString(100, 600, producto.Nombre)
	p.drawString(180, 600, producto.Descripcion)	
	p.drawString(350, 600, cant)	
	p.showPage()
	p.save()
	return response

def About(request):
	return render (request,"Somos.html",{})
	
@login_required	
def editar(request):
	fmod = FProveedor(request.POST or None)
	proveedor = Proveedor.objects.get(Codigo=request.GET['Codigo'])
	context={
		'Prov':proveedor,
		'f':fmod,
	}
	fmod.fields["Codigo"].initial = proveedor.Codigo
	fmod.fields["Nombre"].initial = proveedor.Nombre
	fmod.fields["Telefono"].initial = proveedor.Telefono
	fmod.fields["Direccion"].initial = proveedor.Direccion
	
	if request.method == 'POST':
		if fmod.is_valid():
			datos = fmod.cleaned_data
			proveedor.Codigo = datos.get("Codigo")
			proveedor.Nombre = datos.get("Nombre")
			proveedor.Telefono = datos.get("Telefono")
			proveedor.Direccion = datos.get("Direccion")

			if (proveedor.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el proveedor", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el proveedor", fail_silently=True)
			return redirect(Adlistar)
	return render(request,"editar.html",context)
	
@login_required	
def eliminarP(request):
	elprov = Proveedor.objects.get(Codigo=request.GET['Codigo'])
	context = {
		'Prov':elprov,
	}
	return render(request,"eliminar_prov.html",context)

@login_required	
def eliminarProv(request):
	proveed = Proveedor.objects.get(Codigo=request.GET['Codigo'])
	if proveed.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el proveedor", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el proveedor", fail_silently=True)
	return redirect(Adlistar)

@login_required
def farma(request):
	usuariost= usuario.objects.all()
	context={
			'usuarios':usuariost,
		}
	return render(request,"Farma.html",context)
	

@login_required
def ven(request):
	Ventas=Venta.objects.all()
	contenido = {
		'ventas':Ventas,
	}
	return render(request,"ven.html",contenido)	
	
@login_required
def reg_ventas(request):
	vent=FVenta(request.POST or None)
	if request.method == 'POST':
		if vent.is_valid():
			datos=vent.cleaned_data
			v=Venta()
			v.Code=datos.get("Code")
			v.CodFa=datos.get("CodFa")
			v.Descripcion=datos.get("Descripcion")
			v.CodFact=datos.get("CodFact")
			v.Total=datos.get("Total")
			if v.save()!=True:
				redirect(ven)
	context={
		'Vent':vent
	}
	return render(request,"registrarv.html",context)

@login_required
def listfacturas(request):
	factua=Factura.objects.all()
	context={
		'fact':factua
	}
	return render(request,"viewfact.html",context)

@login_required	
def fact(request):
	formf=FormFact(request.POST or None)
	if(request.method =='POST'):
		if formf.is_valid():
			datos=formf.cleaned_data
			fa=Factura()
			fa.NumF = datos.get("NumF")
			fa.CodP = datos.get("CodP")
			fa.Cantidad = datos.get("Cantidad")
			fa.Subtotal = datos.get("Subtotal")
			if fa.save()!=True:
				redirect(listfacturas)
	contenido={
		'fcfactura':formf
	}
	return render(request,"regfactura.html",contenido)
	
def listweb(request):
	queryset=Producto.objects.all()
	queryset=serializers.serialize('json',queryset)
	return HttpResponse(queryset, content_type='application/json')
	
def listwebj(request):
	medicamentos = Producto.objects.all() 
	mresult = [] 
	mreturn = {}
	for m in medicamentos:
		mresult.append({"Nombre Generico": m.Nombre ,
		"Cantidad": m.Cantidad,
		"Descripcion": m.Descripcion})
	mreturn['Medicamento'] = mresult
	return HttpResponse(simplejson.dumps(mreturn),'application/json')
	
def detail(request):
	factura = Factura.objects.get(NumF=request.GET['CodFact'])
	context ={
		'Fact': factura,
	}
	
	return render(request,"viewFact.html",context)