from pluton.plug.application import Application

from .routing import PlutonRouting
from pluton.plug.jinja2.app import Jinja2AppPlug


class PlutonApplication(Application):

    class Config(Application.Config):
        routing_cls = PlutonRouting
        module = 'pluton'

    def create_plugs(self):
        self.jinja2 = self.add_plug(Jinja2AppPlug)


main = PlutonApplication()
