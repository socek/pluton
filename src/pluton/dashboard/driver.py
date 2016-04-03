from pluton.plug.sqlalchemy.driver import ModelDriver

from .models import Client


class ClientDriver(ModelDriver):
    model = Client
