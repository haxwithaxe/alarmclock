#!/usr/bin/env python

import logging
import sys

import alarm
import command
import play
import button
import button_press
import kbpress


if __name__ == "__main__":
    logging.basicConfig(file='/tmp/alarmclockpi.log', level=logging.ERROR)
    logger = logging.getLogger("alarmclockpi")
    button.gpio__init__()
    pin = 18
    wav_file = sys.argv[1]
    action = play.Play(wav_file)
    #condition = button_press.ButtonPress(18)
    condition = kbpress.KBPress()
    alarm = alarm.Alarm(action, condition)
    logger.debug("Begining LOUD THINGS!!!")
    alarm.execute()
    logger.debug("All done. Exiting %s.", sys.argv[0])
