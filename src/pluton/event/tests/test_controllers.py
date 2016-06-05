from mock import sentinel

from pluton.application.testing import ControllerCase

from ..controllers import AddReaction
from ..controllers import ConfigureReactions
from ..controllers import HideEvent
from ..controllers import RemoveReaction
from ..widgets import AddReactionFormWidget


class TestAddReaction(ControllerCase):
    _object_cls = AddReaction

    def test_make(self):
        madd_form_widget = self.mforms().add_form_widget
        form = madd_form_widget.return_value
        db = self.mdatabase()
        utils = self.mutils()
        self.matchdict()['event_group_id'] = sentinel.event_group_id

        self.object().make()

        madd_form_widget.assert_called_once_with(AddReactionFormWidget)
        form.validate.assert_called_once_with()
        db.assert_called_once_with()
        db.return_value.commit.assert_called_once_with()
        utils.redirect.assert_called_once_with(
            'events:edit',
            event_group_id=sentinel.event_group_id,
        )

    def test_make_no_form(self):
        madd_form_widget = self.mforms().add_form_widget
        form = madd_form_widget.return_value
        db = self.mdatabase()
        utils = self.mutils()
        self.matchdict()['event_group_id'] = sentinel.event_group_id
        form.validate.return_value = False

        self.object().make()

        madd_form_widget.assert_called_once_with(AddReactionFormWidget)
        form.validate.assert_called_once_with()
        assert not db.called
        assert not db.return_value.commit.called
        assert not utils.redirect.called


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

    def test_make(self):
        db = self.mdatabase()
        reactions = self.mreaction_links()
        utils = self.mutils()
        reaction = reactions.get_by_id.return_value
        self.matchdict()['reaction_id'] = sentinel.reaction_id

        self.object().make()

        reactions.get_by_id.assert_called_once_with(id=sentinel.reaction_id)
        utils.redirect.assert_called_once_with(
            'events:edit',
            event_group_id=reaction.event_group_id,
        )
        db.return_value.delete.assert_called_once_with(reaction)
        db.return_value.commit.assert_called_once_with()
        db.assert_called_once_with()
