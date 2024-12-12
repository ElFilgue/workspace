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

class Administrador(Usuario):
  
  def __init__(self, nombre, apellido, correo, edad):

    super().__init__(nombre, apellido, correo, edad)
    self.privilegios = ["puede añadir comentario", "puede borrar comentario", "puede vetar usuarios"]
  def muestra_privilegios(self):
    print(f"El administrador es: {self.nombre} {self.apellido}")
    print(f"Privilegios como administrador:")
    for privilegio in self.privilegios:
      print(f"- {privilegio}")

admin = Administrador("Lucas", "Martinez", "lucasm7@gmail.com", "37" )

admin.muestra_privilegios()