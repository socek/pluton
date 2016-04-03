from .exceptions import FinalizeController
from .exceptions import QuitController
from .utils import ControllerUtils
from ..plug import RequestPlug


class Controller(RequestPlug):

    def __init__(self, root_factory, request):
        self.feed_request(request)
        self.root_factory = root_factory
        self.response = None

    def create_plugs(self):
        super().create_plugs()
        self.utils = self.add_plug(ControllerUtils)

    def feed_request(self, request):
        self.application = request.registry['application']
        self.request = request
        self.create_plugs()

    def __call__(self):
        return self.run()

    def run(self):
        try:
            self._before_context()
            self._create_context()
            self._before_make()
            self._make()
            self._after_make()
            return self._get_response()
        except QuitController as end:
            self._before_quit()
            return end.response or self.response

    def _make(self):
        try:
            self.make()
        except FinalizeController as finalizer:
            self.context.update(finalizer.context)

    def _create_context(self):
        self.context = {
            'request': self.request,
            'route_path': self.request.route_path,
        }

    def make(self):
        pass

    def _get_response(self):
        if self.response is None:
            self._create_widgets()
            return self.context
        else:
            return self.response

    def _before_context(self):
        pass

    def _before_make(self):
        pass

    def _after_make(self):
        pass

    def _create_widgets(self):
        pass

    def _before_quit(self):
        pass
