from pluton.application.plugs import RequestPluggedMixin
from pluton.plug.plug import RequestPlug


class BreadCrumbElement(RequestPluggedMixin, RequestPlug):

    def __init__(self, key, label, url=None, parent=None):
        self.key = key
        self._label = label
        self.url = url
        self._parent = parent

    def get_url(self):
        if self.url:
            return self.url(self.request, self.parent.main)

    @property
    def label(self):
        if isinstance(self._label, str):
            return self._label
        else:
            return self._label(self.parent)


class BreadCrumb(RequestPluggedMixin, RequestPlug):

    def feed_parent(self, request):
        super().feed_parent(request)
        for key, crumb in self.data.items():
            crumb.feed_parent(request)

    def add(self, key, *args, **kwargs):
        self.data[key] = BreadCrumbElement(key, *args, **kwargs)

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
        def wrapped(req, main):
            values = main.get_breadcrumbs_vars()
            for name in var_names:
                kwargs[name] = values[name]
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
            lambda parent: 'Endpoint: ' + parent.main.endpoint.name,
            self.route('endpoints:show', var_names=('endpoint_id',)),
            'dashboard',
        )
        self.add(
            'endpoints:configure',
            'Configure',
            self.route('endpoints:configure', var_names=('endpoint_id',)),
            'endpoints:show',
        )
        self.add(
            'endpoints:create',
            'Create',
            self.route('endpoints:create'),
            'dashboard',
        )
        self.add(
            'events:main',
            'Events',
            None,
            'dashboard',
        )

        self.add(
            'events:edit',
            'Edit',
            self.route('events:edit', var_names=('event_group_id',)),
            'endpoints:show',
        )
