from pluton.plug.fanstatic.application import FanstaticApplication

from .routing import PlutonRouting
from pluton.plug.beaker import BeakerAppPlug
from pluton.plug.haml.app import HamlAppPlug
from pluton.plug.jinja2.app import Jinja2AppPlug
from pluton.plug.sqlalchemy.app import SqlAlchemyPlug


class PlutonApplication(FanstaticApplication):

    class Config(FanstaticApplication.Config):
        routing_cls = PlutonRouting
        module = 'pluton'

    def create_plugs(self):
        self.add_plug(Jinja2AppPlug)
        self.add_plug(SqlAlchemyPlug)
        self.add_plug(HamlAppPlug)
        self.add_plug(BeakerAppPlug)


main = PlutonApplication()
