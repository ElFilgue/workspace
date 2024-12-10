class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    def describir_restaurante(self):
         print(f"El restaurante se llama {self.nombre_restaurante} y sirve {self.tipo_cocina}.")
    def abrir_restaurante(self):
         print(f"{self.nombre_restaurante} está abierto.")

restaurante = Restaurante("La Cocina del Abuelo", "Comida española")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()