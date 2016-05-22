from pluton.plug.sqlalchemy.testing import BaseDatabaseCase
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
    pass


class DatabaseCase(TestConfigurationMixin, BaseDatabaseCase):
    pass
