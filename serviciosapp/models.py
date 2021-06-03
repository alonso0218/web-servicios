from django.db import models
# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now=True)#nos ayuda a dar la fecha de ingres0
    update=models.DateTimeField(auto_now=True)#nos ayuda a dar la fecha de cambios

    class Meta:
        verbose_name ='servicio'
        verbose_name_plural ='servicios'

    def __str__(self):
        return self.titulo

