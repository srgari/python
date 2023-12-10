import RPi.GPIO as GPIO
import time 

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)


#set GPIO direction (IN / OUT)
GPIO.setup(25, GPIO.OUT)
#GPIO.setup(25, GPIO.IN)
lala = lambda x: print(GPIO.input(x))
while True:#LED
    GPIO.output(25, True)    
    lala(25)
    time.sleep(1)
    GPIO.output(25, False)
    lala(25)

#GPIO.output(18, True)
#lala(18)
#time.sleep(1)
#GPIO.output(18, False)
#lala(18)