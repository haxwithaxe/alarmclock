

import RPi.GPIO as gpio
import time

def gpio__init__():
    gpio.setmode(gpio.BCM)

class Button(object):

    def __init__(self, pin):
        self.pin = pin
	gpio__init__()
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def poll(self):
        return gpio.input(self.pin) #(gpio.input(self.pin) or False)

if __name__ == "__main__":
	b = Button(18)
	print(b.poll())
