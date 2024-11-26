def LeerFecha():
  dia = int(input("Ingrese el día: "))
  mes = int(input("Ingrese el mes: "))
  año = int(input("Ingrese el año: "))
  return dia, mes, año
def DiasDelMes(mes, año):
  dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if mes == 2 and Bisiesto(año):
    return 29
  else:
    return dias_del_mes[mes - 1]
def Bisiesto(año):
  return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
def Calcular_Dia_Juliano(dia, mes, año):
  dias_acumulados = 0
  for i in range(1, mes):
    dias_acumulados += DiasDelMes(i, año)
  dias_acumulados += dia
  return dias_acumulados
dia, mes, año = LeerFecha()
dia_juliano = Calcular_Dia_Juliano(dia, mes, año)
print(f"El día juliano correspondiente a la fecha {dia}/{mes}/{año} es: {dia_juliano}")