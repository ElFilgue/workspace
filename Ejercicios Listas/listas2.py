#programa que permite crear una lista identica a la primera pero al revés

n=int(input(f"Dígame cuántas palabras tiene la lista: "))
lista=[]

for i in range(0,n):
  palabra=input(f"Dígame la palabra {1+i}: ")
  lista.append(palabra)
print(f"La lista creada es: {lista}")
lista_invertida=reversed(lista)
print(f"La lista inversa es: {lista_invertida}")