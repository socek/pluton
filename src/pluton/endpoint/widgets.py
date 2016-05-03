from pluton.application.widget import FormWidget
from pluton.application.widget import SingleWidget

from .forms import CreateEndpointForm


class EndpointSummaryWidget(SingleWidget):
    renderer = 'pluton.endpoint:templates/widgets/summary.haml'

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make(self):
        self.context['endpoint_name'] = self.endpoint.name
        self.context['api_key'] = self.endpoint.api_key
        self.context['api_secret'] = self.endpoint.api_secret
        self.context['events'] = self.events.list_latest(self.endpoint.id)
        self.context['get_reactions'] = self.get_reactions

    def get_reactions(self, group_id):
        return self.events.get_reaction_count(group_id)


class EndpointRowWidget(SingleWidget):
    renderer = 'pluton.endpoint:templates/widgets/row.haml'

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make(self):
        self.context['endpoint'] = self.endpoint
        self.context['status'] = self.events.get_status(self.endpoint.id)


class CreateEndpointFormWidget(FormWidget):
    template = 'pluton.endpoint:templates/widgets/create_form.haml'
    form = CreateEndpointForm
