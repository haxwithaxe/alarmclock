
""" Run alarm action """

from alarm import Alarm
from play import Play
from kbpress import KBPress
from button_press import ButtonPress

wav_file = "/usr/share/sounds/alsa/Front_Center.wav"
pin = 18

action = Play(wav_file, volume=60, card="default", repeat=True, delay_sec=0.2)
condition = ButtonPress(pin)
demo = Alarm(action, condition)
demo.execute()
