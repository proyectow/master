Para empezar a utilizar el sensor de temperatura y humedad e instalar las dependencias de python para Rpi seguir los siguientes pasos:

Desde linea de comandos:

sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel

sudo pip3 install Adafruit_DHT

DIRIGIRNOS AL DIRECTORIO DE TRABAJO-> cd /home/pi/projectoW

DESCARGAR LA LIBRERIA -> git clone https://github.com/adafruit/Adafruit_Python_DHT.git

ACTUALIZAR Rpi-> sudo apt-get update

ACTUALIZAR ENTORNO PARA PYTHON -> sudo apt-get install build-essential python-dev

INSTALAR CONFIGURACION PARA PYTHON -> sudo python setup.py install

REINICIAR RPI -> sudo reboot

ACCESO A LOS PINES GPIO -> /usr/bin/gksu -u root idle

sudo./AdafruitDHT.py 22 4 -> name_program type GPIO



