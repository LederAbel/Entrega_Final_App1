from django import forms
from App1.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App1.models import Avatar

class Cliente_Formulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    direccion = forms.CharField()
    localidad = forms.CharField()
    provincia = forms.CharField()
    pais = forms.CharField()
    
#choice Envio
opcionesEnvio= (("1", "Si"),
        ("2", "No") )

class Reparacion_Formulario(forms.Form):
    modelo = forms.CharField()
    efecto = forms.CharField()
    fabricante = forms.CharField()
    volts = forms.CharField()
    origen = forms.CharField()
    falla = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':50}))
    envio = forms.ChoiceField(choices=opcionesEnvio)
    
    
class StockPropio_Formulario(forms.Form):
    modelo = forms.CharField()
    efecto = forms.CharField()
    unidades = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':50}))
    precio = forms.CharField()
    

class UsuarioRegistro(UserCreationForm):
    
    email = forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email","first_name","last_name","password1","password2"]

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        
        model = Avatar
        fields = ["imagen"]