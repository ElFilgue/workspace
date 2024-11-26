import json

# Explora la estuctura de datos.
nombreFichero = 'datos/eq_data_1_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

todos_los_diccionarios = todos_los_datos['features']

magnitudes, longitudes, latitudes = [], [], []
for eq_dict in todos_los_diccionarios:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    magnitudes.append(mag)
    longitudes.append(lon)
    latitudes.append(lat)

print(magnitudes[:10])
print(longitudes[:5])
print(latitudes[:5])
