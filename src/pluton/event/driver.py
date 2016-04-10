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
