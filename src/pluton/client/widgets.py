from pluton.application.widget import SingleWidget


class ClientSummaryWidget(SingleWidget):
    renderer = 'pluton.client:templates/widgets/summary.haml'

    def __init__(self, client):
        self.client = client

    def make(self):
        self.context['client_name'] = self.client.name
        self.context['events'] = self.events.list_latest(self.client.id)
