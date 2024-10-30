# juego de adivinar un numero

import random
valor_minimo = int(input("Introduce el valor mínimo: "))
valor_maximo = int(input("Introduce el valor máximo: "))
secreto = random.randint(valor_minimo,valor_maximo)
print(f"A ver si adivinas un número entero entre {valor_minimo} y {valor_maximo}")
intentos = 1
numero= int(input("Escribe un número: "))
while numero != secreto:
    if numero < secreto:
        numero = int(input("¡Demasiado pequeño! Intentalo de nuevo: "))
    else:
        numero = int(input("¡Demasiado alto! Intentalo de nuevo: "))
    intentos += 1
print(f"¡Acertaste! Te ha costado {intentos} intentos")



