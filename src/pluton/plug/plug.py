class Plug(object):

    def __init__(self):
        super().__init__()
        self.parent = None

    @property
    def plugs(self):
        return self.application.plugs

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


class RequestPlug(Plug):

    def feed_parent(self, parent):
        self.request = parent.request
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
    def matchdict(self):
        return self.request.matchdict

    @property
    def route_path(self):
        return self.request.route_path

    @property
    def settings(self):
        return self.registry['settings']

    @property
    def paths(self):
        return self.registry['paths']
