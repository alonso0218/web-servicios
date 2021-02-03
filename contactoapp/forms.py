from django import forms

class Formulario(forms.Form):

    nombre=forms.CharField(label='NOMBRE',required=True)
    
    email=forms.CharField(label='EMAIL',required=True)
    contenido=forms.CharField(label='CONTENIDO',widget=forms.Textarea)#le indicamos nos agregue el campo o area para comentarios 

    
