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

    def setup_plugs(self, *plugs):
        for plug in plugs:
            name = plug.__class__.__name__
            if name in self.plugs:
                # This is so magic I felt dirty writing this.
                # To Plug system to work, we need to have single Plug object,
                # not many.
                plug.__dict__ = self.plugs[name].__dict__
            else:
                plug.feed_parent(self)
                self.plugs[name] = plug

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
