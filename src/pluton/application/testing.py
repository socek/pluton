from pluton.plug.formskit.testing import BaseFormCase
from pluton.plug.sqlalchemy.testing import BaseDatabaseCase
from pluton.plug.testing.cache import cache
from pluton.plug.testing.case import BaseControllerCase
from pluton.plug.testing.case import BasePlugableCase
from pluton.plug.testing.case import BaseRequestCase
from pluton.plug.testing.case import BaseTestCase

from pluton.application.app import main


class TestConfigurationMixin(object):
    _application = main

    @cache
    def mreaction_links(self):
        return self.pobject(self.object(), 'reaction_links')

    @cache
    def mdatabase(self):
        return self.pobject(self.object(), 'database')

    @cache
    def mevents(self):
        return self.pobject(self.object(), 'events')

    @cache
    def mforms(self):
        return self.pobject(self.object(), 'forms')

    @cache
    def mendpoints(self):
        return self.pobject(self.object(), 'endpoints')

    @cache
    def mreactions(self):
        return self.pobject(self.object(), 'reactions')


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


class FormCase(TestConfigurationMixin, BaseFormCase):
    pass
