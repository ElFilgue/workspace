quieres_saludar= 'S'
NUM_MAX_SALUDOS= 4
num_saludo= 0
while quieres_saludar=='S':
    print("Hóla que tal!")
    num_saludo +=1
    if num_saludo == NUM_MAX_SALUDOS:
        print("Has alcanzado el número máximo de saludos")
        break
    quieres_saludar = input("¿Quiere otro saludo? [S/N]")
    while quieres_saludar not in ('S','N'):
        quieres_saludar = input("Sólo se admiten las letras S y N: ¿Quiere otro saludo? [S/N]")
print("Que tenga un buen día")
