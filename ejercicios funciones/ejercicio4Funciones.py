import math
def area_y_perimetro_circunferencia(radio):
  area = math.pi * radio**2
  perimetro = 2 * math.pi * radio
  return area, perimetro
radio = float(input("Dime el radio de la circunferencia: "))
area, perimetro = area_y_perimetro_circunferencia(radio)
print(f"El área de la circunferencia es: {area:.2f}")
print(f"El perímetro de la circunferencia es: {perimetro:.2f}")