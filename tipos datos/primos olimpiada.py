# Programa que decide si un numero es primo o no i calcula numeros primos consecutivos

t = int(input("Indica el número de casos que cal processar: "))
for i in range(0,t):
    k = int(input("Introdueix un nombre entre 0 i 100: "))
    n = int(input("Introdueix un nombre sancer entre 0 i 10000: "))
if k == 0:
    if (n % 2 == 0 ):
            print ("NO")
    else:
            print("SI")