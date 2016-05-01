from collections import defaultdict
from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Event


class EventDriver(ModelDriver):
    model = Event

    def create(
        self,
        endpoint_id,
        name,
        raw,
        state,
        arg=None,
    ):
        return super().create(
            endpoint_id=endpoint_id,
            name=name,
            raw=raw,
            state=state,
            arg=arg,
        )

    def list_latest(self, endpoint_id):
        query = (
            self.find_all()
            .distinct(self.model.name, self.model.arg)
            .filter(
                self.model.endpoint_id == endpoint_id,
            )
            .order_by(
                self.model.name,
                self.model.arg,
                self.model.when_created.desc(),
            )
        )
        for obj in query:
            if not obj.is_hidden:
                yield obj

    def get_status(self, endpoint_id):
        """
        This method returns number of events in each status,
        example: {'normal': 2, 'critical': 1}
        """
        status = defaultdict(lambda: 0)
        status['normal'] = 0
        for event in self.list_latest(endpoint_id):
            status[event.state] += 1
        return status
