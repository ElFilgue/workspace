class Usuario:
  def __init__(self, nombre, apellido, edad=None, correo=None, ciudad=None):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.correo = correo
    self.ciudad = ciudad
    self.intentos_inicio = 0
  def describir_usuario(self):
    print(f"Nombre: {self.nombre}")
    print(f"Apellido: {self.apellido}")
    if self.edad:
      print(f"Edad: {self.edad}")
    if self.correo:
      print(f"Correo: {self.correo}")
    if self.ciudad:
      print(f"Ciudad: {self.ciudad}")
  def saludar_usuario(self):
    print(f"¡Hola {self.nombre} {self.apellido}!")
  def incrementar_intentos_inicio(self):
    self.intentos_inicio += 1
  def restablecer_intentos_inicio(self):
    self.intentos_inicio = 0
usuario = Usuario("Juan", "Pereira")

usuario.incrementar_intentos_inicio()
usuario.incrementar_intentos_inicio()
usuario.incrementar_intentos_inicio()

print(f"Intentos de inicio: {usuario.intentos_inicio}")  

usuario.restablecer_intentos_inicio()

print(f"Intentos de inicio: {usuario.intentos_inicio}")