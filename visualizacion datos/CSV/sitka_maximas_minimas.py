import csv
from datetime import datetime

from matplotlib import pyplot as plt

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas maximas del fichero.
    fechas, maximas, minimas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        fechas.append(fecha_actual)
        maxima = int(fila[5])
        maximas.append(maxima)
        minima = int(fila[6])
        minimas.append(minima)
 
# Dibuja las temperaturas maximas y mínimas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, maximas, c='red')
ax.plot(fechas, minimas, c='blue')

# sombrea el área entre las líneas
plt.fill_between(fechas, maximas, minimas, facecolor='blue', alpha=0.1)

# Formatea el gráfico.
plt.title("Temperaturas diarias maximas y mínimas - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (ºF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
