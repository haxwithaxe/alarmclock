
""" Run alarm action """

import threading


class Alarm(object):

    def __init__(self, action, exit_condition):
        """ 

        Args:
            action (Action) - action to preform when the alarm is called.
            exit_condition (Condition) - Condition under which the action should be terminated.

        """
        self.action = action
        self.exit_condition = exit_condition

    def execute(self):
        exit_event = threading.Event()
        self.action.add_event(exit_event)
        self.exit_condition.add_event(exit_event)
        action_thread = self.action.start()
        condition_thread = self.exit_condition.start()
        exit_event.wait()
