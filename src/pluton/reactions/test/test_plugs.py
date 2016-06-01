from mock import MagicMock

from pluton.application.testing import PlugableCase
from pluton.plug.testing.cache import cache

from ..plugs import ReactionRunner


class TestReactionRunner(PlugableCase):
    _object_cls = ReactionRunner

    @cache
    def mreaction_links(self):
        return self.pobject(self.object(), 'reaction_links')

    def test_add_reaction(self):
        reaction = MagicMock()
        reaction.name = 'myname'
        self.object().reactions = {}

        self.object().add_reaction(reaction)

        assert self.object().reactions == {'myname': reaction}

    def test_react_for_event(self):
        event = MagicMock()
        reaction = MagicMock()
        reaction.name = 'reaction name'
        self.mreaction_links().list_for_event.return_value = [reaction.name]

        self.object().add_reaction(reaction)
        self.object().react_for_event(event)

        reaction.react.assert_called_once_with(event)
