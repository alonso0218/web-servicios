from django.shortcuts import render, HttpResponse
#importamos la classe servicio para poder ver la url de la imagen
from serviciosapp.models import Servicio

# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all() #le indicamos que importe todos los objetos o servicios  de la clase servicio 
    return render(request,'serviciosapp/servicios.html',{"servicios":servicios})
