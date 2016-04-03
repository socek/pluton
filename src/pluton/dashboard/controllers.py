from pluton.plug.controller import Controller
from pluton.plug.controller import JsonController


class Dashboard(JsonController):

    def make(self):
        print(self.context)
