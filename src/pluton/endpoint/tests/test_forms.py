from io import StringIO
from mock import MagicMock
from mock import sentinel
from yaml import dump

from pluton.application.testing import FormCase
from pluton.plug.testing.cache import cache

from ..forms import ConfigureEndpointForm
from ..forms import CreateEndpointForm


class TestCreateEndpointForm(FormCase):
    _object_cls = CreateEndpointForm

    def test_on_success(self):
        data = self.mget_data_dict()
        data.return_value = {
            'name': sentinel.name,
        }
        endpoints = self.mendpoints()
        db = self.mdatabase()

        self.object().on_success()

        endpoints.create.assert_called_once_with(
            sentinel.name,
        )
        data.assert_called_once_with(True)
        db.assert_called_once_with()
        db.return_value.add.assert_called_once_with(
            endpoints.create.return_value,
        )
        db.return_value.flush.assert_called_once_with()


class TestConfigureEndpointForm(FormCase):
    _object_cls = ConfigureEndpointForm

    _file = StringIO(dump({
        'events': [
            {
                'name': 'myname',
                'arg': 'myarg',
            }
        ]
    }))

    @cache
    def object(self):
        return super().object(sentinel.endpoint_id)

    def test_on_success(self):
        data = self.mget_data_dict()
        mock = MagicMock()
        mock.file = self._file
        data.return_value = {
            'server': mock,
        }
        self.mevents()

        self.object().on_success()

        self.mevents().create_event.assert_called_once_with(
            sentinel.endpoint_id,
            'myname',
            raw=None,
            state='normal',
            arg='myarg',
        )
