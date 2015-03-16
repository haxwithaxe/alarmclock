import threading

class Condition(threading.Thread):

    def __init__(self):
        super(Condition, self).__init__()
        self.event = None
        self._met = False  #have the conditions been met?
        self.lock = threading.Lock()

    def add_event(self, event):
        self.event = event

    def run(self):
        self.run_once()
        while not self.met:
            print("self.met", self.met)
            self.poll()
        self.event.set()

    @property
    def met(self):
        self.lock.acquire()
        met = self._met
        self.lock.release()
        return met

    @met.setter
    def met(self, value):
        self.lock.acquire()
        self._met = value
        self.lock.release()


    def poll(self):
        """ Poll the state of the desired object or function.
        If it has satisfied the conditions then set self.met = True
        """
        pass

    def run_once(self):
        pass

