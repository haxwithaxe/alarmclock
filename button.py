

import RPi.GPIO as gpio
import time

def gpio__init__():
    gpio.setmode(gpio.BCM)

class Button(object):

    def __init__(self, pin):
        self.pin = pin
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def poll(self):
        return not gpio.input(self.pin)

if __name__ == "__main__":
	b = Button(18)
	print(b.poll())
