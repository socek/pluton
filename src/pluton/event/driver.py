from collections import defaultdict
from sqlalchemy import func
from pluton.plug.sqlalchemy.driver import ModelDriver

from pluton.reactions.models import ReactionLink

from .models import Event
from .models import EventGroup


class EventDriver(ModelDriver):
    model = EventGroup
    model_event = Event

    def create_event(
        self,
        endpoint_id,
        name,
        raw,
        state,
        arg=None,
    ):
        group = self.upsert(endpoint_id, name, arg)

        event = Event()
        event.raw = raw
        event.group = group
        self.database().add(event)
        return event

    def upsert(self, endpoint_id, name, arg):
        return super().upsert(
            endpoint_id=endpoint_id,
            name=name,
            arg=arg,
        )

    def list_latest(self, endpoint_id):
        return (
            self.query(
                self.model.id,
                self.model.name,
                self.model.arg,
                self.model.state,
                self.model.reaction_data,
                self.model.description,
                self.model_event.when_created,
            )
            .join(self.model_event)
            .filter(
                self.model.endpoint_id == endpoint_id,
                self.model.is_hidden.isnot(True)
            )
            .order_by(
                self.model.name,
                self.model.arg,
                self.model_event.when_created.desc(),
            )
            .distinct(
                self.model.name,
                self.model.arg,
            )
        )

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

    def get_reaction_count(self, group_id):
        return (
            self.query(
                func.count(ReactionLink.id)
            )
            .join(self.model)
            .group_by(self.model.id)
            .filter(
                ReactionLink.event_group_id == group_id
            )
            .scalar()
        )
