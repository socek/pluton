from collections import namedtuple
from formskit.validators import NotEmpty

from pluton.application.forms import Form

ListRow = namedtuple('list_row', ['value', 'label'])


class AddReactionForm(Form):

    def create_form(self):
        self.add_field(
            'name',
            label='Nazwa',
            validators=[NotEmpty()],
        ).set_avalible_values(self._get_reactions)

    def _get_reactions(self):
        yield ListRow('print_event', 'Print Event')
        yield ListRow('disk_check', 'Disk Check')

    def on_success(self):
        data = self.get_data_dict(True)
        reaction = self.reaction_links.create(
            self.matchdict['event_group_id'],
            data['name'],
        )
        self.database().add(reaction)
        self.database().flush()
