from pluton.application.plugs import PluggedMixin
from pluton.plug.plug import Plug


class Reaction(PluggedMixin, Plug):
    name = None

    @property
    def raw(self):
        return self.event.raw

    def react(self, event):
        pass


class PrintEvent(Reaction):
    name = 'print_event'

    def react(self, event):
        print('React:', event.name, event.raw)
