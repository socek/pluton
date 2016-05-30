from ..plug import RequestPlug

from mock import MagicMock


class TestRequestPlug(object):

    def test_endpoints(self):
        parent = MagicMock()
        plug = RequestPlug()
        plug.feed_parent(parent)
        request = parent.main.request

        assert plug.registry == request.registry
        assert plug.POST == request.POST
        assert plug.GET == request.GET
        assert plug.json == request.json
        assert plug.matchdict == request.matchdict
        assert plug.route_path == request.route_path
