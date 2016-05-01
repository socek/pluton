from formskit.validators import NotEmpty

from pluton.application.forms import Form


class CreateEndpointForm(Form):

    def create_form(self):
        self.add_field('name', label='Nazwa', validators=[NotEmpty()])

    def on_success(self):
        data = self.get_data_dict(True)
        event = self.endpoints.create(
            data['name'],
        )
        self.database().add(event)
        self.database().flush()
