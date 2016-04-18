from pluton.application.controller import JsonController

from .forms import AddEventForm


class AddEvent(JsonController):

    def make(self):
        form = AddEventForm(self.forms)
        form.validate()
        self.context['form'] = form.get_report()
        self.database().commit()
