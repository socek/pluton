from pluton.application.plugs import RequestPluggedMixin
from pluton.plug.plug import RequestPlug


class BreadCrumbElement(RequestPluggedMixin, RequestPlug):

    def __init__(self, label, url=None, parent=None):
        self.label = label
        self.url = url
        self._parent = parent

    def get_url(self):
        if self.url:
            return self.url(self.request)


class BreadCrumb(RequestPluggedMixin, RequestPlug):

    def feed_parent(self, request):
        super().feed_parent(request)
        for key, crumb in self.data.items():
            crumb.feed_parent(request)

    def add(self, key, *args, **kwargs):
        self.data[key] = BreadCrumbElement(*args, **kwargs)

    def get_crumbs_for(self, key):
        if not key:
            return
        if key not in self.data:
            return
        keys = []
        tmp = key
        while self.data[tmp]._parent:
            keys.append(tmp)
            tmp = self.data[tmp]._parent
        keys.append(tmp)
        keys.reverse()
        for key in keys:
            yield self.data[key]

    def __init__(self):
        super().__init__()
        self.data = {}
        self.generate_crumbs()

    def route(self, *args, var_names=[], **kwargs):
        def wrapped(req):
            for name in var_names:
                kwargs[name] = req.matchdict[name]
            return req.route_path(*args, **kwargs)
        return wrapped

    def get_current_crumbs(self):
        return self.get_crumbs_for(self.request.matched_route.name)

    def generate_crumbs(self):
        self.add(
            'dashboard',
            'Home',
            self.route('dashboard'),
        )
        self.add(
            'endpoints:show',
            'Endpoint',
            self.route('dashboard'),
            'dashboard',
        )
