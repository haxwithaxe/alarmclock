
from condition import Condition

class KBPress(Condition):

    def __init__(self, prompt="Press enter to disable the alarm:"):
        super(KBPress, self).__init__()
        self.prompt = prompt

    def run(self):
        while not self.met:
            self.poll()
        self.event.set()

    def poll(self):
        """ Poll the state of the desired object or function.
        If it has satisfied the conditions then set self.met = True
        """
        raw_input(self.prompt)
        self.met = True
