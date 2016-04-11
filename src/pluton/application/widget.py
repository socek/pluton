from pluton.plug.jinja2.widget import SingleWidget as BaseSingleWidget

from .plugs import RequestPluggedMixin


class SingleWidget(RequestPluggedMixin, BaseSingleWidget):
    pass
