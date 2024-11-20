alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazamiento = int(input("Escribe un número para el desplazamiento: "))

def cesar(texto_inicial,desplazamiento,direccion):
      def codifica(texto_plano, desplazam, direccion):
     texto_final = ""
     if direccion_cifrado == "descodifica":
        desplazamiento *= -1
     for letra in texto_inicial:
        posicion=alfabeto.index(letra)
        nueva_posición = (posicion + desplazamiento) %27
        texto_final+= alfabeto[nueva_posición]
        print(f"Este ts el resultado de {direccion_cifrado}f: {tecto_final}")
        
        if direccion == 'codifica':
        for letra in texto_cifrado:
                posicion = alfabeto.index(letra)
                indice_posicion = (posicion + desplazam) % 27
                texto_cifrado += alfabeto[indice_posicion]
        print(f"El texto codificado es {texto_cifrado}")
        def codifica(texto_plano, desplazam):
                texto_cifrado = ""
                for letra in texto_plano:
                posicion = alfabeto.index(letra)
                indice_posicion = (posicion + desplazam) % 27
                texto_cifrado += alfabeto[indice_posicion]
                print(f"El texto codificado es {texto_cifrado}")
        
        def descodifica(texto_plano, desplazam):
                texto_cifrado = ""
                for letra in texto_plano:
                        posicion = alfabeto.index(letra)
                        indice_posicion = (posicion - desplazam) % 27
                        texto_cifrado += alfabeto[indice_posicion]
                        print(f"El texto codificado es {texto_plano}")



codifica(texto, desplazam)