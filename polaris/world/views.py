from django.shortcuts import render
from django.http import HttpResponse
from world.read import file_read_pandas, pandas_points

def index(request):
	coords = pandas_points('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json')
	print(coords)
	return render(request,'world/map.html',{'coords':coords})
# Create your views here.
