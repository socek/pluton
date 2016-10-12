from pluton.plug.controller.utils import ControllerUtils
from pluton.plug.plug import Plug

from .models import BreadCrumb
from .widgets import BreadCrumbWidget


class BreadCrumbPlug(Plug):
    model_cls = BreadCrumb
    widget_cls = BreadCrumbWidget
    template_name = 'breadcrumb'

    def create_plugs(self):
        super().create_plugs()
        self.utils = ControllerUtils()
        self.model = self.model_cls()

        self.setup_plugs(
            self.utils,
            self.model,
        )

    def before_make(self):
        self.widget = self.widget_cls(self.model)
        self.utils.add_widget(
            self.template_name,
            self.widget,
        )
