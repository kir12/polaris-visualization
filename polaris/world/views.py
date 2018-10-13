from django.shortcuts import render
from django.http import HttpResponse
from world.read import file_read_pandas, pandas_points

def index(request):
	coords = pandas_points('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json')
	#print(coords)
	sum_long = 0
	sum_lat = 0
	for coord in coords:
		sum_long+=coord[0]
		sum_lat+=coord[1]
	return render(request,'world/map.html',{'coords':coords,'avg_long':sum_long/len(coords),'avg_lat':sum_lat/len(coords)})
# Create your views here.
