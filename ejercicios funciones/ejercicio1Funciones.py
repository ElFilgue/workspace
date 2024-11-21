n1=int(input("Dime el primer numero: "))
n2=int(input("Dime el segundo numero: "))
n3=int(input("Dime el tercer numero: "))

def max_de_tres(a,b,c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  elif c > a and c > b:
    return c
mayor = max_de_tres(n1,n2,n3)
print(f"El mayor es: {mayor}")
