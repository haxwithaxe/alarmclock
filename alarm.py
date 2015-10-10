
""" Run alarm action """

import logging
import threading


class Alarm(object):

    def __init__(self, action, exit_condition):
        """ 

        Args:
            action (Action) - action to preform when the alarm is called.
            exit_condition (Condition) - Condition under which the action should be terminated.

        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("%s, %s", action, exit_condition)
        self.action = action
        self.exit_condition = exit_condition

    def execute(self):
        self.exit_event = threading.Event()
        self.action.add_event(self.exit_event)
        self.exit_condition.add_event(self.exit_event)
        self.logger.debug(self.action)
        self.action.start()
        self.exit_condition.start()
	self.exit_event.wait()
        self.action.join()
        self.exit_condition.join()
