from pluton.plug.jinja2.widget import SingleWidget as BaseSingleWidget

from pluton.plug.formskit.plug import FormskitPlug
from pluton.plug.sqlalchemy.plug import DatabasePlug

from pluton.client.driver import ClientDriver
from pluton.event.driver import EventDriver

from .resources import PlutonFanstaticPlug


class SingleWidget(BaseSingleWidget):

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)
        self.events = self.add_plug(EventDriver)
        self.forms = self.add_plug(FormskitPlug)
        self.database = self.add_plug(DatabasePlug)
        self.add_plug(PlutonFanstaticPlug)
