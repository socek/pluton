from pluton.plug.controller import Controller as BaseController
from pluton.plug.controller import JsonController as BaseJsonController
from pluton.reactions.plugs import ReactionRunner

from .plugs import PluggedMixin
from .plugs import RequestPluggedMixin


class PluggedController(PluggedMixin, BaseController):

    def create_plugs(self):
        super().create_plugs()
        self.reactions = ReactionRunner()

        self.setup_plugs(
            self.reactions,
        )


class Controller(RequestPluggedMixin, PluggedController):
    pass


class JsonController(PluggedController, BaseJsonController):
    pass
