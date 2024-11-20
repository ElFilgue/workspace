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

#TODO-1: Crea una función diferente llamada 'decodifica' que coja el 'texto' y 'desplazam' como entradas.

  #TODO-2: Dentro de la función 'decodifica', desplaza cada letra del 'texto' *hacia atrás* en el alfabeto la cantidad desplazam e imprime el texto decodificado.  
  #ejemplo
  #texto_cifrado = "mtpf"
  #desplazam = 5
  #texto_plano = "hola"
  #imprime la salida: "El texto decodificado es hola"


#TODO-3: Comprueba si el usuario quería codificar o decodificar comprobando la variable 'direccion'. 
# Entonces llama a la función correcta dependiendo de la variable 'direccion'. 
# Deberías ser capaz de comprobar el código tanto para codificar como para decodificar un mensaje.

direccion = input("Escribe 'codifica' para codificar o 'decodifica' para descodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))

codifica(texto, desplazam)