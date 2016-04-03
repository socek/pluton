from importlib import import_module
from os import path

from pyramid.config import Configurator

from .settings import SettingsFactory
from .routing import Routing


class Application(object):

    class Config(object):
        routing_cls = Routing
        module = None

    def __init__(self):
        self.plugs = {}
        self.app_plugs = []
        self.create_plugs()

    def add_plug(self, cls):
        obj = cls()
        obj.feed_parent(self)
        self.app_plugs.append(obj)

    def create_plugs(self):
        pass

    def __call__(self, settings={}):
        return self.run_uwsgi(settings)

    def run_uwsgi(self, settings={}):
        self._create_app(settings, 'uwsgi')
        return self._return_wsgi_app()

    def run_tests(self, settings={}):
        self._create_app(settings, 'tests')

    def run_shell(self, settings={}):
        self._create_app(settings, 'shell')

    def run_command(self, settings={}):
        self._create_app(settings, 'command')

    def _create_app(self, settings={}, settings_name='uwsgi'):
        self._generate_settings(settings, settings_name)
        self._create_config()
        self._generate_registry(self.config.registry)
        self._create_routing()

    def _generate_settings(
        self,
        settings,
        endpoint,
        factorycls=SettingsFactory,
    ):
        self.settings = settings
        self.paths = {}
        self._populte_default_settings()
        settings_module = self._get_settings_module()
        factory = factorycls(settings_module, self.settings, self.paths)
        settings, paths = factory.get_for(endpoint)
        self.settings = settings
        self.paths = paths

        for plug in self.app_plugs:
            plug.create_settings()

    def _get_settings_module(self):
        return '%s.application' % (self.Config.module, )

    def _populte_default_settings(self):
        module = import_module(self.Config.module)
        self.settings['project'] = self.Config.module
        self.paths['project'] = path.dirname(module.__file__)

        for plug in self.app_plugs:
            plug.populate_default_settings()

    def _create_config(self):
        kwargs = self._get_config_kwargs()
        self.config = Configurator(**kwargs)

        for plug in self.app_plugs:
            plug.create_config()

    def _get_config_kwargs(self):
        return {
            'settings': self.settings.to_dict(),
        }

    def _generate_registry(self, registry):
        self.registry = registry
        registry['settings'] = self.settings
        registry['paths'] = self.paths
        registry['application'] = self

        for plug in self.app_plugs:
            plug.generate_registry(registry)

    def _create_routing(self):
        self.routing = self.Config.routing_cls(self)
        self.routing.make()

    def _return_wsgi_app(self):
        return self.config.make_wsgi_app()
