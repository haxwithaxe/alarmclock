
import threading

import web

from condition import Condition

class WebUI(Condition):

    def run(self):
        urls = ('/', 'WebUI')
        app = web.application(urls, globals())
        app.run()

    def GET(self):
        i = web.input()
        if "stop" in i:
            self.met = True
            print("self.met", self.met)
            return """All clear"""
        return """<a href="/?stop=true">Stop</a>"""


