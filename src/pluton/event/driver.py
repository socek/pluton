from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Event


class EventDriver(ModelDriver):
    model = Event

    def create(
        self,
        client_id,
        name,
        data,
        state,
    ):
        return super().create(
            client_id=client_id,
            name=name,
            data=data,
            state=state,
        )

    def list_latest(self, client_id):
        return (
            self.find_all()
            .distinct(self.model.name)
            .filter(
                self.model.client_id == client_id,
            )
            .order_by(
                self.model.name,
                self.model.when_created.desc(),
            )
        )
