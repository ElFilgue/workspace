#programa que dice el número, doble y cuadrado de los números del 0 al 9
("Ingrese un caracter: ")
num_doble_cuadrado = [(num, num*2, num**2) for num in range(10)]
print(num_doble_cuadrado)