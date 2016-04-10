from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Client


class ClientDriver(ModelDriver):
    model = Client

    def list(self):
        return self.find_all()

    def get_by_api(self, key, secret):
        return (
            self.find_all()
            .filter(
                Client.api_key == key,
                Client.api_secret == secret,
            )
            .first()
        )
