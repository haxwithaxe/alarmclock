
from button import Button
from condition import Condition


class ButtonPress(Condition):

    def __init__(self, pin):
        super(ButtonPress, self).__init__()
        self.button = Button(pin)

    def poll(self):
        """ Poll the state of this button.

        If it has satisfied the conditions then set self.met = True

        """
	self.met = self.button.poll()
