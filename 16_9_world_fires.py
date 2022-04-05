# task: Make a map that shows which part of the world are affected
	# by fires

# part 1: data processing (extract data)
# part 2: mapping work (use extracted data to build map)

import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

import os
cwd = os.getcwd()
print(cwd)

# read file
filename = 'world_fires_1_day.csv'

# 2 parts
# part 1: data processing 
# task: read csv file and extract relevant data 
# parse CSV file & print position of headers

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get longitude, latitude, brigthnesses, times from file
	# extract data I need:
		# location(longitude, latitude)
			# longitude = index position [1]
			# latitude = index position [0]
		# brightness of fire = index position [2]
		# date (optional) = index position [5]

# enter relevant parsed data into a list
	lons, lats, brightnesses, hover_texts = [], [], [], []
	for row in reader:
		lon = float(row[1])
		lat = float(row[0])
		brightness = float(row[2])

		#append data to lists
		lons.append(lon)
		lats.append(lat)
		brightnesses.append(brightness)
		hover_texts.append(brightness)



# part 2: mapping work
	# Use for loop to map through throgh the list
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [0.02*brightness for brightness in brightnesses],
		'color': brightnesses,
		'colorscale': 'Reds',
		'reversescale': False,
		'colorbar': {'title': 'Brightness'},
	},
}]
my_layout = Layout(title = 'World Fires past 30 days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')





"""
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])


# plot data of fire (location, brightness of fire)
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
"""


# change the title
# change the color & size of markers on the map
	

