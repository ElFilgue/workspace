import csv

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)
    print(fila_cabecera)
