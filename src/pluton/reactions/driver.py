from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import ReactionLink


class ReactionLinkDriver(ModelDriver):
    model = ReactionLink

    def create(
        self,
        client_id,
        reaction_name,
        event_name,
        priority,
    ):
        return super().create(
            client_id=client_id,
            event_name=event_name,
            reaction_name=reaction_name,
            priority=priority,
        )

    def list_for_event(self, client_id, event_name):
        query = (
            self.query(
                self.model.reaction_name,
            )
            .filter(
                self.model.client_id == client_id,
                self.model.event_name == event_name,
            )
            .order_by(
                self.model.priority.desc(),
            )

        )
        for reactiion in query:
            yield reactiion.reaction_name
