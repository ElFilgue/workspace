alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']


def codifica(texto_plano, desplazamiento):  
  texto_cifrado = ""
  for letra in texto_plano:
    position = alfabeto.index(letra)
    nueva_posicion = position + desplazamiento
    nueva_letra = alfabeto[nueva_posicion]
    texto_cifrado += nueva_letra
  print(f"El texto codificado es {texto_cifrado}")

def decodifica(texto_codificado, desplazamiento):
  texto_plano = ""
  for letra in texto_codificado:
    posicion = alfabeto.index(letra)
    nueva_posicion = posicion - desplazamiento
    texto_plano += alfabeto[nueva_posicion]
  print(f"El texto decodificado es {texto_plano}")

direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))

if direccion == "codifica":
  codifica(texto, desplazam)
elif direccion == "decodifica":
  decodifica(texto, desplazam)
  
#TODO-1: Combina las funciones codifica() y decodifica() en una única función llamada cesar(). 
#TODO-2: Llama a la función cesar(), pasando los valores 'texto', 'desplazam' y 'direccion'.
