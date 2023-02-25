from ClaseConHerencia import *


#Cliente.Registrar()


persona1 = Usuario("Abel","Leder","lambare 700","CABA","CABA")
persona2 = Usuario("Jose","Sosa","Mitre 526","San Miguel","Buenos Aires")



persona1.Registrar_usuario()
persona2.Registrar_usuario()

print(persona1)
print(persona2)

persona1.Usuario_compras(True)
persona1.Comprar()

print(persona1)

print(persona2)

