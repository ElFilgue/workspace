import csv
from datetime import datetime

from matplotlib import pyplot as plt

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas maximas del fichero.
    fechas, maximas = [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        fechas.append(fecha_actual)
        maxima = int(fila[5])
        maximas.append(maxima)
 
# Dibuja las temperaturas maximas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, maximas, c='red')

# Formatea el gráfico.
plt.title("Temperaturas diarias maximas - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (ºF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
