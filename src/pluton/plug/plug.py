from collections import OrderedDict


class Plug(object):

    @property
    def plugs(self):
        self._plugs = getattr(self, '_plugs', OrderedDict())
        return self.main._plugs

    @property
    def main(self):
        if getattr(self, 'parent', None):
            return self.parent.main
        else:
            self._request_cache = getattr(self, '_request_cache', {})
            return self

    @property
    def request_cache(self):
        return self.main._request_cache

    def setup_plugs(self, *plugs):
        for plug in plugs:
            name = plug.__class__.__name__
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
