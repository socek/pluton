from pluton.application.testing import DatabaseCase

from ..driver import EndpointDriver
from pluton.event.models import Event
from pluton.event.models import EventGroup
from pluton.reactions.models import ReactionLink


class TestEndpointDriver(DatabaseCase):
    _object_cls = EndpointDriver

    def test_create(self):
        obj = self.object().create('my name')

        assert obj.name == 'my name'

    def test_list(self):
        self.reset_table()

        endpoint = self.object().create('my fine name')
        self.database().flush()

        assert self.object().list().all() == [endpoint]

    def test_get_by_api(self):
        endpoint = self.object().create('api name')
        self.database().flush()

        result = self.object().get_by_api(endpoint.api_key, endpoint.api_secret)
        assert result == endpoint

    def reset_table(self):
        self.database().query(ReactionLink).delete()
        self.database().query(Event).delete()
        self.database().query(EventGroup).delete()
        super().reset_table()
