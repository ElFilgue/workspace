#programa que mde hace una lista con todos los numeros primos hasta el numero que yo le diga

numeroFinal = int(input("Dígame un número: "))
lista_numeros_primos = []

for i in range(2, numeroFinal + 1):
    primos = True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        lista_numeros_primos.append(i)

            
print(f"Primos hasta el {numeroFinal}", end=(": ")) 
print(lista_numeros_primos)

