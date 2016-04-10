from pluton.plug.controller import Controller as BaseController
from pluton.plug.controller import JsonController as BaseJsonController

from pluton.plug.formskit.plug import FormskitPlug
from pluton.plug.sqlalchemy.plug import DatabasePlug

from pluton.client.driver import ClientDriver

from .resources import PlutonFanstaticPlug


class PluggedController(BaseController):

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)
        self.forms = self.add_plug(FormskitPlug)
        self.database = self.add_plug(DatabasePlug)


class Controller(PluggedController):

    def create_plugs(self):
        super().create_plugs()
        self.add_plug(PlutonFanstaticPlug)


class JsonController(PluggedController, BaseJsonController):
    pass
