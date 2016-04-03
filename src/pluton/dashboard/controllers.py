from pluton.plug.controller import Controller
from pluton.plug.controller import JsonController
from pluton.plug.sqlalchemy.plug import DatabasePlug


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.jinja2'

    def create_plugs(self):
        super().create_plugs()
        self.database = self.add_plug(DatabasePlug)

    def make(self):
        print(self.database())
        self.context['ctrl'] = 'one'


class DashboardSecond(JsonController):

    def make(self):
        self.context['ctrl'] = 'two'
