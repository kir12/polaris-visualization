from django.shortcuts import render
from django.http import HttpResponse
from world.read import file_read_pandas, pandas_points
from random import randint
import pandas as pd
from dateparser import parse
import datetime

def index(request):

	#opens the JSON files, extracts a random point, and extacts the lat/long coords, time/distance, and start-end timestamp
	data_df = pd.read_json('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json',lines=True)
	datapoint = data_df.iloc[randint(0,len(data_df))]
	properties = datapoint.properties
	side_values = {'totalDurationInSeconds':int(properties['totalDurationInSeconds']),'totalDistanceInMeters':round(properties['totalDistanceInMeters'],2),'startTimestamp':parse(str(properties['startTimestamp']['$date'])),'endTimestamp':parse(str(properties['endTimestamp']['$date']))}
	#print(side_values)
	coords = datapoint.geometry['coordinates']

	sum_long = 0
	sum_lat = 0
	for coord in coords:
		sum_long+=coord[0]
		sum_lat+=coord[1]

	return render(request,'world/map.html',{'coords':coords,'avg_long':sum_long/len(coords),'avg_lat':sum_lat/len(coords),'side_values':side_values})
# Create your views here.
