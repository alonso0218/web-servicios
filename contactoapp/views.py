from django.shortcuts import render,redirect
from .forms import Formulario

from django.core.mail import EmailMessage
# Create your views here.



def contacto (request):
    formulario=Formulario
    if request.method =="POST":
        formulario_contacto=formulario(data=request.POST)#CON ESTE METODO RESCATAOS LA INFORMACION DEL INGRESADA EN EL FORMULARIO por medio del metdo post
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")# con estas instruciones rescatamos lo ingresado en cada campo , nombre , email,contenido
            email=request.POST.get("email")
#con este parametro le indicamos que nos retorne a la url de contacto una confirmacionde el envio del formulario   
            contenido=request.POST.get("contenido")

            email=EmailMessage('mensaje desde app django ',"el usuario con el nombre {}  con la direccion de correo {} te escribe este mensaje:\n \n{}" .format(nombre,email,contenido),"",["oalonso222@gmail.com"],reply_to= [email])
            try:
                email.send()

                return redirect("/contacto/?enviado")#usamos e importamos  redirect para que envie la confirmacion de envio del formulario al url de contacto
            except:
                return redirect("/contacto/?noenviado")

    return render(request,'contacto/contacto.html',{'formulario':formulario})



    #enviar informacion al correo electronico dado o una base de datos proximo video