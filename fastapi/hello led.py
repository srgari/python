import RPi.GPIO as GPIO
from time import sleep

#print(GPIO.OUT, GPIO.LOW, GPIO.IN, GPIO.HIGH)

# tell GPIO to use BCM: layout as in raspberry pi 4 map of GPIO
GPIO.setmode(GPIO.BCM)

# Setup channel as output:
# 14 = channel with LED;
# GPIO.OUT = GPIO.LOW = 0; GPIO.IN = 1
# GPIO.IN = GPIO.HIGH = 1
GPIO.setup(14, GPIO.OUT, initial = GPIO.LOW)

for _ in range(4):
    # Change channel to GPIO.HIGH for 1s
    GPIO.output(14, 1) # 1 = GPIO.HIGH
    print(GPIO.input(14))
    sleep(1)
    # Change channel to GPIO.LOW for 1s
    GPIO.output(14, 0) # 0 = GPIO.LOW    
    sleep(1)
# clear up all channels - avoid damages to Pi
GPIO.cleanup()
