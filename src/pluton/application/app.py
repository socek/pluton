from pluton.plug.application import Application

from .routing import PlutonRouting


class PlutonApplication(Application):

    class Config(Application.Config):
        routing_cls = PlutonRouting
        module = 'pluton'


main = PlutonApplication()
