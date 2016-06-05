from mock import sentinel

from pluton.application.testing import ControllerCase
from pluton.plug.testing.cache import cache

from ..controllers import CreateEndpoint
from ..controllers import ShowEndpoint
from ..widgets import CreateEndpointFormWidget


class TestShowEndpoint(ControllerCase):
    _object_cls = ShowEndpoint

    @cache
    def mfetch_endpoint(self):
        return self.pobject(self.object(), 'fetch_endpoint')

    @cache
    def mendpoint_summary_widget(self):
        return self.patch('pluton.endpoint.controllers.EndpointSummaryWidget')

    def test_make(self):
        fetch = self.mfetch_endpoint()
        widget = self.mendpoint_summary_widget()
        add_widget = self.mutils().add_widget

        self.object().make()
        fetch.assert_called_once_with()
        widget.assert_called_once_with(fetch.return_value)
        add_widget.assert_called_once_with('endpoint', widget.return_value)

    def test_fetch_endpoint(self):
        self.matchdict()['endpoint_id'] = sentinel.endpoint_id
        endpoints = self.mendpoints()
        endpoint = endpoints.get_by_id.return_value
        self.object().context = {}

        result = self.object().fetch_endpoint()

        assert self.object().context == {'endpoint': result}
        assert result == endpoint
        endpoints.get_by_id.assert_called_once_with(sentinel.endpoint_id)


class TestCreateEndpoint(ControllerCase):
    _object_cls = CreateEndpoint

    def test_make(self):
        add_form = self.mforms().add_form_widget
        add_form.return_value.validate.return_value = True
        redirect = self.mutils().redirect

        self.object().make()

        add_form.assert_called_once_with(CreateEndpointFormWidget)
        add_form.return_value.validate.assert_called_once_with()
        redirect.assert_called_once_with('dashboard')

    def test_make_no_form(self):
        add_form = self.mforms().add_form_widget
        add_form.return_value.validate.return_value = False
        redirect = self.mutils().redirect

        self.object().make()

        add_form.assert_called_once_with(CreateEndpointFormWidget)
        add_form.return_value.validate.assert_called_once_with()
        assert not redirect.called
