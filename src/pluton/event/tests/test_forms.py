from mock import sentinel

from pluton.application.testing import FormCase

from ..forms import AddReactionForm
from ..forms import ListRow


class TestAddReactionForm(FormCase):
    _object_cls = AddReactionForm

    def test_get_reactions(self):
        data = list(self.object()._get_reactions())

        assert data == [
            ListRow('print_event', 'Print Event'),
            ListRow('disk_check', 'Disk Check'),
        ]

    def test_on_success(self):
        self.mmatchdict()['event_group_id'] = sentinel.event_group_id
        self.mget_data_dict().return_value = {
            'name': sentinel.name,
        }
        db = self.mdatabase()
        links = self.mreaction_links()

        self.object().on_success()

        links.create.assert_called_once_with(
            sentinel.event_group_id,
            sentinel.name,
        )
        db.assert_called_once_with()
        db.return_value.add.assert_called_once_with(links.create.return_value)
        db.return_value.flush.assert_called_once_with()
