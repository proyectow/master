import sys
import Adafruit_DHT

from common import constants


gpioTH = 4
gpioTempHigh = 17
gpioTempLow = 27
gpioHumHigh = 22
gpioHumLow = 10

def eval_climatization(
        UMBRAL_TEMP_L,
        UMBRAL_TEMP_H,
        UMBRAL_HUM_L,
        UMBRAL_HUM_H
):
    while 1:
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        humidity = round(humidity,2)
        temperature = round(temperature,2)

        # Llamar a la funcion que activa o desactiva los ventiladores
        if UMBRAL_TEMP_L > temperature:
            print('TEMP POR DEBAJO DEL UMBRAL {}ºC<{}ºC'.format(temperature,UMBRAL_TEMP_L))
            '''
				- servo1:on
				- servo2:on
				- servo3:off
				- servo4:off
				- vent_clima_1:on
				- vent_clima_2:off
            '''
            # gpioTempLow = HIGH
            # gpioTempHigh = LOW
        elif temperature > UMBRAL_TEMP_H:
            print('TEMP POR ENCIMA DEL UMBRAL {}ºC<{}ºC'.format(UMBRAL_TEMP_H,temperature))
            '''  
            - servo1:off
				- servo2:off
				- servo3:on
				- servo4:on
				- vent_clima_1:off
				- vent_clima_2:on
  				'''  
            # gpioTempHigh = HIGH
        else:
            print('TEMP OK {}ºC<{}ºC<{}ºC'.format(UMBRAL_TEMP_L,temperature,UMBRAL_TEMP_H))
            # gpioTempLow = LOW
        
        # Llamar a la funcion que activa la bomba o el ventilador de humedad
        if UMBRAL_HUM_L > humidity:
            print('HUM POR DEBAJO DEL UMBRAL {}%<{}%'.format(humidity,UMBRAL_TEMP_L))
            '''
           	bomba_neb:on
           	vent_secado:off
            '''      
            # gpioHumHigh = LOW
        elif humidity > UMBRAL_HUM_H:
            print('HUM POR ENCIMA DEL UMBRAL {}%<{}%'.format(humidity,UMBRAL_HUM_H))
            # Realizar accion
            '''
            bomba_neb:on
           	vent_secado:off
            '''  
            # gpioHumLow = LOW
            # gpioHumHigh = HIGH
        else:
            print('HUM OK {}%<{}%<{}%'.format(UMBRAL_HUM_L,humidity,UMBRAL_HUM_H))
            # gpioHumLow = LOW
            # gpioHumHigh = LOW
        

