from pluton.plug.controller import Controller as BaseController
from pluton.plug.controller import JsonController as BaseJsonController
from pluton.plug.formskit.plug import FormskitPlug
from pluton.reactions.plugs import ReactionRunner
from pluton.breadcrumbs.plugs import BreadCrumbPlug

from .plugs import PluggedMixin
from .plugs import RequestPluggedMixin


class PluggedController(PluggedMixin, BaseController):

    def create_plugs(self):
        super().create_plugs()
        self.reactions = ReactionRunner()
        self.breadcrumb = BreadCrumbPlug()

        self.setup_plugs(
            self.reactions,
            self.breadcrumb,
        )


class Controller(RequestPluggedMixin, PluggedController):

    def get_breadcrumbs_vars(self):
        return dict(self.request.matchdict)


class JsonController(PluggedController, BaseJsonController):

    def create_plugs(self):
        super().create_plugs()
        self.forms = FormskitPlug()

        self.setup_plugs(
            self.forms,
        )
