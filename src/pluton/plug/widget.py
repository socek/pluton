from .plug import RequestPlug


class Widget(RequestPlug):

    def feed_parent(self, parent):
        super().feed_parent(parent)
        self._create_context()

    def _create_context(self):
        self.context = {
            'request': self.request,
            'widget': self,
            'route_path': self.request.route_path,
        }

    def add_widget(self, name, obj):
        self.context[name] = obj
