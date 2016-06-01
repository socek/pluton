from mock import MagicMock

from pluton.application.testing import PlugableCase
from pluton.plug.testing.cache import cache

from ..reactions import DiskCheckReaction
from ..reactions import PrintEvent


class TestPrintEvent(PlugableCase):
    _object_cls = PrintEvent

    @cache
    def mprint(self):
        return self.patch("builtins.print", autospec=True)

    def test_sanity(self):
        self.mprint()
        event = MagicMock()
        event.group.name = 'group'
        event.raw = 'raw'

        self.object().react(event)

        self.mprint().assert_called_once_with(
            'React:',
            event.group.name,
            event.raw,
        )


class TestDiskCheckReaction(PlugableCase):
    _object_cls = DiskCheckReaction

    def test_reaction(self):
        db = self.mdatabase()
        event = MagicMock()
        event.group.name = 'group'
        event.raw = {'raw': 'arg'}

        self.object().react(event)

        db.return_value.flush.assert_called_once_with()
        db.assert_called_once_with()

        assert event.group.description == 'raw: arg<br>\n'
