from django.contrib import admin
from .models import Categoria_Producto,Producto
# Register your models here.

class Categoria_ProductoAdmin(admin.ModelAdmin):# creamos esta clase para los modelos de crated y update sean de solo lectura
    readonly_fields=("created","update")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")


admin.site.register(Categoria_Producto,Categoria_ProductoAdmin)
admin.site.register(Producto, ProductoAdmin)