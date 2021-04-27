from django.db import models
from django.contrib.auth.models import User #importamos esta clase para poder manejar varios usuarios en nuestro blog
# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now=True)#nos ayuda a dar la fecha de ingres0
    update=models.DateTimeField(auto_now=True)#nos ayuda a dar la fecha de cambios

#creamos dentro de la clase otra sub clase llamada meta
# que nos ayudara a dar otras caracteisticas a la clase principal en este caso como la buscamos en la base de datos
    class Meta:
        verbose_name ='categoria'
        verbose_name_plural ='categorias'

    #esta funcion nos ayuda a devolver el nombre del blog que solicitemos   
    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog',null=True,blank=True)#con null o blank le indicamos que es opcinal la foto
    autor=models.ForeignKey(User,on_delete = models.CASCADE)#con esta instrucion le idicamos que se borren sus entradas cuando el usuario es eliminado
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now=True)#nos ayuda a dar la fecha de ingreso
    update=models.DateTimeField(auto_now=True)#nos ayuda a dar la fecha de cambios


    class Meta:
       verbose_name ='post'
       verbose_name_plural ='posts'

    def __str__(self):
        return self.titulo
