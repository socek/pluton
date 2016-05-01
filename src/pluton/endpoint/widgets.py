from pluton.application.widget import SingleWidget


class EndpointSummaryWidget(SingleWidget):
    renderer = 'pluton.endpoint:templates/widgets/summary.haml'

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make(self):
        self.context['endpoint_name'] = self.endpoint.name
        self.context['events'] = self.events.list_latest(self.endpoint.id)
