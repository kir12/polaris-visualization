from django.shortcuts import render
from django.http import HttpResponse
from world.read import pandas_chunks
from random import randint
import pandas as pd
from dateparser import parse
import datetime

#accesses datapoint directly without chunksize
#faster, but won't work with larger dataset
def old_read(request):
	#moved above as a global var
	data_df = pd.read_json('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json',lines=True)
	print('json file loaded')

	#opens the JSON files, extracts a random point, and extacts the lat/long coords, time/distance, and start-end timestamp
	print('page loading started')
	datapoint = data_df.iloc[randint(0,len(data_df))]
	print(type(datapoint))
	print('specific data point isolated')


def index(request):
	datapoint = pandas_chunks('/run/media/brianl/SAMSUNG USB/RideCommandForHack.json')
	properties = datapoint.properties
	print('properties apect extracted')

	side_values = {'totalDurationInSeconds':int(properties['totalDurationInSeconds']),'totalDistanceInMeters':round(properties['totalDistanceInMeters'],2),'startTimestamp':parse(str(properties['startTimestamp']['$date'])),'endTimestamp':parse(str(properties['endTimestamp']['$date']))}
	print('side_values dictionary created')

	coords = datapoint.geometry['coordinates']
	print('coordinates list extracted')

	sum_long = 0
	sum_lat = 0
	for coord in coords:
		sum_long+=coord[0]
		sum_lat+=coord[1]
	print('average coords calculated')

	return render(request,'world/map.html',{'coords':coords,'avg_long':sum_long/len(coords),'avg_lat':sum_lat/len(coords),'side_values':side_values})
# Create your views here.

def world_view(request):
	data_df = pd.read_json('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json',lines=True) #copied from old_read
	average_points = []
	print(data_df.columns)
	for datapoint in data_df.geometry:
		print(type(datapoint))
		sum_long =0
		sum_lat = 0
		for coord in datapoint['coordinates']:
			sum_long+=coord[0]
			sum_lat+=coord[1]
		average_points.append([sum_long/len(datapoint['coordinates']),sum_lat/len(datapoint['coordinates'])])
	print(len(average_points))
	return render(request,'world/world_view.html',{'average_points':average_points})

