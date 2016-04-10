from pluton.client.driver import ClientDriver
from pluton.event.driver import EventDriver
from pluton.plug.formskit.models import PostForm
from pluton.plug.formskit.plug import FormskitPlug
from pluton.plug.sqlalchemy.plug import DatabasePlug


class Form(PostForm):

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)
        self.events = self.add_plug(EventDriver)
        self.forms = self.add_plug(FormskitPlug)
        self.database = self.add_plug(DatabasePlug)
