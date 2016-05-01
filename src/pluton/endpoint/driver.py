from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Endpoint


class EndpointDriver(ModelDriver):
    model = Endpoint

    def create(
        self,
        name
    ):
        return super().create(
            name=name,
        )

    def list(self):
        return self.find_all()

    def get_by_api(self, key, secret):
        return (
            self.find_all()
            .filter(
                Endpoint.api_key == key,
                Endpoint.api_secret == secret,
            )
            .first()
        )
