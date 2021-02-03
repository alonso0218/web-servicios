from django.shortcuts import render,HttpResponse
from blogapp.models import Post,Categoria
# Create your views here.

   
def blog (request):
   posts=Post.objects.all()
   return render(request,'blogapp/blog.html',{'posts':posts})

   
def categoria (request,categoria_id):
   categoria=Categoria.objects.get(id=categoria_id)
   posts=Post.objects.filter(categorias=categoria)#para que nos muestre los post dentro de cada categoria
   return render(request,'blogapp/categoria.html',{'categoria':categoria,'posts':posts})
