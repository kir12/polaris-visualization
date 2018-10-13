import json
from pprint import pprint

def file_read(url):
	with open(url) as f:
		data = json.load(f)
	pprint(data)
	print('a')

if __name__ == "__main__":
	file_read('/run/media/brianl/SAMSUNG USB/RideCommandForHack_example.json')
