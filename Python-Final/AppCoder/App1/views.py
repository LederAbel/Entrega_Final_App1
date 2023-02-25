from django.shortcuts import render
from django.http import HttpResponse
import datetime, random 
from App1.models import *
from App1.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#Vistas Registrar Cliente y Reparacion

def InicioSesion(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username= usuario, password=contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "App1/inicio.html", {"mensaje": f"Bienvenido {user}"})
        
        else:
            
            return render(request, "App1/inicio.html", {"mensaje": "Datos incorrectos"})
    
    else:
        
        form = AuthenticationForm()
        
    return render(request, "App1/login.html", {"formulario": form})

def registro(request):
    
    if request.method == "POST":
        
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"App1/inicio.html", {"mensaje":"Usuario Creado"})

    else:
        
        form = UsuarioRegistro()
        
    return render(request, "App1/registro.html", {"formulario": form})
        
def inicio(request):
    
    return render(request, "App1/inicio.html")

def nuevo_cliente(request):
    
    client = Cliente(nombre = "Abel",apellido ="Leder", direccion = "Entre Rios 1191",localidad="Bella Vista",provincia="Buenos Aires",pais="Argentina")
    
    client.save()
    
    return render(request, "App1/nuevo_cliente.html")
    
def cliente_formulario(request):
    
    if request.method == "POST":
        
        formulario1 = Cliente_Formulario(request.POST)
        
        if formulario1.is_valid():
            
            info = formulario1.cleaned_data
            
            cliente = Cliente(nombre=info["nombre"],apellido=info["apellido"],email=info["email"],direccion=info["direccion"],localidad=info["localidad"],provincia=info["provincia"],pais=info["pais"])            
            
            cliente.save()
            return render(request,"App1/inicio.html")
    else:
    
        formulario1= Cliente_Formulario()
    
    return render(request,"App1/cliente_formulario.html",{"form1":formulario1})

def reparacion(request):
     
    if request.method == "POST":
        
        formula1 = Reparacion_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            reparacion = Reparacion(nombre=info["modelo"],efecto=info["efecto"],fabricante=info["fabricante"],volts=info["volts"],origen=info["origen"],cliente=info["cliente"],falla=info["falla"],envio=info["envio"],)            
            reparacion.save()
            return render(request,"App1/inicio.html")
    else:
    
         formula1= Reparacion_Formulario()
    
     
         return render (request,"App1/reparacion_formulario.html",{"form2":formula1})

#Imagenes

@login_required
def agregarAvatar(request):
    
    if request.method=="POST":
        
        form= AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            
            usuarioLogin = User.objects.get(username=request.user)
            
            avatar = Avatar(usuario=usuarioLogin, imagen= form.cleaned_data["imagen"])
            
            avatar.save()
            
            return render(request, "App1/inicio.html")
        
    else:
            form = AvatarFormulario()
            
    return render(request,"App1/agregarAvatar.html",{"formulario":form})
            

# CRUD StockPropio

def leer_stockpropio(request):
    
    pedal = StockPropio.objects.all()
    
    contexto = {"modelopropio": pedal}
    
    return render (request,"App1/pedalespropios.html", contexto)

@login_required
def crear_stockpropio(request): 
    if request.method == "POST":
        
        formula1 = StockPropio_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            modelopropio = StockPropio(modelo=info["modelo"],efecto=info["efecto"],unidades=info["unidades"],descripcion=info["descripcion"],precio=info["precio"])            
            modelopropio.save()
            return render(request,"App1/inicio.html")
    else:
        
         formula1= StockPropio_Formulario()
    
     
         return render (request,"App1/nuevo_stock_propio.html",{"form1":formula1})
 
@login_required   
def eliminar_stockpropio(request,modelopropio):
    
    modelo= StockPropio.objects.get(modelo=modelopropio)
    modelo.delete()
    
    modelo=StockPropio.objects.all()
    contexto={"nombre":modelo}
    
    return render(request,"App1/pedalespropios.html",contexto)
 
@login_required   
def editar_stockpropio(request, modelopropio):
    
    pedalpropio= StockPropio.objects.get(modelo=modelopropio)
    
    if request.method == "POST":
        
        formula1 = StockPropio_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            pedalpropio.modelo= info["modelo"]
            pedalpropio.efecto= info["efecto"]
            pedalpropio.unidades= info["unidades"]
            pedalpropio.descripcion= info["descripcion"]
            pedalpropio.precio= info["precio"]
            pedalpropio.save()
            return render(request,"App1/inicio.html")
    else:
        
         formula1= StockPropio_Formulario(initial={"modelo":pedalpropio.modelo, "efecto":pedalpropio.efecto,
            "unidades":pedalpropio.unidades,"descricion":pedalpropio.descripcion,"precio":pedalpropio.precio})
    
     
         return render (request,"App1/editar_stock_propio.html",{"form1":formula1,"modelo": modelopropio})

# CRUD Reparaciones

class listaReparacion(LoginRequiredMixin, ListView):

    model = Reparacion
    

class DetalleReparacion(LoginRequiredMixin, DetailView):

    model = Reparacion
    
    
class CrearReparacion(LoginRequiredMixin, CreateView):

    model = Reparacion
    success_url = "/App1/reparacion/list"
    fields = ["nombre","efecto","fabricante","volts",
    "made","falla","envio",]

class ActualizarReparacion(LoginRequiredMixin, UpdateView):

    model = Reparacion
    success_url = "/App1/reparacion/list"
    fields = ["nombre","efecto","fabricante","volts",
    "made","falla","envio",]

class BorrarReparacion(LoginRequiredMixin, DeleteView):
    
    model = Reparacion
    success_url = "/App1/reparacion/list"
    


# Esto lo voy a borrar
def mostrar_resultados(request):
    
    if request.GET["modelo"]:
        
        modelo = request.GET["modelo"]
        
        modelos= StockPropio.objects.filter(modelo__icontains=modelo)
        unidades = StockPropio.objects.filter(modelo__icontains=modelo)
        
        return render (request, "App1/resultadostock.html",{"modelos":modelos ,"unidades":unidades})
    else:
        respuesta = "No enviaste datos."
    
    return HttpResponse(respuesta)