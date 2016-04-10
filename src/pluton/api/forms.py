from formskit.formvalidators import FormValidator
from formskit.validators import NotEmpty

from pluton.application.forms import Form


class ClientExistsValidator(FormValidator):
    message = 'Authentication failed'

    def validate(self):
        api_key = self.form.get_value('api_key')
        api_secret = self.form.get_value('api_secret')
        self.form.client = self.form.clients.get_by_api(api_key, api_secret)
        return self.form.client


class AddEventForm(Form):
    with_csrf = False

    def create_form(self):
        self.clients
        self.add_field('api_key', validators=[NotEmpty()])
        self.add_field('api_secret', validators=[NotEmpty()])
        self.add_field('name', validators=[NotEmpty()])
        self.add_field('data', validators=[NotEmpty()])
        self.add_field('state', validators=[NotEmpty()])

        self.add_form_validator(ClientExistsValidator())

    def on_success(self):
        data = self.get_data_dict(True)
        self.events.create(
            self.client.id,
            data['name'],
            data['data'],
            data['state'],
        )
        self.database().commit()
