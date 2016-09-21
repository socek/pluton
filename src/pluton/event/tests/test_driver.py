from pytest import raises

from pluton.application.testing import DatabaseCase
from pluton.endpoint.driver import EndpointDriver
from pluton.plug.testing.cache import cache
from pluton.reactions.driver import ReactionLinkDriver

from ..driver import EventDriver
from ..errors import GroupBlockedError


class TestEventDriver(DatabaseCase):
    _object_cls = EventDriver

    def create_plugs(self):
        super().create_plugs()
        self.endpoints = EndpointDriver()
        self.reactions = ReactionLinkDriver()

        self.setup_plugs(
            self.endpoints,
            self.reactions,
        )

    @cache
    def endpoint(self):
        endpoint = self.endpoints.create('My Super Name')
        self.database().flush()
        return endpoint

    def test_create_event(self):
        event = self.object().create_event(
            self.endpoint().id,
            'event name',
            'raw',
            'critical',
            'argg',
        )

        self.database().flush()

        assert event.id is not None
        assert event.raw == 'raw'
        assert event.group.name == 'event name'
        assert event.group.arg == 'argg'
        assert event.group.state == 'critical'
        assert event.group.id is not None
        assert event.group.is_blocked is False

    def test_create_event_on_blocked_group(self):
        endpoint_id = self.endpoint().id
        group = self.object().upsert(
            endpoint_id,
            'event name',
            'argg'
        )
        group.is_blocked = True

        self.database().flush()

        with raises(GroupBlockedError):
            self.object().create_event(
                endpoint_id,
                'event name',
                'raw',
                'critical',
                'argg',
            )

    def test_list_latest(self):

        name = 'event name'
        raw = 'pointless'
        endpoint_id = self.endpoint().id

        self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-1',
        )

        third = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-2',
        )

        second = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-3',
        )
        self.database().flush()

        result = self.object().list_latest(endpoint_id).all()
        expected = [
            (
                third.group.id,
                name,
                None,  # arg
                'critical-3',
                None,  # reaction data
                None,  # description
                second.when_created,
            )
        ]
        assert result == expected

    def test_list_latest_many_groups(self):
        name = 'event name'
        raw = 'pointless'
        endpoint_id = self.endpoint().id

        self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-1',
        )

        third = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-2',
        )

        second = self.object().create_event(
            endpoint_id,
            name + 'elo',
            raw,
            'critical-3',
        )
        self.database().flush()

        result = self.object().list_latest(endpoint_id).all()
        expected = [
            (
                third.group.id,
                name,
                None,  # arg
                'critical-2',
                None,  # reaction data
                None,  # description
                third.when_created,
            ),
            (
                second.group.id,
                name + 'elo',
                None,  # arg
                'critical-3',
                None,  # reaction data
                None,  # description
                second.when_created,
            ),
        ]
        assert result == expected

    def test_list_latest_different_args(self):
        name = 'event name'
        raw = 'pointless'
        endpoint_id = self.endpoint().id

        self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-1',
            'arg1',
        )

        third = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-2',
            'arg1',
        )

        second = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-3',
            'arg2',
        )
        self.database().flush()

        result = self.object().list_latest(endpoint_id).all()
        expected = [
            (
                third.group.id,
                name,
                'arg1',  # arg
                'critical-2',
                None,  # reaction data
                None,  # description
                third.when_created,
            ),
            (
                second.group.id,
                name,
                'arg2',  # arg
                'critical-3',
                None,  # reaction data
                None,  # description
                second.when_created,
            ),
        ]
        assert result == expected

    def test_get_reaction_count(self):
        name = 'event name'
        raw = 'pointless'
        endpoint_id = self.endpoint().id

        event = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-1',
            'arg1',
        )
        self.database().flush()

        result = self.object().get_reaction_count(event.group.id)
        assert result == 0

    def test_get_reaction_count_many(self):
        name = 'event name'
        raw = 'pointless'
        endpoint_id = self.endpoint().id

        event = self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-1',
            'arg1',
        )
        self.database().flush()

        self.reactions.create(event.group.id, 'myname')
        self.reactions.create(event.group.id, 'myname2')

        result = self.object().get_reaction_count(event.group.id)
        assert result == 2

    def test_get_status(self):
        name = 'event name'
        raw = 'pointless'
        endpoint_id = self.endpoint().id

        self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-1',
            'arg1',
        )

        self.object().create_event(
            endpoint_id,
            name,
            raw,
            'critical-2',
            'arg1',
        )

        self.object().create_event(
            endpoint_id,
            name + 'elo',
            raw,
            'normal',
            'arg1',
        )

        self.object().create_event(
            endpoint_id,
            name + 'elo2',
            raw,
            'critical-2',
            'arg1',
        )

        self.database().flush()

        result = self.object().get_status(endpoint_id)
        assert result == {
            'normal': 1,
            'critical-2': 2,
        }
