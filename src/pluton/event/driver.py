from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Event


class EventDriver(ModelDriver):
    model = Event

    def create(
        self,
        client_id,
        name,
        raw,
        state,
        arg=None,
    ):
        return super().create(
            client_id=client_id,
            name=name,
            raw=raw,
            state=state,
            arg=arg,
        )

    def list_latest(self, client_id):
        return (
            self.find_all()
            .distinct(self.model.name, self.model.arg)
            .filter(
                self.model.client_id == client_id,
            )
            .order_by(
                self.model.name,
                self.model.arg,
                self.model.when_created.desc(),
            )
        )
