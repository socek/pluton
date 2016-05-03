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
        print('React:', event.group.name, event.raw)


class DiskCheckReaction(Reaction):
    name = 'disk_check'

    def react(self, event):
        data = ''
        for key, value in sorted(event.raw.items()):
            data += '%s: %s<br>\n' % (key, value)
        event.group.description = data
        self.database().flush()
