
import time

from condition import Condition

class WaitTime(Condition):

    def __init__(self, wait_sec=5):
        super(WaitTime, self).__init__()
        self.wait_sec = wait_sec

    def run(self):
        while not self.met:
            self.poll()
        self.event.set()

    def poll(self):
        """ Poll the state of the desired object or function.
        If it has satisfied the conditions then set self.met = True
        """
        time.sleep(self.wait_sec)
        self.met = True
