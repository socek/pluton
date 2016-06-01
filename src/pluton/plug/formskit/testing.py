from pluton.plug.testing.cache import cache
from pluton.plug.testing.case import BaseRequestCase


class BaseFormCase(BaseRequestCase):

    @cache
    def object(self):
        return super().object(self)

    @cache
    def mget_data_dict(self):
        return self.pobject(self.object(), 'get_data_dict')
