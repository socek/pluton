from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Client


class ClientDriver(ModelDriver):
    model = Client

    def list(self):
        return self.find_all()
