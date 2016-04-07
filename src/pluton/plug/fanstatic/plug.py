from js.bootstrap import bootstrap
from js.jquery import jquery

from pluton.plug.plug import RequestPlug


class FanstaticPlug(RequestPlug):

    default = {
        'jquery': jquery,
        'bootstrap': bootstrap,
    }

    def add_resource(self, name, lib):
        self.resources[name] = lib

    def need(self, name):
        self.resources[name].need()
        return ''

    def before_make(self):
        self.resources = dict(self.default)
        self.append_resources()
        self.main.context['need'] = self.need

    def append_resources(self):
        pass
