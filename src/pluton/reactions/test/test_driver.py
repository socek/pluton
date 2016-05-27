from pluton.application.testing import DatabaseCase
from pluton.plug.testing.cache import cache

from ..driver import ReactionLinkDriver
from pluton.endpoint.driver import EndpointDriver
from pluton.event.driver import EventDriver


class TestReactionLinkDriver(DatabaseCase):
    _object_cls = ReactionLinkDriver

    def create_plugs(self):
        super().create_plugs()
        self.events = self.add_plug(EventDriver)
        self.endpoints = self.add_plug(EndpointDriver)

    @cache
    def endpoint(self):
        endpoint = self.endpoints.create('My Super Name')
        self.database().flush()
        return endpoint

    def test_list_for_event(self):
        event = self.events.create_event(
            self.endpoint().id,
            'event name',
            'raw',
            'critical',
            'argg',
        )

        assert list(self.object().list_for_event(event)) == []

        self.object().create(event.group.id, 'reaction name')

        assert list(self.object().list_for_event(event)) == ['reaction name']
