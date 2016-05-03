from pluton.application.controller import Controller

from .widgets import CreateEndpointFormWidget
from .widgets import EndpointSummaryWidget


class EndpointController(Controller):

    def fetch_endpoint(self):
        endpoint_id = self.matchdict['endpoint_id']
        endpoint = self.endpoints.get_by_id(endpoint_id)
        self.context['endpoint'] = endpoint
        return endpoint


class CreateEndpoint(Controller):
    renderer = 'pluton.endpoint:templates/admin/create.haml'

    def make(self):
        form = self.forms.add_form_widget(CreateEndpointFormWidget)

        if form.validate():
            self.utils.redirect('dashboard')


class ShowEndpoint(EndpointController):
    renderer = 'pluton.endpoint:templates/admin/show.haml'

    def make(self):
        endpoint = self.fetch_endpoint()
        widget = EndpointSummaryWidget(endpoint)
        self.utils.add_widget('endpoint', widget)


