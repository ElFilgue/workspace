class restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
         self.nombre_restaurante = nombre_restaurante
         self.tipo_cocina = tipo_cocina
    def describir_restaurante(self):
         print(f"El restaurante se llama {self.nombre_restaurante} y sirve {self.tipo_cocina}.")
    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto.")
restaurante1 = restaurante("La Cocina del Abuelo", "Comida española")
restaurante2 = restaurante("El Rinconcito Mexicano", "Comida mexicana")
restaurante3 = restaurante("Sushi Bar Tokio", "Comida japonesa")

restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()