from pluton.plug.formskit.plug import FormskitPlug
from pluton.plug.sqlalchemy.plug import DatabasePlug

from pluton.endpoint.driver import EndpointDriver
from pluton.event.driver import EventDriver
from pluton.reactions.driver import ReactionLinkDriver

from .resources import PlutonFanstaticPlug


class PluggedMixin(object):

    def create_plugs(self):
        super().create_plugs()
        self.endpoints = EndpointDriver()
        self.events = EventDriver()
        self.reaction_links = ReactionLinkDriver()
        self.database = DatabasePlug()

        self.setup_plugs(
            self.endpoints,
            self.events,
            self.reaction_links,
            self.database,
        )


class RequestPluggedMixin(PluggedMixin):

    def create_plugs(self):
        super().create_plugs()
        self.forms = FormskitPlug()
        self.setup_plugs(
            PlutonFanstaticPlug(),
            self.forms,
        )
