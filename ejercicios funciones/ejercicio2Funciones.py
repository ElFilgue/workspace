caracter= input("Dime un caracter: ")
vocales=['a','e','i','o','u']
def es_vocal(caracter):
  if  caracter in vocales:
    return True
  else:
    return False

print(es_vocal(caracter))