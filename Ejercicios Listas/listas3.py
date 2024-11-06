

n=int(input(f"Dígame cuántas palabras tiene la lista: "))
lista=[]

for i in range(0,n):
  palabra=input(f"Dígame la palabra {1+i}: ")
  lista.append(palabra)
print(f"La lista creada es: {lista}")
lista_ordenada=list(sorted(lista))
print(f"La lista ordenada es: {lista_ordenada}")