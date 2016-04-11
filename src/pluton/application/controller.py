from pluton.plug.controller import Controller as BaseController
from pluton.plug.controller import JsonController as BaseJsonController

from .plugs import PluggedMixin
from .plugs import RequestPluggedMixin


class PluggedController(PluggedMixin, BaseController):
    pass


class Controller(RequestPluggedMixin, PluggedController):
    pass


class JsonController(PluggedController, BaseJsonController):
    pass
