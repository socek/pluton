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
        self.reaction_links = self.add_plug(ReactionLinkDriver)
        self.database = self.add_plug(DatabasePlug)

        self.add_reaction_cls(PrintEvent)
        self.add_reaction_cls(DiskCheckReaction)

    def add_reaction_cls(self, cls):
        reaction = self.add_plug(cls)
        self.reactions[reaction.name] = reaction

    def react_for_event(self, event):
        query = self.reaction_links.list_for_event(event)
        for reaction_name in query:
            react = self.reactions[reaction_name]
            react.react(event)
