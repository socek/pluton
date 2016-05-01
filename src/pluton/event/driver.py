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
