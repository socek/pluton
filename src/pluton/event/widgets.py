from pluton.application.widget import FormWidget

from .forms import AddReactionForm


class AddReactionFormWidget(FormWidget):
    template = 'pluton.event:templates/widgets/add_reaction_form.haml'
    form = AddReactionForm
