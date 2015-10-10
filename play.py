

import logging
from StringIO import StringIO
import time
import wave

import alsaaudio

from action import Action


class Play(Action):

    def __init__(self, wav_file=None, volume=100, card="default", repeat=True, delay_sec=0.2):
        super(Play, self).__init__(repeat=repeat, delay_sec=delay_sec)
        self.wav_file = wav_file
        with open(self.wav_file, "rb") as wf:
	    self.wav_str = wf.read()
        self.wavio = lambda: wave.open(StringIO(self.wav_str))
        self.volume = volume
        self.card = card
        self.device = alsaaudio.PCM(card=card)
        self._alsa_init()

    def _alsa_init(self):
        f = self.wavio()
        self.device.setchannels(f.getnchannels())
        self.device.setrate(f.getframerate())
        # 8bit is unsigned in wav files
        if f.getsampwidth() == 1:
            self.device.setformat(alsaaudio.PCM_FORMAT_U8)
        # Otherwise we assume signed data, little endian
        elif f.getsampwidth() == 2:
            self.device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        elif f.getsampwidth() == 3:
            self.device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
        elif f.getsampwidth() == 4:
            self.device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
        else:
            raise ValueError('Unsupported format')
        self.device.setperiodsize(320)

    def execute(self):
        f = wave.open(StringIO(self.wav_str))
        data = f.readframes(320)
        while data and self.should_continue_loop:
            if self.logger.getEffectiveLevel() == logging.DEBUG:
                self.logger.debug("Quiet pass for sanity: %s", self.wav_file)
                time.sleep(self.delay_sec*10)
            self.logger.debug("Playing %s", self.wav_file)
            self.device.write(data)
            data = f.readframes(320)
            self.logger.debug("Done playing %s", self.wav_file)
