from formskit.validators import NotEmpty
from yaml import load

from pluton.application.forms import Form


class CreateEndpointForm(Form):

    def create_form(self):
        self.add_field('name', label='Nazwa', validators=[NotEmpty()])

    def on_success(self):
        db = self.database()
        data = self.get_data_dict(True)
        event = self.endpoints.create(
            data['name'],
        )
        db.add(event)
        db.flush()


class ConfigureEndpointForm(Form):

    def __init__(self, parent, endpoint_id):
        super().__init__(parent)
        self.endpoint_id = endpoint_id

    def create_form(self):
        self.add_field('server', label='Plik', validators=[NotEmpty()])

    def on_success(self):
        data = self.get_data_dict(True)
        data = load(data['server'].file)
        for event in data['events']:
            event = self.events.create_event(
                self.endpoint_id,
                event['name'],
                raw=None,
                state='normal',
                arg=event['arg'],
            )
            event.group.is_hidden = False
