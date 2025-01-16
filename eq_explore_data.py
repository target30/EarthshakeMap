import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

# Изучение структуры данных
filename = 'Data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'Data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f,indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
mags,lons, lats, hover_texts = [], [], [], []
for eq_data in all_eq_dicts:
    mag = eq_data['properties']['mag']
    lon = eq_data['geometry']['coordinates'][0]
    lat = eq_data['geometry']['coordinates'][1]
    title = eq_data['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Нанесение данных на карту
# Первый способ определения данных для Scattergeo
# data = [Scattergeo (lon = lons, lat = lats)]
# Второй способ
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='Global Earthquakes.html')

