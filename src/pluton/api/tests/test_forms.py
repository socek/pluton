from mock import MagicMock
from mock import sentinel

from pluton.application.testing import FormCase, TestCase

from ..forms import AddEventForm
from ..forms import EndpointExistsValidator


class TestAddEventForm(FormCase):
    _object_cls = AddEventForm

    def test_on_success(self):
        db = self.mdatabase()
        data = self.mget_data_dict()
        create = self.mevents().create_event
        reactions = self.mreactions()
        endpoint = self.object().endpoint = MagicMock()
        self.object().raw = sentinel.raw
        data.return_value = {
            'name': sentinel.name,
            'state': sentinel.state,
            'arg': sentinel.arg,
        }

        self.object().on_success()

        data.assert_called_once_with(True)
        create.assert_called_once_with(
            endpoint.id,
            sentinel.name,
            sentinel.raw,
            sentinel.state,
            sentinel.arg,
        )
        assert create.return_value.group.is_hidden is False
        db.return_value.add.assert_called_once_with(create.return_value)
        db.return_value.flush.assert_called_once_with()
        db.assert_called_once_with()
        reactions.react_for_event.assert_called_once_with(create.return_value)

    def test_get_form_data(self):
        self.m_post().dict_of_lists.return_value = {
            'raw_something': ['one', 'two', 'three'],
            'something2': ['2one', '2two', '2three'],
        }

        assert self.object()._get_form_data() == {
            'something2': ['2one', '2two', '2three'],
        }
        assert self.object().raw == {'something': 'one'}


class TestEndpointExistsValidator(TestCase):
    _object_cls = EndpointExistsValidator

    def test_validate(self):
        form = MagicMock()
        self.object().set_form(form)

        result = self.object().validate()

        assert result == form.endpoint
        form.endpoints.get_by_api.assert_called_once_with(
            form.get_value.return_value,
            form.get_value.return_value,
        )
