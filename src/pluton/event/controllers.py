from pluton.application.controller import Controller
from pluton.application.controller import JsonController
from pluton.plug.testing.cache import cache

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

    @property
    @cache
    def event_group(self):
        return self.events.get_by_id(self.matchdict['event_group_id'])

    @property
    @cache
    def endpoint(self):
        if self.event_group.endpoint_id:
            return self.event_group.endpoint

    def make(self):
        self.context['event_group'] = self.event_group
        self.context['reactions'] = self.reaction_links.list_for_event_group(
            self.event_group.id,
        )

    def get_breadcrumbs_vars(self):
        data = super().get_breadcrumbs_vars()
        data['endpoint_id'] = str(self.event_group.endpoint_id)
        return data


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
        db = self.database()

        reaction = self.reaction_links.get_by_id(
            id=self.matchdict['reaction_id']
        )
        self.utils.redirect(
            'events:edit',
            event_group_id=reaction.event_group_id,
        )
        db.delete(reaction)
        db.commit()
