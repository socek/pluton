from pluton.application.controller import Controller


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.haml'

    def make(self):
        self.context['clients'] = self.clients.list()
