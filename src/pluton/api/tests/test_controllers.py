from mock import sentinel

from pluton.application.testing import ControllerCase
from pluton.plug.testing.cache import cache

from ..controllers import AddEvent


class TestAddEvent(ControllerCase):
    _object_cls = AddEvent

    @cache
    def madd_event_form(self):
        return self.patch('pluton.api.controllers.AddEventForm')

    def test_make(self):
        form = self.madd_event_form().return_value
        db = self.mdatabase()
        self.object().forms = sentinel.forms

        self.object().make()

        db.assert_called_once_with()
        db.return_value.commit.assert_called_once_with()
        self.madd_event_form().assert_called_once_with(sentinel.forms)
        form.validate.assert_called_once_with()
        self.object().context = {
            'form': form.get_report.return_value
        }
        form.get_report.assert_called_once_with()
