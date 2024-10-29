# Programa que dibuja un rectángulo

anchura = int(input("Dime la anchura de tu rectangulo: "))
altura = int(input("Dime la altura de tu rectangulo: "))
for i in range (altura):
    for j in range (anchura):
        print("*", end= " ")
    print()
