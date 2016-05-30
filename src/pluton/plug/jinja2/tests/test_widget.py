from mock import MagicMock
from mock import sentinel

from pluton.application.testing import RequestCase
from pluton.plug.testing.cache import cache

from ..widget import MultiWidget
from ..widget import SingleWidget


class ExampleSingleWidget(SingleWidget):
    renderer = sentinel.renderer

    def make(self, *args, **kwargs):
        super().make()
        self.result = MagicMock()
        self.result(*args, **kwargs)


class WidgetCase(RequestCase):

    @cache
    def mrender(self):
        return self.pobject(self.object(), 'render')


class TestSingelWidget(WidgetCase):
    _object_cls = ExampleSingleWidget

    @cache
    def mjinja2(self):
        return self.pobject(self.object(), 'jinja2')

    @cache
    def mmarkup(self):
        return self.patch('pluton.plug.jinja2.widget.Markup')

    def test_simple(self):
        mrender = self.mrender()

        result = self.object()('arg', kw='arg2')

        assert mrender.return_value == result
        mrender.assert_called_once_with(sentinel.renderer)
        self.object().result.assert_called_once_with('arg', kw='arg2')

    def test_render(self):
        mjinja2 = self.mjinja2()
        mmarkup = self.mmarkup()

        self.object().render(sentinel.renderer2)

        mjinja2.env.get_template.assert_called_once_with(sentinel.renderer2)
        template = mjinja2.env.get_template.return_value
        mmarkup.assert_called_once_with(template.render.return_value)
        template.render.assert_called_once_with(
            request=self.request,
            route_path=self.request.route_path,
            widget=self.object(),
        )


class TestMultiWidget(WidgetCase):
    _object_cls = MultiWidget

    def test_simple(self):
        mrender = self.mrender()

        self.object().render_for(sentinel.path, {'context': sentinel.context})

        mrender.assert_called_once_with(sentinel.path)
        assert self.object().context == {
            'request': self.request,
            'route_path': self.request.route_path,
            'widget': self.object(),
            'context': sentinel.context,
        }
