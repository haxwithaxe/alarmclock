
import subprocess

from action import Action

class Command(Action):

    def __init__(self, command, args, delay_sec=0.2, repeat=False):
        super(Command, self).__init__(delay_sec, repeat)
        self.command = command
        self.args = args

    def execute(self):
        cmd = [self.command]
        cmd.extend(self.args)
        subprocess.Popen(cmd)
