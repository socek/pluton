from mock import MagicMock

from pluton.application.testing import TestCase
from pluton.plug.testing.cache import cache

from ..application import FanstaticApplication


class TestFanstaticApplication(TestCase):
    _object_cls = FanstaticApplication

    @cache
    def mfastatic(self):
        return self.patch('pluton.plug.fanstatic.application.Fanstatic')

    def test_return_wsgi_app(self):
        self.mfastatic()
        self.object().config = MagicMock()
        self.object().settings = MagicMock()

        result = self.object()._return_wsgi_app()

        assert self.mfastatic().return_value == result
        self.mfastatic().assert_called_once_with(
            self.object().config.make_wsgi_app.return_value,
            **self.object().settings['fanstatic']
        )
