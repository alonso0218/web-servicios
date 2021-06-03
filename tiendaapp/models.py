from django.db import models

# Create your models here.

class Categoria_Producto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:#esta clase nos ayuda a identificarnos en nuestra base de datos
        verbose_name="Categoria_Producto"
        verbose_name_plural="Categorias_Productos"
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True,default='tienda')
    precio=models.DecimalField(max_digits=10,decimal_places=6)
    disponibilidad=models.BooleanField(default=True)
    contenido=models.CharField(max_length=1000) 
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
      

    def __str__(self):
        return self.nombre
