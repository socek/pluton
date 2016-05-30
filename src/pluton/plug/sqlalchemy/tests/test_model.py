from pluton.application.testing import PlugableCase

from ..model import Model


class TestModel(PlugableCase):
    _object_cls = Model

    def test_repr(self):
        obj = self.object()
        assert repr(obj) == 'Model (None)'
        obj.id = 123
        assert repr(obj) == 'Model (123)'
