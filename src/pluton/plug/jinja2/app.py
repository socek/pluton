from pluton.plug.app_plug import AppPlug


class Jinja2AppPlug(AppPlug):

    def create_settings(self):
        self.parent.settings['jinja2.extensions'] = []

    def create_config(self):
        self.parent.config.include('pyramid_jinja2')
