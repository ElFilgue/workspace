# juego de adivinar un numero

import random
valor_minimo = int(input("Introduce el valor mínimo: "))
valor_maximo = int(input("Introduce el valor máximo: "))
secreto = random.randint(valor_minimo,valor_maximo)
print("El número secreto está entre",valor_minimo,"y",valor_maximo)
