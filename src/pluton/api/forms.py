from formskit.formvalidators import FormValidator
from formskit.validators import NotEmpty

from pluton.application.forms import Form


class EndpointExistsValidator(FormValidator):
    message = 'Authentication failed'

    def validate(self):
        api_key = self.form.get_value('api_key')
        api_secret = self.form.get_value('api_secret')
        self.form.endpoint = self.form.endpoints.get_by_api(api_key, api_secret)
        return self.form.endpoint


class AddEventForm(Form):
    with_csrf = False
    always_submitting = True

    def create_form(self):
        self.add_field('api_key', validators=[NotEmpty()])
        self.add_field('api_secret', validators=[NotEmpty()])
        self.add_field('name', validators=[NotEmpty()])
        self.add_field('state', validators=[NotEmpty()])
        self.add_field('arg')

        self.add_form_validator(EndpointExistsValidator())

    def on_success(self):
        data = self.get_data_dict(True)
        event = self.events.create(
            self.endpoint.id,
            data['name'],
            self.raw,
            data['state'],
            data['arg'],
        )
        self.database().add(event)
        self.database().flush()
        self.reactions.react_for_event(event)

    def _get_form_data(self):
        self.raw = {}
        data = {}
        for key, values in self.POST.dict_of_lists().items():
            if key.startswith('raw_'):
                key = key[4:]
                self.raw[key] = values[0]
            else:
                data[key] = values
        return data
