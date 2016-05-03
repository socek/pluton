from pluton.application.controller import Controller
from pluton.application.controller import JsonController

from .widgets import AddReactionFormWidget


class HideEvent(JsonController):

    def make(self):
        event = self.events.get_by_id(id=self.matchdict['event_id'])
        event.is_hidden = True
        self.utils.redirect(
            'endpoints:show',
            endpoint_id=event.endpoint_id,
        )

        self.database().commit()


class ConfigureReactions(Controller):
    renderer = 'pluton.event:templates/admin/configure_reactions.haml'

    def make(self):
        event_group = self.events.get_by_id(self.matchdict['event_group_id'])
        self.context['event_group'] = event_group
        self.context['reactions'] = self.reaction_links.list_for_event_group(
            event_group.id,
        )


class AddReaction(Controller):
    renderer = 'pluton.event:templates/admin/add_reaction.haml'

    def make(self):
        form = self.forms.add_form_widget(AddReactionFormWidget)

        if form.validate():
            self.database().commit()
            self.utils.redirect(
                'events:edit',
                event_group_id=self.matchdict['event_group_id'],
            )


class RemoveReaction(JsonController):

    def make(self):
        reaction = self.reaction_links.get_by_id(
            id=self.matchdict['reaction_id']
        )
        self.utils.redirect(
            'events:edit',
            event_group_id=reaction.event_group_id,
        )
        self.database().delete(reaction)
        self.database().commit()
