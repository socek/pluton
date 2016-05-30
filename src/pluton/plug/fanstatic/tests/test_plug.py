from mock import MagicMock
from mock import sentinel

from pluton.application.testing import RequestCase

from ..plug import FanstaticPlug


class TestFanstaticPlug(RequestCase):
    _object_cls = FanstaticPlug

    def test_add_resource(self):
        self.object().resources = {}

        self.object().add_resource('my name', sentinel.lib)

        assert self.object().resources == {'my name': sentinel.lib}

    def test_need(self):
        mock = MagicMock()
        self.object().resources = {'woman': mock}

        assert self.object().need('woman') == ''
        mock.need.assert_called_once_with()

    def test_before_make(self):
        self.context = {}

        self.object().before_make()

        assert self.object().resources == self.object().default
        assert self.context == {'need': self.object().need}
