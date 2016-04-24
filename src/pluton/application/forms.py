from pluton.plug.formskit.models import PostForm
from pluton.reactions.plugs import ReactionRunner

from .plugs import PluggedMixin


class Form(PluggedMixin, PostForm):

    def create_plugs(self):
        super().create_plugs()
        self.reactions = self.add_plug(ReactionRunner)
