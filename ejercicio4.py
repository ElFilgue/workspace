class Restaurante:
  def __init__(self, nombre_restaurante, tipo_cocina):
    self.nombre_restaurante = nombre_restaurante
    self.tipo_cocina = tipo_cocina
    self.numero_servido = 0 
  def describir_restaurante(self):
    print(f"El restaurante se llama {self.nombre_restaurante} y sirve {self.tipo_cocina}.")
  def abrir_restaurante(self):
    print(f"{self.nombre_restaurante} está abierto.")
  def establecer_como_servido(self, numero_clientes):
    self.numero_servido = numero_clientes
  def incrementar_numero_servido(self, numero_clientes):
    self.numero_servido += numero_clientes
restaurante = Restaurante("La Cocina del Abuelo", "Comida española")
print(f"El restaurante {restaurante.nombre_restaurante} ha servido a {restaurante.numero_servido} clientes.")
restaurante.numero_servido = 10

print(f"Ahora ha servido a {restaurante.numero_servido} clientes.")
restaurante.establecer_como_servido(25)
print(f"Después de actualizar el número de clientes servidos, ahora ha servido a {restaurante.numero_servido} clientes.")

restaurante.incrementar_numero_servido(15)
print(f"Después de atender más clientes, ahora ha servido a {restaurante.numero_servido} clientes.")