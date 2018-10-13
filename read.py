import json
import ijson
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

def file_read(url):
	with open(url,'r') as f:
		data = json.load(f)
	pprint(data)
	print('a')

def file_read_ijson(url):
	with open(url,'r') as f:
		objects = ijson.items(f,'geometry.coordinates.items')
		columns=list(objects)

def file_read_pandas(url):

	#opens JSON in pandas
	#data_df is of type series
	data_df = pd.read_json(url,lines=True)

	#get all 1st all attributes
	print(data_df.columns)

	#example of calling series 1st level attribute
	print(data_df.creationDate)

	#ietereates through the Property series. Each 'test' is a Python dictionary
	for test in data_df.properties:
		print(test.keys())
if __name__ == "__main__":
	file_read_pandas('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json')

