from ..exceptions import FinalizeController
from ..exceptions import QuitController


class TestFinalizeController(object):

    def test_simple(self):
        exception = FinalizeController('context')

        assert exception.context == 'context'


class TestQuitController(object):

    def test_simple(self):
        exception = QuitController('reason')
        assert exception.response == 'reason'
