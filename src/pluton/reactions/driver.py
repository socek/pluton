from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import ReactionLink


class ReactionLinkDriver(ModelDriver):
    model = ReactionLink

    def create(
        self,
        event_group_id,
        reaction_name,
    ):
        return super().create(
            reaction_name=reaction_name,
            event_group_id=event_group_id,
        )

    def list_for_event(self, event):
        for reaction in self.list_for_event_group(event.group_id):
            yield reaction.reaction_name

    def list_for_event_group(self, group_id):
        return (
            self.query(
                self.model
            )
            .filter(
                self.model.event_group_id == group_id
            )
            .order_by(
                self.model.priority.desc(),
            )

        )
