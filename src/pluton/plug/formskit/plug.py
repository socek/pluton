from pluton.plug.controller.utils import ControllerUtils
from pluton.plug.plug import RequestPlug

from .widget import FormWidget


class FormskitPlug(RequestPlug):

    def create_plugs(self):
        super().create_plugs()
        self.utils = self.add_plug(ControllerUtils)

    def add_raw_form(self, formcls, *args, **kwargs):
        return formcls(self, *args, **kwargs)

    def add_form(
        self,
        formcls,
        name='form',
        widgetcls=FormWidget,
        *args,
        **kwargs
    ):
        form = self.add_raw_form(formcls, *args, **kwargs)
        widget = widgetcls(form)
        self.utils.add_widget(name, widget)
        return form

    def add_form_widget(self, widget, name='form', *args, **kwargs):
        form, widget = widget.from_form(self, *args, **kwargs)
        self.utils.add_widget(name, widget)
        return form
