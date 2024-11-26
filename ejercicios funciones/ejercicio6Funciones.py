def Login(usuario, contraseña, intentos):
  if usuario == "usuario1" and contraseña == "asdasd":
    return True
  else:
    intentos -= 1
    return False
def Registrarse():
  usuario = input("Ingrese un nuevo nombre de usuario: ")
  contraseña = input("Ingrese una nueva contraseña: ")
  print("Usuario registrado exitosamente.")
intentos = 3
while intentos > 0:
  opcion = input("¿Desea iniciar sesión o registrarse? (iniciar/registrar): ")
  if opcion.lower() == "iniciar":
    while intentos > 0:
      usuario = input("Ingrese su nombre de usuario: ")
      contraseña = input("Ingrese su contraseña: ")
  
      if Login(usuario, contraseña, intentos):
        print("Inicio de sesión exitoso.")
        intentos = 3
        break
      else:
        print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", intentos)
    if intentos == 0:
      print("Demasiados intentos. Acceso denegado.")
      break
  elif opcion.lower() == "registrar":
    Registrarse()
    intentos = 3
  else:
    print("Opción inválida.")
    intentos -= 1
if intentos == 0:
  print("Demasiados intentos. Acceso denegado.")