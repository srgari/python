# modified from https://tutorials-raspberrypi.com/control-all-gpios-with-the-raspberry-pi-rest-api-via-python/
from fastapi import FastAPI
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
app = FastAPI()
 
 
@app.get("/read/{gpio}")
def read_root(gpio: int):
    #GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio, GPIO.OUT)
    #return {"gpio": gpio, "on": GPIO.input(gpio)}
    return {"gpio": gpio, "on": GPIO.input(gpio)}