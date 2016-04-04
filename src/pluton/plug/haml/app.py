from pluton.plug.app_plug import AppPlug


class HamlAppPlug(AppPlug):

    def create_settings(self):
        self.parent.settings['jinja2.extensions'].append(
            'hamlish_jinja.HamlishExtension'
        )

    def create_config(self):
        self.parent.config.add_jinja2_renderer('.haml')
