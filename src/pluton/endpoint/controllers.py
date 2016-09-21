from pluton.application.controller import Controller

from .widgets import ConfigureEndpointFormWidget
from .widgets import CreateEndpointFormWidget
from .widgets import EndpointSummaryWidget


class EndpointController(Controller):

    def get_endpoint_id(self):
        return self.matchdict['endpoint_id']

    def fetch_endpoint(self):
        endpoint_id = self.get_endpoint_id()
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


class ConfigureEndpoint(EndpointController):
    renderer = 'pluton.endpoint:templates/admin/configure.haml'

    def make(self):
        self.context['endpoint_id'] = self.get_endpoint_id()

        form = self.forms.add_form_widget(
            ConfigureEndpointFormWidget,
            endpoint_id=self.get_endpoint_id(),
        )

        if form.validate():
            self.utils.redirect(
                'endpoints:show',
                endpoint_id=self.get_endpoint_id(),
            )
            self.database().commit()
