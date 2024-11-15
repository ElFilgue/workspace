def minimo(a,b):
    if a<b:
        print(f'El valor minimo es {a} y {b} es: {a}')
    elif a>b:
        print(f'El valor minimo es {a} y {b} es: {b}')
    else:
        print(f'Los dos numeros son iguales')

numero1= int(input('Introduce el numero 1: '))
numero2= int(input('Introduce el numero 2: '))
minimo(numero1,numero2)
