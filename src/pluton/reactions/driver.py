from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import ReactionLink


class ReactionLinkDriver(ModelDriver):
    model = ReactionLink

    def create(
        self,
        endpoint_id,
        reaction_name,
        event_name,
        priority,
    ):
        return super().create(
            endpoint_id=endpoint_id,
            event_name=event_name,
            reaction_name=reaction_name,
            priority=priority,
        )

    def list_for_event(self, event):
        query = (
            self.query(
                self.model.reaction_name,
            )
            .filter(
                self.model.endpoint_id == event.group.endpoint_id,
                self.model.event_name == event.group.name,
            )
            .order_by(
                self.model.priority.desc(),
            )

        )
        for reactiion in query:
            yield reactiion.reaction_name
