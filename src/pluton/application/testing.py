from pluton.plug.sqlalchemy.testing import BaseDatabaseCase
from pluton.plug.testing.cache import cache
from pluton.plug.testing.case import BaseControllerCase
from pluton.plug.testing.case import BasePlugableCase
from pluton.plug.testing.case import BaseRequestCase
from pluton.plug.testing.case import BaseTestCase

from pluton.application.app import main


class TestConfigurationMixin(object):
    _application = main


class TestCase(TestConfigurationMixin, BaseTestCase):
    pass


class RequestCase(TestConfigurationMixin, BaseRequestCase):
    pass


class ControllerCase(TestConfigurationMixin, BaseControllerCase):
    pass


class PlugableCase(TestConfigurationMixin, BasePlugableCase):

    @cache
    def mdatabase(self):
        return self.pobject(self.object(), 'database')


class DatabaseCase(TestConfigurationMixin, BaseDatabaseCase):
    pass
