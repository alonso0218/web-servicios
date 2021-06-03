from django.contrib import admin
from .models import Servicio#de models importamos la clase creada servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):#con esto registramos los campos de update y created 
    readonly_fields=('created','update')

admin.site.register(Servicio,ServicioAdmin)#aqui registramos la aplicacion y la clase anterior en la administracion de django