

from StringIO import StringIO
import wave

import alsaaudio

from action import Action


class Play(Action):

    def __init__(self, wav_file=None, volume=100, card="default", repeat=True, delay_sec=0.2):
        super(Play, self).__init__(delay_sec)
        self.wav_file = wav_file
        wf = open(self.wav_file, "rb")
        self.wav_str = wf.read()
        wf.close()
        self.wavio = lambda: wave.open(StringIO(self.wav_str))
        self.volume = volume
        self.card = card
        self.repeat = repeat
        self.device = alsaaudio.PCM(card=card)
        self.event = None
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
        while data:
            # Read data from stdin
            self.device.write(data)
            data = f.readframes(320)
