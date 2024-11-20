
def max_de_tres(a=1,b=4,c=5):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  elif c > a and c > b:
    return c
print("El mayor es: ", max_de_tres())
