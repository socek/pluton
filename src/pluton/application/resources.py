from fanstatic import Library
from fanstatic import Resource

from pluton.plug.fanstatic.plug import FanstaticPlug

library = Library('impex', 'static')

bootstrap_js = Resource(
    library,
    'bootstrap/bootstrap.min.js',
    bottom=True,
)
bootstrap_css = Resource(
    library,
    'bootstrap/bootstrap.min.css',
    depends=[
        bootstrap_js,
    ]
)


class PlutonFanstaticPlug(FanstaticPlug):

    def append_resources(self):
        self.add_resource('bootstrap', bootstrap_css)
