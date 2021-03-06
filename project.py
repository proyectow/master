import json
import argparse

from Adafruit_Python_DHT.examples import AdafruitDHT as th


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


def handler(
    plt: str
) -> None:
    params = read_json_file('config.json')

    temp_umbral, hum_umbral = get_params(plt, params)

    print('Temp min:', temp_umbral[0],
          'Temp max:', temp_umbral[1])

    print('Hum min:', hum_umbral[0],
          'Hum max:', hum_umbral[1])

    th.eval_climatization(
        temp_umbral[0],
        temp_umbral[1],
        hum_umbral[0],
        hum_umbral[1]    
    )

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
