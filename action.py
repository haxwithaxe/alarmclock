import logging
import threading
import time


class Action(threading.Thread):

    def __init__(self, delay_sec=0.2, repeat=True):
        super(Action, self).__init__()
        self.delay_sec = delay_sec
        self.event = None
        self.repeat = repeat
        self.logger = logging.getLogger(self.__class__.__name__)

    def add_event(self, event):
        self.event = event

    def run(self):
        self._while()

    @property
    def should_continue_loop(self):
        if self.event.is_set():
            return False
        return True

    def _while(self):
        if not self.event:
            raise ValueError("self.event is not set yet")
        while not self.event.is_set():
            self.logger.debug("Event is set: %s", self.event.is_set())
            self.execute()
            self.delay()
            if not self.repeat:
                break

    def execute(self):
        pass

    def delay(self):
        time.sleep(self.delay_sec)

    def stop(self):
        self.event.set()
