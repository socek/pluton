from pluton.plug.controller import Controller
from pluton.plug.controller import JsonController


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.jinja2'

    def make(self):
        self.context['ctrl'] = 'one'


class DashboardSecond(JsonController):

    def make(self):
        self.context['ctrl'] = 'two'
