from pluton.application.plugs import RequestPluggedMixin
from pluton.plug.plug import RequestPlug


class BreadCrumbElement(RequestPluggedMixin, RequestPlug):

    def __init__(self, label, url=None, parent=None):
        self._label = label
        self.url = url
        self.parent = parent

    def get_url(self):
        if self.url:
            return self.url(self.request)

    @property
    def label(self):
        return self._label


class BreadCrumb(RequestPluggedMixin, RequestPlug):

    def feed_request(self, request):
        super().feed_request(request)
        for key, crumb in self.data.items():
            crumb.feed_request(request)

    def add(self, key, *args, **kwargs):
        self.data[key] = BreadCrumbElement(*args, **kwargs)

    def get_crumbs_for(self, key):
        if not key:
            return
        keys = []
        tmp = key
        while self.data[tmp].parent:
            keys.append(tmp)
            tmp = self.data[tmp].parent
        keys.append(tmp)
        keys.reverse()
        for key in keys:
            yield self.data[key]

    def __init__(self):
        self.data = {}

        self.add('home', 'Główna', lambda req: req.route_path('home'))
