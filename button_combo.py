

from button import Button
from condition import Condition

class ButtonCombo(Condition):

    def __init__(self, patern, tail=None):
        """

        Args:
            pattern - A list of buttons and numbers representing buttons
                and how long they should be pressed. None is treated as a
                nonpress interval and tuples of buttons are treated as simultaneous presses.
            tail - The number of seconds to wait before assuming the button presses are all done. Defaults to the largest interval provided.

        """ 
        self.pattern = pattern
        self.buttons = []
        self._get_uniq_buttons()
        self.tail = tail
        if not self.tail:
            self._get_default_tail()

    def _get_default_tail(self):
        intervals = [x for x in self.pattern if isinstance(x, int) or isinstance(x, float)]
        self.tail = max(intervals)

    def _get_uniq_buttons(self):
        seen = []
        for button in self._get_buttons():
            if button.pin not in seen:
                seen.append(button.pin)
                self.buttons.append(button)

    def _get_buttons(self):
        for item in self.pattern:
            if isinstance(item, Tuple):
                for i in item:
                    yield i
            if isinstance(item, Button):
                yield item

    def check_pattern(self):
        """ Step through the pattern and check to see that buttons are pressed when they should be. """
        for index, item in enumerate(self.pattern):
            if isinstance(item, Button):
                time.sleep(self.pattern[index+1])
                if not item.poll():
                    return False
            elif isinstance(item, tuple):
                time.sleep(self.pattern[index+1])
                if False in [x.poll() for x in item]:
                    return False
            elif item is None:
                time.sleep(self.pattern[index+1])

