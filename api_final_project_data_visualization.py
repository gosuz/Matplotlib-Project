import requests
import json

from plotly.graph_objs import Bar
from plotly import offline

# Make a call, and store the response
url = "https://api-football-standings.azharimm.site/leagues/eng.1/standings?season=2020&sort=asc"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Store API response in variable
print(response_dict.keys())

# print(response_dict['status']['name'])
repo_dicts = response_dict['data']
# print(f"Data returned: {len(repo_dicts)}")


standings_data_list = repo_dicts['standings']
# print(f"\nStarts here: {standings_data_list}")

print(f"\nLength of data of 'standings': {len(standings_data_list)}")

# loop it and add 1 to index number each time


index_number = 0
total_wins = []
while index_number < 20:
	standing_data = standings_data_list [index_number]
	index_number = index_number + 1

	standings_stats = standing_data['stats']

	for info in standings_stats:
		print(len(standings_stats))

		counter = 0
		for item in standings_stats:
			print(f"\n{item}")
			print(f"Index position: {counter}")
			counter = counter + 1

		print(f"Index position 0: {standings_stats[0]}") # to get wins
		wins_standings_stats = standings_stats[0]

		wins_data, wins = [], []
		for value in wins_standings_stats.values():
			wins_data.append(value)

	total_wins.append(wins_data[-2])
	print(f"Total wins: {total_wins}\n")



team_names = []
for header in standings_data_list:
	team_name = (header['team']['displayName'])
	team_names.append(team_name)
print(team_names)

# looping through lists to create a dictionary (key, value pairs)
# loop through 


# We have 2 lists:
	# team_names
	# total_wins

repo_names, win_list = [], []
for team in team_names:
	repo_names.append(team)
	for win in total_wins:
		win_list.append(win)

# got access to all team names

data = [{
	'type': 'bar',
	'x': repo_names,
	'y': win_list,
}]

my_layout = {
	'title': 'Data Visualization API Project- Premier League wins in 2020 season',
	'xaxis': {'title': 'Name of team'},
	'yaxis': {'title': 'Total wins in season'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='data_visualization_project.html')
