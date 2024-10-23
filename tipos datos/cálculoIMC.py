#calculadora de índice de masa corporal

peso = float(input("Introduce tu peso en kilos: "))
estatura = float(input("Introduce tu altura en metros: "))
print(f"Entonces pesas {peso} kg y mides {estatura}")
imc = round(peso/(estatura*estatura),2)
print(f"tu IMC es de {imc}")

if imc <= 18.5:
    print ("Tienes Insuficiencia ponderal")
elif imc >18.5: 
    if imc <24.9:
        print("Tienes un Peso normal")
    elif imc>29.9:
        print("Tienes Obesidad")   
