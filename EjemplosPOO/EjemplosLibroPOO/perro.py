class Perro:
    """Ejemplo para modelar un perro mediante POO."""
  
    def __init__(self, nombre, edad):
        """Inicializa los atributos nombre y edad."""
        self.nombre = nombre
        self.edad = edad
        
    def sientate(self):
        """Simula a un perro que se sienta en respuesta a una orden."""
        print(f"{self.nombre} se ha sentado.")

    def da_la_vuelta(self):
        """Simula que da la vuelta en respuesta a una orden."""
        print(f"¡{self.nombre} ha dado la vuelta!")

mi_perro = Perro('Tom', 6)
tu_perro = Perro('Jan', 3)

print(f"El nombre de mi perro es {mi_perro.nombre}.")
print(f"Mi perro tiene {mi_perro.edad} años.")
mi_perro.sientate()

print(f"\nEl nombre de tu perro es {tu_perro.nombre}.")
print(f"Tu perro tiene {tu_perro.edad} años.")
tu_perro.da_la_vuelta()
