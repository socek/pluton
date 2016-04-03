from pluton.plug.controller import Controller
from pluton.plug.controller import JsonController


class Dashboard(JsonController):

    def make(self):
        self.context['ctrl'] = 'one'
        self.utils.redirect('dashboard_second', True)


class DashboardSecond(JsonController):

    def make(self):
        self.context['ctrl'] = 'two'
