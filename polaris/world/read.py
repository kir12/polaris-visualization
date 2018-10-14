'''
pre-django implementation of Panda
MERGED INTO DJANGO
'''
import json
import ijson
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
from random import randint

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

	for test in data_df.geometry:
		print(test.keys())

	print("\n===========\n")

	#ietereates through the Property series. Each 'test' is a Python dictionary
	for test in data_df.properties:
		print(test.keys())
def pandas_points(url):

	#opens JSON in pandas
	#data_df is of type series
	data_df = pd.read_json(url,lines=True)

	#gets specific datapoint (e.g. first one) and returns as a list
	#todo: replace 0 with random number once google maps api is soldified
	datapoint = data_df.iloc[randint(0,len(data_df))]
	return datapoint.geometry['coordinates']

def pandas_chunks(url):
	#will also need to re-direct to loading page

	#opens json file in pandas as JsonReader type (i.e. an ieterator)
	data_df = pd.read_json(url,lines=True,chunksize=1)
	
	#creates value to summon, index to increment by, and intiailizes placeholder for datapointFrame
	random_val = randint(0,49999)	
	datapointFrame = pd.DataFrame()
	iet=0

	#ieterates through JsonReader and keeps ieterating iet until desired value is hit. 
	#exits out of loop upon hitting said value
	for chunk in data_df:
		if iet == random_val:
			datapointFrame=chunk
			break
		else:
			iet+=1
			print(iet)
	#extracts Series type out of DataFrame and returns
	datapoint = datapointFrame.iloc[0]
	return datapoint
	
if __name__ == "__main__":
	pandas_chunks('/run/media/brianl/SAMSUNG USB/RideCommandForHack.json')

