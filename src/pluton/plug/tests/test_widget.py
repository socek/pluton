from mock import sentinel
from ..widget import Widget

from pluton.plug.testing.case import BaseRequestCase


class TestWidget(BaseRequestCase):
    _object_cls = Widget

    def test_create_context(self):
        assert self.object().context == {
            'request': self.request,
            'widget': self.object(),
            'route_path': self.request.route_path,
        }

    def test_add_widget(self):
        self.object().add_widget('my name', sentinel.widget)

        assert self.object().context['my name'] == sentinel.widget

