import json


def get_cities():
	cites_coords = []
	with open('cities.json') as data_file:    
	    data = json.load(data_file)
	    for city in data:
	    	coordinates = str(city["latitude"]) + " " + str(city["longitude"])
	    	cites_coords.append(str(coordinates))
	return cites_coords;

