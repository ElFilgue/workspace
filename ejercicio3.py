class Usuario:
  def __init__(self, nombre, apellido, edad=None, correo=None, ciudad=None):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.correo = correo
    self.ciudad = ciudad
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

usuario1 = Usuario("Juan", "Pereira", edad=30, correo="juan.pereira@example.com", ciudad="Santiago")
usuario2 = Usuario("Lucas", "Perez", edad=25, ciudad="Barcelona")
usuario3 = Usuario("Pedro", "Sanchez")

usuario1.describir_usuario()
usuario1.saludar_usuario()

usuario2.describir_usuario()
usuario2.saludar_usuario()

usuario3.describir_usuario()
usuario3.saludar_usuario()