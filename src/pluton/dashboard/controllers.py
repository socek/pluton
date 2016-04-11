from pluton.application.controller import Controller
from pluton.client.widgets import ClientSummaryWidget


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.haml'

    def make(self):
        self.context['clients'] = self.get_clients()

    def get_clients(self):
        for client in self.clients.list():
            obj = ClientSummaryWidget(client)
            obj.feed_parent(self)
            yield obj
