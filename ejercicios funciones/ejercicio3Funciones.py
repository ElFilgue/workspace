def histograma(numeros):
    for numero in numeros:
        print("*" * numero)
cantidad_numeros = int(input("Dime cuantos numeros quieres poner: "))
numeros=[]
print("Dime los numeros: ")
for i in range(cantidad_numeros):
    numero = int(input(f"Numero {i+1}: "))
    numeros.append(numero)
histograma(numeros)