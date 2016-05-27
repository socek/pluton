from collections import OrderedDict


class BasePlug(object):

    @property
    def plugs(self):
        return self.main._plugs

    @property
    def main(self):
        if getattr(self, 'parent', None):
            return self.parent.main
        else:
            self._plugs = getattr(self, '_plugs', OrderedDict())
            return self

    def add_plug(self, cls):
        if cls.__name__ not in self.plugs:
            self.plugs[cls.__name__] = cls()
            self.plugs[cls.__name__].feed_parent(self)
        return self.plugs[cls.__name__]

    def feed_parent(self, parent):
        self.parent = parent
        self.application = parent.application
        self.create_plugs()

    def create_plugs(self):
        pass

    @property
    def registry(self):
        return self.application.registry

    @property
    def settings(self):
        return self.application.settings

    @property
    def paths(self):
        return self.application.paths


class Plug(BasePlug):
    pass


class RequestPlug(Plug):

    def feed_parent(self, parent):
        self.request = parent.main.request
        super().feed_parent(parent)

    @property
    def registry(self):
        return self.request.registry

    @property
    def POST(self):
        return self.request.POST

    @property
    def GET(self):
        return self.request.GET

    @property
    def json(self):
        return self.request.json

    @property
    def matchdict(self):
        return self.request.matchdict

    @property
    def route_path(self):
        return self.request.route_path
