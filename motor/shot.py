import wiringpi
from wiringpi import GPIO
from time import sleep

wiringpi.wiringPiSetup() 

shot_pin = 6
pause = 0.1

def shot():
    wiringpi.pinMode(shot_pin, GPIO.OUTPUT)  
    wiringpi.digitalWrite(shot_pin, 1)  #GPIO.HIGH
    sleep(0.1)
    wiringpi.digitalWrite(shot_pin, 0)  # GPIO.LOW
        


def wshot():
    wiringpi.pinMode(shot_pin, GPIO.OUTPUT)  
    wiringpi.digitalWrite(shot_pin, 1)  #GPIO.HIGH
    sleep(pause)
    wiringpi.digitalWrite(shot_pin, 0)  # GPIO.LOW
    sleep(pause)
    wiringpi.digitalWrite(shot_pin, 1)  #GPIO.HIGH
    sleep(pause)
    wiringpi.digitalWrite(shot_pin, 0)  # GPIO.LOW
    sleep(pause)
    wiringpi.digitalWrite(shot_pin, 1)  #GPIO.HIGH
    sleep(pause)
    wiringpi.digitalWrite(shot_pin, 0)  # GPIO.LOW
    sleep(pause)