from mock import MagicMock
from pytest import fixture

from ..requestable import Requestable


class ExampleRequestable(Requestable):
    pass


# class TestRequestable(object):

#     @fixture
#     def model(self):
#         return ExampleRequestable()

#     def test_feed_request(self, model):
#         request = ExampleRequest(None)
#         model.feed_request(request)

#         assert model.request == request

#     def test_feed_request_with_convert(self, model):
#         request = MagicMock()
#         model.feed_request(request)

#         assert model.request.myrequest == request

#     def test_properties(self, model):
#         request = MagicMock()
#         model.request = request
#         model.request.registry = {
#             'settings': 'settings1',
#             'paths': 'paths1',
#         }

#         assert model.registry is request.registry
#         assert model.POST is request.POST
#         assert model.GET is request.GET
#         assert model.matchdict is request.matchdict
#         assert model.route_path is request.route_path
#         assert model.settings == 'settings1'
#         assert model.paths == 'paths1'
