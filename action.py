import threading
import time

class Action(threading.Thread):

    def __init__(self, delay_sec=0.2, repeat=True):
        super(Action, self).__init__()
        self.delay_sec = delay_sec
        self.event = None
        self.repeat = repeat

    def add_event(self, event):
        self.event = event

    def run(self):
        self._while()

    def _while(self):
        if not self.event:
            raise ValueError("self.event is not set yet")
        while not self.event.isSet():
            self.execute()
            self.delay()
            if not self.repeat:
                break

    def execute(self):
        pass

    def delay(self):
        time.sleep(self.delay_sec)
