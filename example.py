#!/usr/bin/env python

import sys
from alarm import Alarm
from command import Command
from play import Play
from button import gpio__init__
from button_press import ButtonPress

gpio__init__()

pin = 18
wav_file = sys.argv[1]

action = Play(wav_file)
condition = ButtonPress(18)
alarm = Alarm(action, condition)

alarm.execute()
