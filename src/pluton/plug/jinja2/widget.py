from jinja2 import Markup

from pluton.plug.jinja2.plug import Jinja2Plug
from pluton.plug.widget import Widget


class BaseWidget(Widget):

    def create_plugs(self):
        super().create_plugs()
        self.jinja2 = self.add_plug(Jinja2Plug)

    def render(self, renderer):
        template = self.jinja2.env.get_template(renderer)
        return Markup(template.render(**self.context))


class SingleWidget(BaseWidget):

    def __call__(self, *args, **kwargs):
        self._create_context()
        self.make(*args, **kwargs)
        return self.render(self.renderer)

    def make(self):
        pass


class MultiWidget(BaseWidget):

    def render_for(self, path, context):
        self._create_context()
        self.context.update(context)
        return self.render(path)
