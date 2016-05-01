from pluton.application.controller import Controller

from .widgets import CreateEndpointFormWidget


class CreateEndpoint(Controller):
    renderer = 'pluton.endpoint:templates/admin/create.haml'

    def make(self):
        form = self.forms.add_form_widget(CreateEndpointFormWidget)

        if form.validate():
            self.utils.redirect('dashboard')
