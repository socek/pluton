from pluton.plug.controller import Controller
from pluton.plug.controller import JsonController
from pluton.dashboard.driver import ClientDriver


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.jinja2'

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)

    def make(self):
        self.context['ctrl'] = 'one'
        self.context['clients'] = self.clients.find_all()


class DashboardSecond(JsonController):

    def make(self):
        self.context['ctrl'] = 'two'
