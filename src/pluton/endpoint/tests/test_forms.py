from mock import sentinel

from pluton.application.testing import FormCase

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
