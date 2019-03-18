from Adafruit_Python_DHT import Adafruit_DHT as dht
from common import constants

gpioTH = 4
gpioLedTEMP = 7


def eval_climatization(
	UMBRAL_TEMP_L, 
	UMBRAL_TEMP_H, 
	UMBRAL_HUM_L, 
	UMBRAL_HUM_H
):
	humidity,temperature = dht.read_retry(dht.DHT22, gpioTH)
	print ('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

	# Llamar a la funcion que activa o desactiva los ventiladores
	if UMBRAL_TEMP_L < temperature < UMBRAL_TEMP_H:
		# Realizar accion
		gpioLedTEMP = LOW
	else:
		# Realizar accion
		gpioLedTEMP = HIGH

	# Llamar a la funcion que activa la bomba o el ventilador de humedad
	if UMBRAL_HUM_L < humidity < UMBRAL_HUM_H:
		# Realizar accion
		gpioLedHUM = LOW
	else:
		# Realizar accion
		gpioLedHUM = HIGH