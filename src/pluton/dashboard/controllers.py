from pluton.application.controller import Controller
from pluton.endpoint.widgets import EndpointRowWidget


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.haml'

    def make(self):
        self.context['endpoints'] = self.get_endpoints()

    def get_endpoints(self):
        for endpoint in self.endpoints.list():
            obj = EndpointRowWidget(endpoint)
            obj.feed_parent(self)
            yield obj
