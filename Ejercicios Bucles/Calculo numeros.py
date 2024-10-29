# Programa para el cálculo de números

n = int(input("¿Cuántos números vas a introducir?"))
numeros = []

for i in range (n):
    numeros.append( float(input(f"Introduce el número {i + 1}: ")))
mayor = max(numeros)
menor = min(numeros)
media = sum(numeros) / n

print (f"El número más pequeño es: {menor}")
print (f"El número más grande es: {mayor}")
print (f"La media de los números introducidos es: {media}")