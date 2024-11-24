def Login(usuario, contraseña, intentos):
  if usuario == "usuario1" and contraseña == "asdasd":
    return True
  else:
    intentos -= 1  
    return False
intentos = 3 
while intentos > 0:
  usuario = input("Ingrese su nombre de usuario: ")
  contraseña = input("Ingrese su contraseña: ")
  
  if Login(usuario, contraseña, intentos):
    print("Inicio de sesión exitoso.")
    break
  else:
    print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", intentos)
if intentos == 0:
  print("Demasiados intentos. Acceso denegado.")