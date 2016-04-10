from pluton.application.controller import Controller


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.haml'

    def make(self):
        self.context['clients'] = self.clients.list()
        self.context['get_events'] = self._get_events

    def _get_events(self, client):
        return self.events.list_latest(client.id)
