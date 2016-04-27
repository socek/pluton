from pluton.application.controller import JsonController


class HideEvent(JsonController):

    def make(self):
        event = self.events.get_by_id(id=self.matchdict['event_id'])
        event.is_hidden = True
        self.database().commit()
        self.utils.redirect('dashboard')
