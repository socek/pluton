from .plug import RequestPlug


class Widget(RequestPlug):

    def feed_request(self, request):
        super().feed_request(request)
        self._create_context()

    def _create_context(self):
        self.context = {
            'request': self.request,
            'widget': self,
            'route_path': self.request.route_path,
        }

    def add_widget(self, name, obj):
        obj.feed_request(self.request)
        self.context[name] = obj
        print(self.context)
