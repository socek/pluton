from mock import sentinel

from pluton.application.testing import ControllerCase

from ..controllers import AddReaction
from ..controllers import ConfigureReactions
from ..controllers import HideEvent
from ..controllers import RemoveReaction


class TestAddReaction(ControllerCase):
    _object_cls = AddReaction


class TestConfigureReactions(ControllerCase):
    _object_cls = ConfigureReactions

    def test_make(self):
        events = self.mevents()
        links = self.mreaction_links()
        self.matchdict()['event_group_id'] = sentinel.event_group_id

        self.object().make()

        assert self.object().context == {
            'event_group': events.get_by_id.return_value,
            'reactions': links.list_for_event_group.return_value,
        }
        events.get_by_id.assert_called_once_with(sentinel.event_group_id)
        links.list_for_event_group.assert_called_once_with(
            events.get_by_id.return_value.id,
        )


class TestHideEvent(ControllerCase):
    _object_cls = HideEvent

    def test_make(self):
        db = self.mdatabase()
        events = self.mevents()
        utils = self.mutils()
        self.matchdict()['event_id'] = sentinel.event_id
        event = events.get_by_id.return_value

        self.object().make()

        events.get_by_id.assert_called_once_with(id=sentinel.event_id)
        utils.redirect.assert_called_once_with(
            'endpoints:show',
            endpoint_id=event.endpoint_id,
        )

        db.assert_called_once_with()
        db.return_value.commit.assert_called_once_with()


class TestRemoveReaction(ControllerCase):
    _object_cls = RemoveReaction
