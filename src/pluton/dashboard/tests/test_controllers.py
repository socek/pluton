from mock import MagicMock

from pluton.plug.testing.cache import cache

from pluton.application.testing import ControllerCase
from pluton.dashboard.controllers import Dashboard


class TestDashboard(ControllerCase):
    _object_cls = Dashboard

    @cache
    def mget_endpoints(self):
        return self.pobject(self.object(), 'get_endpoints')

    @cache
    def mendpoints(self):
        return self.pobject(self.object(), 'endpoints')

    @cache
    def mendpoint_row_widget(self):
        return self.patch('pluton.dashboard.controllers.EndpointRowWidget')

    def test_make(self):
        mock = self.mget_endpoints()

        self.object().make()

        assert self.context() == {
            'endpoints': mock.return_value,
        }

    def test_get_endpoints(self):
        endpoint = MagicMock()
        self.mendpoints().list.return_value = [endpoint]
        self.mendpoint_row_widget()

        result = list(self.object().get_endpoints())

        widget = self.mendpoint_row_widget().return_value
        assert result == [widget]
        self.mendpoint_row_widget().assert_called_once_with(endpoint)
        widget.feed_parent.assert_called_once_with(self.object())
