from pluton.plug.controller import JsonController


class Dashboard(JsonController):

    def make(self):
        self.context['ctrl'] = 'one'
        self.utils.redirect('dashboard_second')


class DashboardSecond(JsonController):

    def make(self):
        self.context['ctrl'] = 'two'
