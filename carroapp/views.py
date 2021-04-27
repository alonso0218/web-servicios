from django.shortcuts import render
from .carro import Carro
from tiendaapp.models import Producto
from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('tienda') 


def eliminar(request,product_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('tienda')

def restar(request,product_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('tienda')

def limpiar_carro(request,eliminar):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect('tienda')