def segundos_a_hms(segundos):
  horas = segundos // 3600
  minutos = (segundos % 3600) // 60
  segundos_restantes = segundos % 60
  return horas, minutos, segundos_restantes
def hms_a_segundos(horas, minutos, segundos):
  return (horas * 3600) + (minutos * 60) + segundos
while True:
  print("\nMenú:")
  print("1. Convertir a segundos")
  print("2. Convertir a horas, minutos y segundos")
  print("3. Salir")
  opcion = input("Elige una opción: ")
  if opcion == "1":
    horas = int(input("Ingresa las horas: "))
    minutos = int(input("Ingresa los minutos: "))
    segundos = int(input("Ingresa los segundos: "))
    total_segundos = hms_a_segundos(horas, minutos, segundos)
    print(f"Total de segundos: {total_segundos}")
  elif opcion == "2":
    segundos = int(input("Ingresa los segundos: "))
    horas, minutos, segundos_restantes = segundos_a_hms(segundos)
    print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos_restantes}")
  elif opcion == "3":
    print("Saliendo del programa...")
    break
  else:
    print("Opción inválida.")