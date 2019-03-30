import sys
from Adafruit_Python_DHT import Adafruit_DHT

from common import constants

gpioTH = 4
gpioTempHigh = 7
gpioTempLow = 8
gpioHumHigh = 9
gpioHumLow = 10


def eval_climatization(
        UMBRAL_TEMP_L,
        UMBRAL_TEMP_H,
        UMBRAL_HUM_L,
        UMBRAL_HUM_H
):
    sensor = Adafruit_DHT.DHT22
    while 1:     
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpioTH)
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        '''
        # Llamar a la funcion que activa o desactiva los ventiladores
        if UMBRAL_TEMP_L > temperature:
            # Realizar accion
            gpioTempLow = HIGH
            gpioTempHigh = LOW
        elif temperature > UMBRAL_TEMP_H:
            # Realizar accion
            gpioTempLow = LOW
            gpioTempHigh = HIGH
        else:
        	gpioTempLow = LOW
            gpioTempHigh = LOW

        # Llamar a la funcion que activa la bomba o el ventilador de humedad
        if UMBRAL_HUM_L > humidity:
            # Realizar accion
            gpioHumLow = HIGH
            gpioHumHigh = LOW
        elif temperature > UMBRAL_HUM_H:
            # Realizar accion
            gpioHumLow = LOW
            gpioHumHigh = HIGH
        else:
        	gpioHumLow = LOW
            gpioHumHigh = LOW
        '''
