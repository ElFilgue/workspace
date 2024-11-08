#  programa que compruebe si existe o no un valor en el diccionario.
diccionario = {'a': 100, 'b': 200, 'c': 300}
valor = int(input("Dígame un número: "))
if valor in diccionario.values():
    print(f"{valor} está en el diccionario")
else: 
    print(f"{valor} no está en el diccionario")