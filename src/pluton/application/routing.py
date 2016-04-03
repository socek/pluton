from pluton.plug.routing import Routing


class PlutonRouting(Routing):

    def make(self):
        super().make()
        self.read_from_dotted('pluton.dashboard:routing.yaml')
