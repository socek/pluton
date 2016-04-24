from pluton.plug.formskit.plug import FormskitPlug
from pluton.plug.sqlalchemy.plug import DatabasePlug

from pluton.client.driver import ClientDriver
from pluton.event.driver import EventDriver
from pluton.reactions.driver import ReactionLinkDriver

from .resources import PlutonFanstaticPlug


class PluggedMixin(object):

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)
        self.events = self.add_plug(EventDriver)
        self.reaction_links = self.add_plug(ReactionLinkDriver)
        self.forms = self.add_plug(FormskitPlug)
        self.database = self.add_plug(DatabasePlug)


class RequestPluggedMixin(PluggedMixin):

    def create_plugs(self):
        super().create_plugs()
        self.add_plug(PlutonFanstaticPlug)
