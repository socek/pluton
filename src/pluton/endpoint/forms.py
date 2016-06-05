from formskit.validators import NotEmpty

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
