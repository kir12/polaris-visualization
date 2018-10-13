import json
from pprint import pprint
import pandas as pd

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
	data_df = pd.read_json(url,lines=True)
	print(data_df)

if __name__ == "__main__":
	file_read(r'C:\Users\MeaadFRC\Documents\RideCommandForHack_example.json')
