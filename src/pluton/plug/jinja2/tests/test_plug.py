from pyramid_jinja2 import IJinja2Environment

from pluton.application.testing import RequestCase

from ..plug import Jinja2Plug


class TestJinja2Plug(RequestCase):
    _object_cls = Jinja2Plug

    def test_env(self):
        self.mregistry()

        assert self.object().env == self.mregistry().queryUtility.return_value
        self.mregistry().queryUtility.assert_called_once_with(
            IJinja2Environment,
            name='.jinja2',
        )
