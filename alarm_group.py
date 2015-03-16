
""" Run multiple alarms """

import threading


class AlarmGroup(object):

    def __init__(self, alarms, exit_condition=None, sequential=True):
        """

        Args:

        """
        self.alarms = alarms
        self.global_exit_condition = exit_condition
        self.sequential = sequential

    def execute(self):
        if not self.sequential:
            self._execute_parallel()
        else:
            self._execute_sequential()

    def _execute_sequential(self):
        for alarm in self.alarms:
            alarm.execute()

    def _execute_parallel(self):
        exit_event = threading.Event()
        threads = [threading.Thread(target=x.execute) for x in self.actions]
        if self.global_exit_condition:
            exit_event = threading.Event()
            self.global_exit_condition.add_event(exit_event)
            condition_thread = self.exit_condition.start()
            exit_event.wait()
            condition_thread.join()
        [x.join() for x in threads]
