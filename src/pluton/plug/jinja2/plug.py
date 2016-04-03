from pluton.plug.plug import RequestPlug
from pyramid_jinja2 import IJinja2Environment


class Jinja2Plug(RequestPlug):

    @property
    def env(self):
        return self.registry.queryUtility(IJinja2Environment, name='.jinja2')
