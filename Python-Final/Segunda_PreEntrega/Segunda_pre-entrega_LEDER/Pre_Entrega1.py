def Registro (Base):
    user = input("Ingrese el nombre de usuario: ")
    contra = input("Ingrese su contraseña: ")
    Base[user]= contra
    #print (Userycontra)
    
def LeerReg(Base):
    print("La base de usuarios y contraseñas es: ")
    for user, contra in Base.items():
        print(f"usuario: {user}  --->  contraseña: {contra}")
            
def Login(Base):
  i = True
  j = True
  while i == True:
    usuario = input("Ingrese su nombre de usuario:  ")
    if usuario in Base:
      i == False
      break
    else:
      print("El usuario no existe")
      i== True

  while j == True:
    contra = input("Ingrese su contraseña:  ")
    if Base[usuario]== contra:
      print(f"Has iniciado sesión como {usuario}")
      j == False
      break
    else:
      print("Contraseña incorrecta!")
      pass