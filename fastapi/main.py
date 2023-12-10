# https://tutorials-raspberrypi.com/control-all-gpios-with-the-raspberry-pi-rest-api-via-python/
# This code is not meant to be executed manually
# This code is executed by uvicorn: $uvicorn main:app --reload -host 0.0.0.0

# End result: visit [site]/switch/14 and the LED should turn on and off!

# You should have a led connected to your pi. I recommend gpio port 14 for simplicity
# --------
# |oo12oo
# |oooooo

# 1: ground; 2: gpio14


from fastapi import FastAPI
import RPi.GPIO as GPIO
import colorama
from colorama import Fore, Style
print(Fore.BLUE + "Hello World")
# instantiate FastAPI
app = FastAPI()

# tell GPIO to use BCM: layout as in raspberry pi 4 map of GPIO
GPIO.setmode(GPIO.BCM)

@app.get('/switch/{gpio}')
def read_root(gpio:int):
    gpio = int(gpio)
    print(Fore.RED + str(gpio) + Style.RESET_ALL)
    GPIO.setup(gpio, GPIO.OUT)
    channel_status = GPIO.input(gpio)
    if channel_status == 1:
        GPIO.output(gpio, 0)
    else:
        GPIO.output(gpio, 1)
    
    return {'message':GPIO.input(gpio)}
