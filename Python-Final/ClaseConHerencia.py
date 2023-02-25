class Usuario:
    
    def __init__(self,nombre, apellido,dirección,localidad,provincia):
        
        self.nombre = nombre
        self.apellido = apellido
        self.dirección = dirección
        self.localidad = localidad
        self.provincia = provincia
    
    def __str__(self):
                     
        return f"""
Se ha creado al usuario: {self.nombre} {self.apellido} 
Con domicilio: {self.dirección}, {self.localidad},{self.provincia}
"""  
    
    def Registrar_usuario(self):
        self.nombre = input("Ingrese su nombre:")
        self.apellido = input("Ingrese su apellido:")
        self.dirección = input ("Dirección para envíos:")
        self.localidad = input ("Localidad:")
        self.provincia = input ("Provincia: ")
    
    def Usuario_compras(self, comprar : bool):
        
        if comprar == True:
            self.__class__ = Cliente
        
            return f"El Usuario {self.nombre} {self.apellido} ahora es un Cliente que va a comprar productos \n"   
          


class Cliente(Usuario):
    
    def __init__(self, nombre, apellido, dirección,localidad, provincia,carrito, pago):
        super().__init__(nombre, apellido, dirección,localidad, provincia)
        self.carrito = carrito
        self.pago = pago
    
    
    
    
    def __str__(self):
        return f"""
El Cliente {self.nombre} {self.apellido}
Compró {self.carrito} productos
Forma de pago: {self.pago}
Envío a: {self.dirección},{self.localidad},{self.provincia}
"""

    def Comprar(self):
        print("Usted es un Cliente:")
        self.carrito = int(input("¿Cuantos productos va a comprar? "))
        self.pago = input("\n¿Qué medio de pago va a utilizar? ")