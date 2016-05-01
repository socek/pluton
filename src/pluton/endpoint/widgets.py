from pluton.application.widget import FormWidget
from pluton.application.widget import SingleWidget

from .forms import CreateEndpointForm


class EndpointSummaryWidget(SingleWidget):
    renderer = 'pluton.endpoint:templates/widgets/summary.haml'

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make(self):
        self.context['endpoint_name'] = self.endpoint.name
        self.context['events'] = self.events.list_latest(self.endpoint.id)


class CreateEndpointFormWidget(FormWidget):
    template = 'pluton.endpoint:templates/widgets/create_form.haml'
    form = CreateEndpointForm
