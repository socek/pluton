from pluton.plug.plug import Plug
from pluton.plug.sqlalchemy.plug import DatabasePlug

from .driver import ReactionLinkDriver
from .reactions import PrintEvent
from .reactions import DiskCheckReaction


class ReactionRunner(Plug):

    def __init__(self):
        super().__init__()
        self.reactions = {}

    def create_plugs(self):
        super().create_plugs()
        self.reaction_links = ReactionLinkDriver()
        self.database = DatabasePlug()

        self.add_reaction(PrintEvent())
        self.add_reaction(DiskCheckReaction())

        self.setup_plugs(
            self.reaction_links,
            self.database,
            *self.reactions.values(),
        )

    def add_reaction(self, reaction):
        self.reactions[reaction.name] = reaction

    def react_for_event(self, event):
        query = self.reaction_links.list_for_event(event)
        for reaction_name in query:
            react = self.reactions[reaction_name]
            react.react(event)
