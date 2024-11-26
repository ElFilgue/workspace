def mcd(a, b):

  while b != 0:
    a, b = b, a % b
  return a
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
mcd_result = mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd_result}")