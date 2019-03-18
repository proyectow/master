import json
import argparse

from Adafruit_Python_DHT import Adafruit_DHT as dht
from climatization import temp_hum as th


def read_json_file(dataset_path):
    with open(dataset_path) as file:
        params = json.load(file)
    return params


def get_params(type_weed, params):
	for param in params:
		if param == type_weed:
			temp_umbral = params[param]['temperature_umbral']
			hum_umbral = params[param]['humidity_umbral']
	return temp_umbral, hum_umbral

def handler(type_weed: str) -> None:
	params = read_json_file('config.json')
	temp_umbral, hum_umbral = get_params(type_weed, params) # primer parametro HIGh temp_umbral[0] = umbral por arriba
	

if __name__ == '__main__':

	parser = argparse.ArgumentParser(
    	prog='plan',
    	description='tipo de planta',
	)
	parser.add_argument('plt', help='tipo de planta')

	args = parser.parse_args()
	handler(
	    args.plt,
	)
