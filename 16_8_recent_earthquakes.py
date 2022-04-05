import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from plotly import colors
for key in colors.PLOTLY_SCALES.keys():
    print(key)

# import geojsondata ('significant_month.geojson')
filename = 'significant_month.geojson'

# open file
with open(filename) as f:
	all_eq_data = json.load(f)

# map data on EQ
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

# format map/style map
	# edit title
my_layout = Layout(title= all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
	# color and size of marker (larger and darker color for bigger EQ)

