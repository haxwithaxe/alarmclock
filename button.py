

import RPi.GPIO as GPIO
import time

def gpio__init__():
    GPIO.setmode(GPIO.BCM)

class Button(object):

    def __init__(self, pin):
        self.pin = pin
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def poll(self):
        return gpio.input(self.pin) #(gpio.input(self.pin) or False)
