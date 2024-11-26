import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
nombreFichero = 'datos/eq_data_30_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

todos_los_diccionarios = todos_los_datos['features']

magnitudes, longitudes, latitudes, textos_hover = [], [], [], []
for eq_dict in todos_los_diccionarios:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    magnitudes.append(mag)
    longitudes.append(lon)
    latitudes.append(lat)
    textos_hover.append(title)

# Ubica los terremotos en el mapa.
data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': textos_hover,
    'marker': {
        'size': [5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitud'},
    },
}]

my_layout = Layout(title='Terremotos Globales')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
