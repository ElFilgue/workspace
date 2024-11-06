#Programa que me dice todos los numeros primos hasta el numero que yo le diga

n=int(input("Dígame un número: "))
lista = []

for i in range(1,n+1):
  if i%2!=0:
    lista.append(i)
print(f"Pares hasta el: {lista}")
  