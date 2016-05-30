from mock import MagicMock
from mock import patch
from pytest import raises
from pytest import yield_fixture

from ..exceptions import QuitController
from .test_controller import ControllerFixtures


class TestControllerUtils(ControllerFixtures):

    @yield_fixture
    def mhttp_found(self):
        patcher = patch('pluton.plug.controller.utils.HTTPFound')
        with patcher as mock:
            yield mock

    def test_add_widget(self, controller, mrequest):
        mwidget = MagicMock()
        controller.context = {}

        controller.utils.add_widget('myname', mwidget)

        assert controller.context == {
            'myname': mwidget,
        }

    def test_redirect(self, controller, mrequest, mhttp_found):
        controller.utils.redirect('somewhere', kw='arg')

        assert controller.response == mhttp_found.return_value
        mhttp_found.assert_called_once_with(
            location=mrequest.route_url.return_value,
            headers=mrequest.response.headerlist,
        )
        mrequest.route_url.assert_called_once_with(
            'somewhere',
            kw='arg',
        )

    def test_redirect_with_quit(self, controller):
        with raises(QuitController):
            controller.utils.redirect('somewhere', True, kw='arg')
