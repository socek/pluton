from mock import MagicMock

from pluton.plug.testing.cache import cache
from pluton.plug.testing.case import TestHelpersMixin

from ..application import Application


class TestApplication(TestHelpersMixin):

    @cache
    def application(self):
        app = Application()
        app.Config.module = 'pluton.plug'
        return app

    @cache
    def mimport_module(self):
        return self.patch('pluton.plug.application.import_module')

    @cache
    def mconfigurator(self):
        return self.patch('pluton.plug.application.Configurator')

    @cache
    def msettings_factory(self):
        return self.patch('pluton.plug.application.SettingsFactory')

    @cache
    def mrouting(self):
        return self.patch('pluton.plug.application.Routing')

    @cache
    def mpopulte_default_settings(self):
        return self.pobject(self.application(), '_populte_default_settings')

    @cache
    def mgenerate_settings(self):
        def side_effect(*args, **kwargs):
            self.application().settings = MagicMock()
            self.application().paths = {}
        return self.pobject(
            self.application(),
            '_generate_settings',
            side_effect=side_effect,
        )

    def test_uwsgi(self):
        mconfigurator = self.mconfigurator()
        msettings = self.mgenerate_settings()

        result = self.application()()

        mconfigurator.assert_called_once_with(
            settings=self.application().settings.to_dict.return_value,
        )
        mconfigurator.return_value.make_wsgi_app.assert_called_once_with()

        assert result == mconfigurator.return_value.make_wsgi_app.return_value
        msettings.assert_called_once_with({}, 'uwsgi')

    def test_shell(self):
        mconfigurator = self.mconfigurator()
        msettings = self.mgenerate_settings()

        result = self.application().run_shell()

        mconfigurator.assert_called_once_with(
            settings=self.application().settings.to_dict.return_value,
        )
        assert mconfigurator.return_value.make_wsgi_app.called is False

        assert result is None
        msettings.assert_called_once_with({}, 'shell')

    def test_tests(self):
        mconfigurator = self.mconfigurator()
        msettings = self.mgenerate_settings()

        result = self.application().run_tests()

        mconfigurator.assert_called_once_with(
            settings=self.application().settings.to_dict.return_value,
        )
        assert mconfigurator.return_value.make_wsgi_app.called is False

        assert result is None
        msettings.assert_called_once_with({}, 'tests')

    def test_command(self):
        mconfigurator = self.mconfigurator()
        msettings = self.mgenerate_settings()

        result = self.application().run_command()

        mconfigurator.assert_called_once_with(
            settings=self.application().settings.to_dict.return_value,
        )
        assert mconfigurator.return_value.make_wsgi_app.called is False

        assert result is None
        msettings.assert_called_once_with({}, 'command')
