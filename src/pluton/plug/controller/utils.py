from pyramid.httpexceptions import HTTPFound

from .exceptions import QuitController
from pluton.plug.plug import RequestPlug


class ControllerUtils(RequestPlug):

    def redirect(self, to, quit=False, **kwargs):
        url = self.request.route_url(to, **kwargs)
        self.main.response = HTTPFound(
            location=url,
            headers=self.request.response.headerlist,
        )
        if quit:
            raise QuitController(self.parent.response)

    def add_widget(self, name, obj):
        obj.feed_parent(self)
        self.main.context[name] = obj
