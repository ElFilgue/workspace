#programa que permite crear una lista de palabras

n=int(input(f"Dígame cuántas palabras tiene la lista: "))
lista=[]
for i in range(0,n):
  palabra=input(f"Dígame la palabra {1+i}: ")
  lista.append(palabra)
print(f"La lista creada es: {lista}")
palabra_eliminar=input("Palabra a eliminar: ")
lista.remove(palabra_eliminar)
print(f"La lista es ahora: {lista}")