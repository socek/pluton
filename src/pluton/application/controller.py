from pluton.plug.controller import Controller as BaseController
from pluton.plug.controller import JsonController as BaseJsonController

from pluton.plug.fanstatic.plug import FanstaticPlug
from pluton.plug.formskit.plug import FormskitPlug

from pluton.dashboard.driver import ClientDriver


class PluggedController(BaseController):

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)
        self.forms = self.add_plug(FormskitPlug)


class Controller(PluggedController):

    def create_plugs(self):
        super().create_plugs()
        self.add_plug(FanstaticPlug)


class JsonController(PluggedController, BaseJsonController):
    pass
