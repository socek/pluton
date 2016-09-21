from pyramid.exceptions import HTTPForbidden

from .forms import AddEventForm
from pluton.application.controller import JsonController
from pluton.event.errors import GroupBlockedError


class AddEvent(JsonController):

    def make(self):
        try:
            form = AddEventForm(self.forms)
            form.validate()
            self.context['form'] = form.get_report()
            self.database().commit()
        except GroupBlockedError:
            self.response = HTTPForbidden()
