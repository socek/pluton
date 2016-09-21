from mock import MagicMock
from mock import sentinel

from pluton.application.testing import RequestCase
from pluton.plug.testing.cache import cache

from ..widgets import EndpointRowWidget
from ..widgets import EndpointSummaryWidget


class TestEndpointSummaryWidget(RequestCase):
    _object_cls = EndpointSummaryWidget

    @cache
    def mendpoint(self):
        return MagicMock()

    @cache
    def object(self):
        return super().object(self.mendpoint())

    def test_make(self):
        endpoint = self.mendpoint()
        events = self.mevents()

        obj = self.object()
        obj.make()

        assert obj.context == {
            'endpoint_name': endpoint.name,
            'endpoint_id': endpoint.id,
            'api_key': endpoint.api_key,
            'api_secret': endpoint.api_secret,
            'events': events.list_latest.return_value,
            'get_reactions': obj.get_reactions,
            'request': self.mrequest(),
            'route_path': self.mrequest().route_path,
            'widget': obj,
        }
        events.list_latest.assert_called_once_with(endpoint.id)

    def test_get_reactions(self):
        obj = self.object()
        events = self.mevents()

        result = obj.get_reactions(sentinel.group_id)
        events.get_reaction_count(sentinel.group_id)
        assert events.get_reaction_count.return_value == result


class TestEndpointRowWidget(RequestCase):
    _object_cls = EndpointRowWidget

    @cache
    def mendpoint(self):
        return MagicMock()

    @cache
    def object(self):
        return super().object(self.mendpoint())

    def test_make(self):
        obj = self.object()
        events = self.mevents()
        endpoint = self.mendpoint()

        obj.make()

        assert obj.context == {
            'endpoint': endpoint,
            'status': events.get_status.return_value,
            'request': self.mrequest(),
            'route_path': self.mrequest().route_path,
            'widget': obj,
        }
        events.get_status.assert_called_once_with(endpoint.id)
